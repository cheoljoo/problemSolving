#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

void findEarlyAdaptor(vector<vector<int>>& edge , vector<bool>& nodeVisited, vector<bool>& nodeEarly, int& nodeEarlyCount, vector<bool>& hasEarlyInChild, const int startNode, const int parentNode)
{
	if(nodeVisited[startNode] == true){ return ;}
	nodeVisited[startNode] = true;

    // cout << "find (parent=" << parentNode << ": start=" << startNode << endl;

	int flag = -1;
	for(auto p : edge[startNode]){
		//if(nodeVisited[p] == true){ continue ;}
        if(p == parentNode){ continue ;}

        if(flag == -1){ flag = 0; }
        // cout << "EDGE in find loop (parent=" << parentNode << ": start=" << startNode << ") : ";
        // cout << startNode << " -> " << p << endl;
		findEarlyAdaptor(edge ,nodeVisited, nodeEarly, nodeEarlyCount, hasEarlyInChild, p, startNode);
        // cout << "EDGE out find loop : EarlyCount=" << nodeEarlyCount << endl;
		if( (true == nodeEarly[p]) || (true == hasEarlyInChild[p]) ){
			flag = 1;
		}
	}
    // cout << "find flag (parent=" << parentNode << ": start=" << startNode << ": flag=" << flag << endl;
	if(0 == flag){
        if(parentNode >= 0){ hasEarlyInChild[parentNode] = true; }
		nodeEarly[startNode] = true;
		nodeEarlyCount ++;
        // cout << "(flag=0) EarlyCount=" << nodeEarlyCount << endl;
    } 
    if(1 == flag){
		int flag1=0;
        for(auto p : edge[startNode]){
            if(p == parentNode){ continue ;}
            // cout << "(flag=1) p :" << p << ", EarlyCount=" << nodeEarlyCount << ",E:" << nodeEarly[p] << ",hasE:" << hasEarlyInChild[p] << endl;
            if( (nodeEarly[p] == false) && (hasEarlyInChild[p] == false) ){
				flag1 = 1;
            }
        }
		if(flag1 == 1){
            if(parentNode >= 0){ hasEarlyInChild[parentNode] = true; }
	        nodeEarly[startNode] = true;
	        nodeEarlyCount ++;
            // cout << "(flag=1) EarlyCount=" << nodeEarlyCount << endl;
		}
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);

	int CASE;
	cin >> CASE;
	for(int i=0;i<CASE;i++){
		int NODE,EDGE;
		int cameraCount = 0;
		cin >> NODE >> EDGE;
		vector<vector<int>> edge(NODE,vector<int>());
		vector<bool> nodeVisited(NODE,false);
		vector<bool> nodeEarly(NODE,false);		// false : NORMAL , true : EARLY
		vector<bool> hasEarlyInChild(NODE,false);		// false : NORMAL , true : EARLY
		for(int j=0;j<EDGE;j++){
			int node1,node2;
			cin >> node1 >> node2;
			edge[node1].push_back(node2);
			edge[node2].push_back(node1);
		}

		// find EarlyAdaptor (Camera)  count 
		int answer = 0;
		for(int j=0;j<NODE;j++){
			if(nodeVisited[j] == true){ continue;}
			if(edge[j].size() == 0){ 
				answer ++;
			} else {
				int nodeEarlyCount = 0;
				findEarlyAdaptor(edge ,nodeVisited, nodeEarly, nodeEarlyCount, hasEarlyInChild,j, -1);
				answer += nodeEarlyCount;
			}
		}
		cout << answer << endl;

		edge.clear();
		nodeVisited.clear();
		nodeEarly.clear();
	}

	return 0;
}
