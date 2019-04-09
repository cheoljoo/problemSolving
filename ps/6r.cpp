#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
 
using namespace std;
 
#define DBG 0
 
#define MAX 100
 
int C;
int N,M;
int garrN[MAX],garrM[MAX];
int gIS[MAX][MAX];
int gcnt,gMaxIndex;
int gcntIS[MAX];
int gchangedIS[MAX];

void printIS()
{
    for(int i=0;i<gcnt;i++){ 
		cout << "==gIS index: " << i << " ,changed:" << gchangedIS[i] << " ,sizegISline: " << gcntIS[i] << " >> ";
		for(int j=0;j<gcntIS[i];j++){ 
			cout << "  " << gIS[i][j];
		}
		cout << endl;
	}
}

void printAnswer(const char *s,int ansIS[MAX][MAX],int& ansSize,int ansSizeIS[])
{
    for(int i=0;i<ansSize;i++){ 
		cout << "=" << s << "=ANSWER index: " << i << " ,sizeIS: " << ansSizeIS[i] << " >> ";
		for(int j=0;j<ansSizeIS[i];j++){ 
			cout << "  " << ansIS[i][j];
		}
		cout << endl;
	}
}

void printInput()
{
    cout << "==== C: " << C << " ,N: "<< N << " ,M:" << M << endl;
    cout << "N(" << N << "): ";
    for(int i=0;i<N;i++){ cout << garrN[i] << " ";  }
	cout << endl;
    cout << "M(" << M << "): ";
    for(int i=0;i<M;i++){ cout << garrM[i] << " ";  }
	cout << endl;
}

void findgIS(int arr[],const int size)
{
	gcnt = 0;
	gMaxIndex = 0;
	for(int i=0;i<MAX;i++){ gcntIS[i] = 0;  gchangedIS[i] = 0;}

	int flagAdded= 0;
	for(int i=0;i<size;i++){
		if(i == 0){ gcnt = 1; gcntIS[0] = 1; gIS[0][0]=arr[i]; }
		for(int idx = gcnt-1 ; idx >= 0 ; idx--){
			if(gIS[idx][idx] < arr[i]){
				if(idx == gcnt-1){		// last longest line then add new line
					for(int t = 0;t<=idx; t++){
						gIS[idx+1][t] = gIS[idx][t];
					}
					gchangedIS[idx] = 0;
					gchangedIS[idx+1] = 1;
					gIS[idx+1][idx+1] = arr[i];
					gcntIS[idx+1] = gcntIS[idx] + 1;
					gcnt++;
					gMaxIndex = idx+1;
					//cout << "last index idx:" << idx;
					//cout << "gcnt:" << gcnt;
					//cout << "gcntIS:" << gcntIS[idx+1];
					//cout << endl;
				} else if(gIS[idx+1][idx+1] > arr[i]){
					for(int t = 0;t<=idx; t++){
						gIS[idx+1][t] = gIS[idx][t];
					}
					gIS[idx+1][idx+1] = arr[i];
					gchangedIS[idx] = 0;
					gchangedIS[idx+1] = 1;
					//cout << "NO last index idx:" << idx;
					//cout << "gcnt:" << gcnt;
					//cout << "gcntIS:" << gcntIS[idx+1];
					//cout << endl;
				}
				break;
			} 
			if( (idx == 0) && (gIS[0][0] > arr[i]) ){
				gIS[0][0] = arr[i];
				gchangedIS[0] = 1;

			}
		}
		//cout << "==input[" << i <<"]: " << arr[i] << " , gcnt:" << gcnt << endl;
		//printIS();
	}

	return ;
}

void copyAns(int ansIS[MAX][MAX],int& ansSize,int ansSizeIS[])
{
	ansSize = 0;
    for(int i=0;i<gcnt;i++){ 
		if(gchangedIS[i] == 1){
			ansSizeIS[ansSize] = gcntIS[i];
			for(int j=0;j<gcntIS[i];j++){ 
				ansIS[ansSize][j] = gIS[i][j];
			}
			ansSize++;
		}
	}
}

//int mergeLIS(

int 
JoinedLIS(
	int ansISN[MAX][MAX],int& ansSizeN,int ansSizeISN[],
	int ansISM[MAX][MAX],int& ansSizeM,int ansSizeISM[])
{
	int Max=0;
    for(int iN=0;iN<ansSizeN;iN++){ 
		for(int iM=0;iM<ansSizeM;iM++){ 
			//cout << "==Joined N to M: N idx " << iN << " ( size " << ansSizeISN[iN] << ") to M idx " << iM << " ( size " << ansSizeISM[iM] << " )" << endl;
			int cnt=0;
			int same=0;
			int n=0;
			int m=0;
			// find same number connt
			while(1){
				if( (n >= ansSizeISN[iN]) || (m >= ansSizeISM[iM]) ){
					break;
				}
				if(ansISN[iN][n] == ansISM[iM][m]){
					same++;
					n++;
				} else if(ansISN[iN][n] > ansISM[iM][m]){
					m++;
				} else {      // (ansISN[iN][n] < ansISM[iM][m])
					n++;
				}
			}
			cnt = ansSizeISN[iN] + ansSizeISM[iM] - same;
			//cout << "same=" << same << ",cnt=" << cnt << endl;
			if(cnt > Max){ Max = cnt; }
		}
	}
	return Max;
}

int main(int argc,char *argv[])
{
 
    scanf("%d", &C);
	for(int c = 0 ; c < C ; c++){
		scanf("%d %d",&N,&M);
		for(int n=0;n<N;n++){
			scanf("%d",&garrN[n]);
		}
		for(int m=0;m<M;m++){
			scanf("%d",&garrM[m]);
		}

		int ansISN[MAX][MAX];
		int ansSizeN;
		int ansSizeISN[MAX];
		findgIS(garrN,N);
		copyAns(ansISN,ansSizeN,ansSizeISN);
		//::printIS();

		int ansISM[MAX][MAX];
		int ansSizeM;
		int ansSizeISM[MAX];
		findgIS(garrM,M);
		copyAns(ansISM,ansSizeM,ansSizeISM);
		//::printIS();
		
		//::printInput();
		//::printAnswer("N",ansISN,ansSizeN,ansSizeISN);
		//::printAnswer("M",ansISM,ansSizeM,ansSizeISM);

		printf("%d\n", JoinedLIS(ansISN,ansSizeN,ansSizeISN, ansISM,ansSizeM,ansSizeISM));
    }
 
     
    vector<int> v;

    return 0;
}
