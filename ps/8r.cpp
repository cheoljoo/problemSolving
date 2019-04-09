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
 
int C;
int N,K;
int garrN[MAX];	// input

set<int> innerSet[MAX*120];
int innerCnt=0;
set<int>::iterator innerIt;

struct classcomp {
  bool operator() (const int& s1, const int& s2) const
  {
	  //printf("compare outer: s1: %d  s2: %d\n",s1,s2);
	  // https://stackoverflow.com/questions/16182958/how-to-compare-two-stdset
	  set<int>::iterator it1=innerSet[s1].begin();
	  set<int>::iterator it2=innerSet[s2].begin();
	  for( ;(it1 != innerSet[s1].end()) || (it2 != innerSet[s2].end());it1++,it2++){
		  if(it1 == innerSet[s1].end()){ return true; }
		  if(it2 == innerSet[s2].end()){ return false; }
		  //printf("inner t1: %d  t2: %d\n",*it1,*it2);
		  if(*it1 < *it2){ return true; }
		  if(*it1 > *it2){ return false; }
	  }
	  return true;
  }
};

set<int,classcomp> outerSet[MAX];
int outerCnt=1;
set<int,classcomp >::iterator outerIt;


void
printSet()
{
	cout << "_____________________" << endl;
	for(int i=0;i<outerCnt;i++){
		for ( outerIt=outerSet[i].begin() ; outerIt != outerSet[i].end(); outerIt++ ){
			cout << "Out[" << i << "] ";
			cout << "(" << *outerIt << ") In: ";
			for( innerIt = innerSet[*outerIt].begin() ; innerIt != innerSet[*outerIt].end() ; innerIt++){
				cout << " " << *innerIt;
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
	for ( outerIt=outerSet[i].begin() ; outerIt != outerSet[i].end(); outerIt++ , num++){
		if(num == K){
			;; cout << "i:" << i << " , K[" << K << "] ";
			;; cout << "(" << *outerIt << ") In: ";
			for( innerIt = innerSet[*outerIt].begin() ; innerIt != innerSet[*outerIt].end() ; innerIt++){
				printf("%d ",*innerIt);
			}
			printf("\n");
		}
	}
	return i;
}


int 
findIS(int arr[],const int size)
{
#if 0
	for(int i=0;i<MAX;i++){ outerSet[i].clear(); }
	for(int i=0;i<MAX*MAX;i++){ innerSet[i].clear(); }
#endif

	// init
	outerCnt = 1;
	outerSet[0].clear();
	outerSet[1].clear();
	innerCnt = 0;
	innerSet[0].clear();

	for(int input=0;input<size;input++){
		;; printf("input [ %d ] : %d\n",input,arr[input]);
		if(input == 0){  
			//printf("-1-\n");
			innerSet[0].insert(arr[input]);
			innerCnt++;
			innerSet[innerCnt].clear();
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
				set<int>::reverse_iterator rit;
				if(innerSet[*outerIt].empty()){ printf("ERROR : input%d i%d *outerIt%d\n",input, i,*outerIt);  continue; }
				rit=innerSet[*outerIt].rbegin(); 
				//printf("-3- %d\n",*rit);
				if(*rit < arr[input]){
					//printf("-4- %d %d\n",innerCnt,*outerIt);
					innerSet[innerCnt].insert( (-1) * (*outerIt) );	// - index to indirect acces instead of copy
					innerSet[innerCnt].insert(arr[input]);
					if(outerSet[i+1].empty()){
						outerSet[i+1].insert(innerCnt);
						outerCnt++;
						outerSet[outerCnt].clear();
					} else {
						outerSet[i+1].insert(innerCnt);
					}
					innerCnt++;
					innerSet[innerCnt].clear();
					flagAdded = 1;
				}
			}
			if(flagAdded == 1){
				break;
			}
			if(i == 1){		// flagAdded == 0
				innerSet[innerCnt].insert(arr[input]);
				outerSet[1].insert(innerCnt);
				innerCnt++;
				innerSet[innerCnt].clear();
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
