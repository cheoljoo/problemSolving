#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
#include <iterator>
#include <unistd.h>
 
using namespace std;
 
#define MAX 500
#define MAX2 (MAX*300)
 
int C;
int N,K;
int garrN[MAX];	// input

int innerIS[MAX2][2];
int innerCntIS[MAX2];
int innerCnt=0;

struct classcomp {
  bool operator() (const int& s1, const int& s2) const
  {
	  //printf("compare outer: s1: %d  s2: %d\n",s1,s2);
	  // https://stackoverflow.com/questions/16182958/how-to-compare-two-stdset
	  for(int i=0 ;(i < innerCntIS[s1]) || (i < innerCntIS[s2]);i++){
		  if(i == innerCntIS[s1]){ return true; }
		  if(i == innerCntIS[s2]){ return false; }
		  //printf("inner t1: %d  t2: %d\n",*it1,*it2);
		  if(innerIS[s1][i] < innerIS[s2][i]){ return true; }
		  if(innerIS[s1][i] > innerIS[s2][i]){ return false; }
	  }
	  return true;
  }
};

set<int> outerSet[MAX];
int outerCnt=1;
set<int>::iterator outerIt;


void
printSet()
{
	cout << "_____________________" << endl;
	for(int i=0;i<outerCnt;i++){
		for ( outerIt=outerSet[i].begin() ; outerIt != outerSet[i].end(); outerIt++ ){
			cout << "Out[" << i << "] ";
			cout << "(" << *outerIt << ") In: ";
			for(int v=0; v < innerCntIS[*outerIt] ; v++){
				cout << " " << innerIS[*outerIt][v];
			}
			cout << endl;
		}
	}
	cout << "=====================" << endl;
	for(int i=0;i<MAX;i++){
		if(innerCntIS[i] > 0){
			cout << i << ": size " << innerCntIS[i] << " : ";
			for(int v=0; v < innerCntIS[i] ; v++){
				cout << " " << innerIS[i][v];
			}
			cout << endl;
		}
	}
	cout << "=====================" << endl;
}


int
getK()
{
	int i = outerCnt-1;
	int num = 1;
	printf("%d\n",i);
	vector<int> vans[outerSet[i].size()];
	int vcnt=0;
	for ( outerIt=outerSet[i].begin() ; outerIt != outerSet[i].end(); outerIt++,vcnt++){
		vector<int> a;
		for(int v= innerCntIS[*outerIt]-1; v >= 0 ; v--){
			a.push_back( innerIS[*outerIt][v] );
		}
		while(a.size()){
			int val = a.back();
			a.pop_back();
			if(val <= 0){
				val *= -1;
				for(int v= innerCntIS[val]-1; v >= 0 ; v--){
					a.push_back( innerIS[val][v] );
				}
			} else {
				vans[vcnt].push_back(val);
			}
		};
	}
	for(int i=0;i<vcnt;i++){
		;; cout << "vcnt:" << i << " , K[" << K << "] ";
		;; cout << " In: ";
		for(int j=0;j<vans[i].size();j++){
			printf("%d ",vans[i][j]);
		}
		printf("\n");
	}
	/*
	for ( outerIt=outerSet[i].begin() ; outerIt != outerSet[i].end(); outerIt++ , num++){
		if(num == K){
			;; cout << "i:" << i << " , K[" << K << "] ";
			;; cout << "(" << *outerIt << ") In: ";
			for(int v=0; v < innerCntIS[*outerIt] ; v++){
				printf("%d ",innerIS[*outerIt][v]);
			}
			printf("\n");
		}
	}
	*/
	return i;
}


int 
findIS(int arr[],const int size)
{
#if 0
	for(int i=0;i<MAX;i++){ outerSet[i].clear(); }
#endif


	// init
	outerCnt = 1;
	outerSet[0].clear();
	outerSet[1].clear();
	innerCnt = 0;
	for(int i=0;i<MAX2;i++){ innerCntIS[i] = 0; }
	//--innerSet[0].clear();

	for(int input=0;input<size;input++){
		;; printf("input [ %d ] : %d\n",input,arr[input]);
		if(input == 0){  
			//printf("-1-\n");
			innerIS[0][0] = arr[input];
			innerCntIS[0] = 1;
			innerCnt++;
			outerSet[1].insert(0);
			outerCnt++;
			outerSet[outerCnt].clear();
			;; printSet();
			continue;
		}

		for(int i = outerCnt-1 ; i >= 1 ; i--){
			//printf("-2-\n");
			outerSet[outerCnt].clear();
			int flagAdded= 0;
			for( outerIt=outerSet[i].begin() ; outerIt != outerSet[i].end(); outerIt++ ){
				int rit;
				if(innerCntIS[*outerIt] == 0){ printf("ERROR : input%d i%d *outerIt%d\n",input, i,*outerIt);  continue; }
				rit=innerIS[*outerIt][innerCntIS[*outerIt]-1]; 
				//printf("-3- %d\n",rit);
				if(rit < arr[input]){
					//--innerSet[innerCnt] = innerSet[*outerIt];	// copy
					innerIS[innerCnt][0] = (-1) * (*outerIt);
					innerIS[innerCnt][1] = arr[input];
					innerCntIS[innerCnt] = 2;
					if(outerSet[i+1].empty()){
						outerSet[i+1].insert(innerCnt);
						outerCnt++;
						outerSet[outerCnt].clear();
					} else {
						outerSet[i+1].insert(innerCnt);
					}
					innerCnt++;
					flagAdded = 1;
				}
			}
			if(flagAdded == 1){
				break;
			}
			if(i == 1){		// flagAdded == 0
				innerIS[innerCnt][0] = arr[input];
				innerCntIS[innerCnt] = 1;
				outerSet[1].insert(innerCnt);
				innerCnt++;
			}
		}
		;; printSet();

	}

	return getK();
}


int main(int argc,char *argv[])
{
#if 0
	// https://www.coderslexicon.com/ordering-sets-in-c/
	set<int> a;
    // Even though we insert in unsorted order, they come out sorted
    // according to value. Standard thing with a Set container.
    a.insert(1);
    a.insert(5);
    a.insert(2);

    // Iterator for ints
    set<int>::iterator it;

    // Show they are in order
    for ( it=a.begin(); it != a.end(); it++ )
        cout << " " << *it;
    cout << endl << endl;
#endif
 
    scanf("%d", &C);
	for(int c = 0 ; c < C ; c++){
		scanf("%d %d",&N,&K);
		for(int n=0;n<N;n++){
			scanf("%d",&garrN[n]);
		}

		// printf("%d\n",findIS(garrN,N));
		findIS(garrN,N);

    }

    return 0;
}
