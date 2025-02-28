#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
 
using namespace std;
 
#define DBG 0
 
#define MAX 100001
#define MIN -1
struct intersection {
    int A;
    int B;
    int inSecCnt;  // count of intersection
};
 
int N;
struct intersection IC[MAX];

int getMIN=0;
int A,B,C;
int compA,compB;
 
void printDebug()
{
    cout << "====  N:"<< N << endl;
    for(int i=0;i<N;i++){
        cout << "[" << i << "] A:" << IC[i].A << ",B:" << IC[i].B << ",inSecCnt:" << IC[i].inSecCnt << endl;  
    }
}

bool compareValue (int i,int j) { return (IC[i].A < IC[j].A); }
 
int findLargeIdxFromSecond(const int depth,vector<int>& vidx,const int size)
{
	vector<int> vidxNext;
    int max = -1;
    int idx = -1;
    for(auto i : vidx){
        if(max < IC[i].inSecCnt){ 
            max = IC[i].inSecCnt; 
            idx = i;
        }
    }
    for(auto i : vidx){
        if(max ==  IC[i].inSecCnt){ 
			vidxNext.push_back(i);
		}
	}

#if DBG
	for(int i=0;i<depth;i++){
		cout << "\t" ;
	}
	printf("==findSecond{cross:%d} size:%lu== ",max,vidx.size());
	for(auto i : vidx){
        printf("i%d[v%d] ",i,IC[i].A);
	}
	printf("  :Chooseidx=%d:ChooseValue=%d\n", idx, IC[idx].A);
#endif

	if(size != vidxNext.size()){
		return findLargeIdxFromSecond(depth+1,vidxNext,static_cast<int>(vidxNext.size()) );
	} else {
		return vidxNext[0];
	}
}

int findMaxIdx()
{
	vector<int> vidx;
    int max=0;
    int idx = -1;

    for(int i=0;i<N;i++){
        if(max < IC[i].inSecCnt){ 
            max = IC[i].inSecCnt; 
            idx = i;
        }
    }

	if(idx == -1){ return idx; }

    for(int i=0;i<N;i++){
        if(max ==  IC[i].inSecCnt){ 
			vidx.push_back(i);
		}
	}

#if DBG
	printf("==findMaxIdx{cross:%d} size:%lu== ",max,vidx.size());
	for(auto i : vidx){
        printf("i%d[v%d] ",i,IC[i].A);
	}
	printf("\n");
#endif

	if(vidx.size() == 1){ return vidx[0]; }

	idx = findLargeIdxFromSecond(1,vidx,static_cast<int>(vidx.size()) );

#if DBG
	printf("++findMaxIdx{cross:%d} size:%lu== ",max,vidx.size());
	for(auto i : vidx){
        printf("i%d[v%d] ",i,IC[i].A);
	}
	printf("  :Chooseidx=%d:ChooseValue=%d\n", idx, IC[idx].A);
#endif

	return idx;
}
 
int main(int argc,char *argv[])
{
 
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d %d",&(IC[i].A),&(IC[i].B));
    }

	if(argc > 1){ getMIN = 1; }
 
#if DBG
    printDebug();
#endif
 
    for(int i=0;i<N;i++){
        A = IC[i].A;
        B = IC[i].B;
 
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
    printDebug();
#endif
     
    vector<int> v;
    int ans = 0;
    while(1){
        int idx = findMaxIdx();
        if(idx == -1){ break; }
        A = IC[idx].A;
        B = IC[idx].B;
 
        IC[idx].inSecCnt = 0;
        ans++;
        v.push_back(A);
 
        for(int j=0;j<N;j++){
            if(idx == j) continue;
            compA = (IC[j].A -A < 0) ? -1 : 1;
            compB = (IC[j].B -B < 0) ? -1 : 1;
            if( compA*compB < 0 ){
                (IC[j].inSecCnt) --;
            }
        }
#if DBG
        printDebug();
        cout << "idx:" << idx << ",A:" << A << endl;
#endif
    };
 
#if DBG
    printf("==========getMIN:%d\n",getMIN);
    for (auto x : v){
        printf("ans value %d\n",x);
    }
    printf("==========\n");
#endif

    printf("%d\n",ans);
    sort(v.begin(), v.end()); 
    for (auto x : v){
        printf("%d\n",x);
    }
         
#if DBG
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
