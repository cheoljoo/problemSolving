#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

enum {
	NORMAL,
	EARLY
};

void findEarlyAdaptor(vector<vector<int>>& edge , vector<bool>& nodeVisited, vector<bool>& nodeEarly, vector<int>& nodeEarlyCount, const int startNode, const int parentNode)
{
	if(nodeVisited[startNode] == true){ return ;}
	nodeVisited[startNode] = true;

    /*
	bool leafFlag = true;
	for(auto p : edge[startNode]){
		if(nodeVisited[p] == true){ continue ;}
		leafFlag = false; 
		break;
	}
	if(true == leafFlag){
		nodeEarly[startNode] = false;
		return ;
	}
    */

	int flag = 0;
	for(auto p : edge[startNode]){
		if(nodeVisited[p] == true){ continue ;}
        cout << "EDGE in find (parent=" << parentNode << ": start=" << startNode << ") : ";
        cout << startNode << " -> " << p << endl;
		findEarlyAdaptor(edge ,nodeVisited, nodeEarly, nodeEarlyCount, p,startNode);
		nodeEarlyCount[startNode] += nodeEarlyCount[p];
		if(true == nodeEarly[p]){
			flag = 1;
		}
	}
	if(0 == flag){
		nodeEarly[startNode] = true;
		nodeEarlyCount[startNode] += 1;
	}
}

int main()
{
	int CASE;
	cin >> CASE;
	for(int i=0;i<CASE;i++){
		int NODE,EDGE;
		int cameraCount = 0;
		cin >> NODE >> EDGE;
		vector<vector<int>> edge(NODE,vector<int>());
		vector<bool> nodeVisited(NODE,false);
		vector<bool> nodeEarly(NODE,false);		// false : NORMAL , true : EARLY
		vector<int> nodeEarlyCount(NODE,0);		
		for(int j=0;j<EDGE;j++){
			int node1,node2;
			cin >> node1 >> node2;
			edge[node1].push_back(node2);
			edge[node2].push_back(node1);
		}

		// for debugging
		cout << "-------------------" << endl;
		cout << "CASE : " << i << endl;
		cout << "NODE : " << NODE << endl;
		cout << "EDGE : " << EDGE << endl;
		for(int j=0;j<NODE;j++){
			if(edge[j].size() <= 0){ continue; }
			cout << "node " << j << " : " ;
				for(int p : edge[j]){
					cout << " " << p;
				}
				cout << endl;
		}

		// find EarlyAdaptor (Camera)  count 
		int answer = 0;
		for(int j=0;j<NODE;j++){
			if(nodeVisited[j] == true){ continue;}
			if(edge[j].size() == 0){ 
				answer ++;
			} else {
				findEarlyAdaptor(edge ,nodeVisited, nodeEarly, nodeEarlyCount, j,-1);
				answer += nodeEarlyCount[j];
			}
		}
		cout << answer << endl;

		// for debugging
		cout << "===================" << endl;
		cout << "CASE : " << i << endl;
		cout << "NODE : " << NODE << endl;
		cout << "EDGE : " << EDGE << endl;
		for(int j=0;j<NODE;j++){
			if(edge[j].size() <= 0){ continue; }
			cout << "node " << j << " : " ;
				for(int p : edge[j]){
					cout << " " << p;
				}
				cout << ", early:" << nodeEarly[j] ;
				cout << ", earlyCount:" << nodeEarlyCount[j] ;
				cout << endl;
		}


		edge.clear();
		nodeVisited.clear();
		nodeEarly.clear();
		nodeEarlyCount.clear();

	}

	return 0;
}
