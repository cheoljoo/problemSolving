#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

void findEarlyAdaptor(vector<vector<int>>& edge , vector<bool>& nodeVisited, vector<bool>& nodeEarly, vector<int>& nodeEarlyCount, const int startNode)
{
	if(nodeVisited[startNode] == true){ return ;}
	nodeVisited[startNode] = true;

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

	int flag = 0;
	for(auto p : edge[startNode]){
		if(nodeVisited[p] == true){ continue ;}
		findEarlyAdaptor(edge ,nodeVisited, nodeEarly, nodeEarlyCount, p);
		nodeEarlyCount[startNode] += nodeEarlyCount[p];
		if(true != nodeEarly[p]){
			flag = 1;
		}
	}
	if(1 == flag){
		nodeEarly[startNode] = true;
		nodeEarlyCount[startNode] += 1;
	}
}

int main()
{
	int NODE,EDGE;
	int startNode = 0;
	cin >> NODE;
	vector<vector<int>> edge(NODE+1,vector<int>());
	vector<bool> nodeVisited(NODE+1,false);
	vector<bool> nodeEarly(NODE+1,false);		// false : NORMAL , true : EARLY
	vector<int> nodeEarlyCount(NODE+1,0);		
	for(int j=1;j<NODE;j++){
		int node1,node2;
		cin >> node1 >> node2;
		edge[node1].push_back(node2);
		edge[node2].push_back(node1);
		if(startNode == 0){ startNode = node1; }
	}

	// for debugging
	cout << "-------------------" << endl;
	cout << "NODE : " << NODE << endl;
	for(int j=0;j<=NODE;j++){
		if(edge[j].size() <= 0){ continue; }
		cout << "node " << j << " : " ;
		for(int p : edge[j]){
			cout << " " << p;
		}
		cout << endl;
	}

	// find EarlyAdaptor (Camera)  count 
	findEarlyAdaptor(edge ,nodeVisited, nodeEarly, nodeEarlyCount, startNode);
	cout << nodeEarlyCount[startNode] << endl;

	// for debugging
	cout << "===================" << endl;
	cout << "NODE : " << NODE << endl;
	for(int j=0;j<=NODE;j++){
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

	return 0;
}
