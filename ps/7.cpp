#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
 
using namespace std;
 
#define MAX 500
 
int C;
int N,M;
int garrN[MAX];	// input
int gIS[MAX][MAX];
int gcntIS[MAX];
int gcnt;

int findgIS(int arr[],const int size)
{
	gcnt = 0;
	for(int i=0;i<MAX;i++){ gcntIS[i] = 0;  }

	int flagAdded= 0;
	for(int i=0;i<size;i++){
		if(i == 0){ gcnt = 1; gcntIS[0] = 1; gIS[0][0]=arr[i]; }
		for(int idx = gcnt-1 ; idx >= 0 ; idx--){
			if(gIS[idx][idx] < arr[i]){
				if(idx == gcnt-1){		// last longest line then add new line
					for(int t = 0;t<=idx; t++){
						gIS[idx+1][t] = gIS[idx][t];
					}
					gIS[idx+1][idx+1] = arr[i];
					gcntIS[idx+1] = gcntIS[idx] + 1;
					gcnt++;
					//cout << "last index idx:" << idx;
					//cout << "gcnt:" << gcnt;
					//cout << "gcntIS:" << gcntIS[idx+1];
					//cout << endl;
				} else if(gIS[idx+1][idx+1] > arr[i]){
					for(int t = 0;t<=idx; t++){
						gIS[idx+1][t] = gIS[idx][t];
					}
					gIS[idx+1][idx+1] = arr[i];
					//cout << "NO last index idx:" << idx;
					//cout << "gcnt:" << gcnt;
					//cout << "gcntIS:" << gcntIS[idx+1];
					//cout << endl;
				}
				break;
			} 
			if( (idx == 0) && (gIS[0][0] > arr[i]) ){
				gIS[0][0] = arr[i];

			}
		}
	}

	return gcntIS[gcnt-1];
}

int main(int argc,char *argv[])
{
 
    scanf("%d", &C);
	for(int c = 0 ; c < C ; c++){
		scanf("%d",&N);
		for(int n=0;n<N;n++){
			scanf("%d",&garrN[n]);
		}

		printf("%d\n",findgIS(garrN,N));

    }

    return 0;
}
