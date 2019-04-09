#include <iostream>
#include <vector>

using namespace std;
	vector<vector<int>> edge(1000001,vector<int>());
	int nodeVisited[1000001];
	int nodeEarly[1000001];
	int nodeEarlyCount = 0;


void findEarlyAdaptor(const int startNode)
{
	if(nodeVisited[startNode] == 1){ return ;}
	nodeVisited[startNode] = 1;

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
		if(nodeVisited[p] == 1){ continue ;}
		findEarlyAdaptor(p);
		// nodeEarlyCount[startNode] += nodeEarlyCount[p];
		if( 1 != nodeEarly[p]){
			flag = 1;
		}
	}
	if(1 == flag){
		nodeEarly[startNode] = 1;
		// nodeEarlyCount[startNode] += 1;
		nodeEarlyCount ++;
	}
}

int main()
{ 
    std::ios_base::sync_with_stdio(false);
	int NODE;
	int startNode = 0;
	cin >> NODE;
	//vector<vector<int>> edge(NODE+1,vector<int>());
	//vector<bool> nodeVisited(NODE+1,false);
	//vector<bool> nodeEarly(NODE+1,false);		// false : NORMAL , true : EARLY
	//int nodeVisited[1000001];
	//int nodeEarly[1000001];
	//for(int j=0;j<NODE+1;j++){
		//nodeVisited[j] = 0;
		//nodeEarly[j] = 0;
	//}
	//vector<int> nodeEarlyCount(NODE+1,0);		
	//int nodeEarlyCount = 0;
	for(int j=1;j<NODE;j++){
		int node1,node2;
		cin >> node1 >> node2;
		edge[node1].push_back(node2);
		edge[node2].push_back(node1);
		if(startNode == 0){ startNode = node1; }
	}

	// find EarlyAdaptor (Camera)  count 
	findEarlyAdaptor(startNode);
	cout << nodeEarlyCount << endl;

	return 0;
}
