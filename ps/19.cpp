#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
#include <map>
#include <iterator>
#include <unistd.h>
#include <math.h>
#include <string.h>
 
using namespace std;
 
int N,R;
char *SS;
char *DD;
int maxCnt=0;

int table[3][200000];
int ret[200000];
vector< pair <int,int> > st; 


int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);

    int mmx=0;

    scanf("%d",&R);
    scanf("%d",&N);
    for(int i=0;i<R;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&table[i][j]);
        }
    }

    for(int p=0;p<N;p++){
        st.push_back( make_pair(table[0][p],p) ); 
    }
    sort(st.begin(), st.end());

    ret[0] = 1;
    for(int a = 1;a<N; a++){
        int m = 0; 
        int idx1 = st[a].second;
        for(int b=0;b<a;b++){
            int flag = 0;
            int idx2 = st[b].second;
            for(int r=1;r<R;r++){
                if(table[r][idx2] > table[r][idx1]){
                    flag = 1;
                }
            }
            if(flag == 0){  // all value is smaller
                m = max(m,ret[b]);
            }
        }
        ret[a] = m + 1;
        mmx = max(mmx,ret[a]);
    }

    
#if 0
    cout << "table[0] : ";
    for(int i=0;i<N;i++){
        printf("%3d ", st[i].first);
    }
    cout << endl;
    for(int r=1;r<R;r++){
        cout << "table[" << r << "] : ";
        for(int i=0;i<N;i++){
            printf("%3d ", table[r][st[i].second]);
        }
        cout << endl;
    }
    cout << "return   : ";
    for(int i=0;i<N;i++){
        printf("%3d ", ret[i]);
    }
    cout << endl;
#endif

    printf("%d\n",mmx);

    return 0;
}
