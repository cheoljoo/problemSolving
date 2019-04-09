#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <iterator>

using namespace std;

#define DBG 0

#define MAX 500000
struct intersection {
	int A;
	int B;
	int inSecCnt;  // count of intersection
};

int N;
int ansMin = MAX;
vector<int> vans;
struct intersection IC[MAX];
int compA,compB;

void printDebug(const char* s)
{
#if DBG
	
	cout << "{" << s << "} ====  N:"<< N << endl;
	for(int i=0;i<N;i++){
		cout << "{" << s << "} [" << i << "] A:" << IC[i].A << ",B:" << IC[i].B << ",inSecCnt:" << IC[i].inSecCnt << endl;	
	}
#endif
}

int findMaxIdx(vector<int>& vidx)
{
	int max=0;
	for(int i=0;i<N;i++){
		if(max < IC[i].inSecCnt){ 
			max = IC[i].inSecCnt; 
		}
	}

	for(int i=N-1;i>=0;i--){
		if(max == IC[i].inSecCnt){ 
			vidx.push_back(i);
		}
	}
	
	return max;
}

void BFS(vector<int>& path , int& ans)
{
	vector<int> vidx;
	int max;
	max = findMaxIdx(vidx);
	if(max == 0){
#if DBG
		cout << "ans:" << ans << ", ansMin:" << ansMin  << endl;;
		cout << "path:";
		for(auto v : path) cout << " " << v; 
		cout << " , ans:" << ans << endl;
#endif
		if(ans < ansMin){
			ansMin = ans;
			vans = path;
#if DBG
			cout << "vans:";
			for(auto v : vans) cout << " " << v; 
			cout << " , ansMin:" << ansMin << endl;
			printDebug("min");
#endif
		}
		return;
	}
	for(auto idx : vidx){
		int A = IC[idx].A;
		int B = IC[idx].B;
		int oldC = IC[idx].inSecCnt;
#if DBG
		cout << "path:";
		for(auto v : path) cout << " " << v; 
		cout << " , idx:" << idx << ",A:" << A << endl;
		printDebug("call");
#endif
		IC[idx].inSecCnt = 0;
		ans++;
		path.push_back(A);
		for(int j=0;j<N;j++){
			if(idx == j) continue;
			compA = (IC[j].A -A < 0) ? -1 : 1;
			compB = (IC[j].B -B < 0) ? -1 : 1;
			if( compA*compB < 0 ){
				(IC[j].inSecCnt) --;
			}
		}

		BFS(path,ans);

		// recover after return
		for(int j=0;j<N;j++){
			if(idx == j) continue;
			compA = (IC[j].A -A < 0) ? -1 : 1;
			compB = (IC[j].B -B < 0) ? -1 : 1;
			if( compA*compB < 0 ){
				(IC[j].inSecCnt) ++;
			}
		}
		path.pop_back();
		ans--;
		IC[idx].inSecCnt = oldC;
#if DBG
		cout << "path:";
		for(auto v : path) cout << " " << v; 
		cout << " , idx:" << idx << ",A:" << A << endl;
		printDebug("return");
#endif
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);

	scanf("%d", &N);
	for(int i=0;i<N;i++){
		scanf("%d %d",&(IC[i].A),&(IC[i].B));
	}

#if DBG
	printDebug("main");
#endif

	for(int i=0;i<N;i++){
		int A = IC[i].A;
		int B = IC[i].B;

		for(int j=0;j<N;j++){
			if(i == j) continue;
			compA = (IC[j].A -A < 0) ? -1 : 1;
			compB = (IC[j].B -B < 0) ? -1 : 1;
			if( compA*compB < 0 ){
				(IC[i].inSecCnt) ++;
			}
		}

	}

#if DBG
	printDebug("init");
#endif
	
	vector<int> v;
	int ans = 0;
	BFS(v,ans);

	printf("%d\n",ansMin);
	sort(vans.begin(), vans.end()); 
    for (auto x : vans){
		printf("%d\n",x);
	}
        
#if 0
	vector<int> a,b;
	for(int j=0;j<N;j++){
		a.push_back(IC[j].A);
		b.push_back(IC[j].B);
	}
	sort(a.begin(), a.end()); 
    for (auto x : a){
		printf("a : %d\n",x);
	}
	sort(b.begin(), b.end()); 
    for (auto x : b){
		printf("b : %d\n",x);
	}
#endif
  

	return 0;
}
