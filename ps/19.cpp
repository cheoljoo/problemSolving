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
int tableIndex[3][200000];
int order[3][200000];
int ad[3][200000];
vector< pair <int,int> > st[3]; 


int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);

    scanf("%d",&R);
    scanf("%d",&N);
    for(int i=0;i<R;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&table[i][j]);
        }
    }

    int rr;
    int r;
    for(rr=0;rr<R;rr++){
        for(int p=0;p<N;p++){
                st[rr].push_back( make_pair(table[rr][p],p) ); 
        }
        sort(st[rr].begin(), st[rr].end());
        for (int ii=0; ii<st[rr].size(); ii++) {
            tableIndex[rr][st[rr][ii].second] = ii;
        }
    }
#if 0       //??
    for(r=0;r<R;r++){
                printf("table [%3d] ",r);
                for(int p=0;p<N;p++){
                        printf("%3d ", table[r][p]);
                }
                cout << endl;
                /*
                printf("order [%3d] ",r);
                for (int ii=0; ii<N; ii++) 
                {
                        printf("%3d ", order[r][ii]);
                }
                cout << endl;
                */
                printf("taIdx [%3d] ",r);
                for (int ii=0; ii<N; ii++) 
                {
                        printf("%3d ", tableIndex[r][ii]);
                }
                cout << endl;
                for (int ii=0; ii<N; ii++) 
                { 
                    cout << st[r][ii].first << ":" 
                    << st[r][ii].second << " "; 
                } 
                cout << endl;
    }
#endif

    for(int i=N,j=0;i>3;i--,j++){
        vector<int> permu(N);
        for(int kk=0;kk<j;kk++){
            permu[N-1-kk] = 1;          // 0 is selected
        }
        //??cout << "====" << i << endl;
        int sizeVec= i;;
        //std::sort(permu.begin(), permu.end());
        do{
            //cout << "permu size : " << permu.size() << endl;
            //??cout << "---- ";
            /*
            for(auto ii : permu){ 
                cout << ii << " "; 
            }
            for(int ii=0;ii<N;ii++){
                cout << permu[ii] << " ";
            }
            cout << endl;
            */
            for(int r=0;r<R;r++){
#if 0
                cout << "The vector after applying sort is:\n" ; 
                for (int ii=0; ii<N; ii++) 
                { 
                    // "first" and "second" are used to access 
                    // 1st and 2nd element of pair respectively 
                    cout << st[r][ii].first << ":" 
                    << st[r][ii].second << ":" 
                    << permu[ii] << " "; 
                } 
                cout << endl;
#endif

#if 1       // important algorithm
                int o= 0;
                for (int ii=0; ii<N; ii++) 
                {
                    int idx = st[r][ii].second;
                    if(permu[idx] == 0){
                        order[r][idx] = o;
                        o++;
                    } 
                }
#endif 

#if 0
                cout << "table [" << r << "] ";
                for(int p=0;p<N;p++){
                    if(permu[p] == 0){
                        cout << table[r][p] << " "; 
                    } else {
                        cout << "- ";
                    }
                }
                cout << endl;
                cout << "order [" << r << "] ";
                for (int ii=0; ii<vect.size(); ii++) 
                {
                    cout << order[r][ii] << " ";
                }
                cout << endl;
#endif
            }
#if 0       //?? print
            for(r=0;r<R;r++){
                printf("table [%3d] ",r);
                for(int p=0;p<N;p++){
                    if(permu[p] == 0){
                        printf("%3d ", table[r][p]);
                    } else {
                        printf("--- ");
                    }
                }
                cout << endl;
                printf("order [%3d] ",r);
                for (int ii=0; ii<N; ii++) 
                {
                    if(permu[ii] == 0){
                        printf("%3d ", order[r][ii]);
                    } else {
                        printf("--- ");
                    }
                }
                cout << endl;
                printf("taIdx [%3d] ",r);
                for (int ii=0; ii<N; ii++) 
                {
                    if(permu[ii] == 0){
                        printf("%3d ", tableIndex[r][ii]);
                    } else {
                        printf("--- ");
                    }
                }
                cout << endl;
                /*
                for (int ii=0; ii<N; ii++) 
                { 
                    if(permu[ii] == 0){
                        cout << st[r][ii].first << ":" 
                            << st[r][ii].second << " "; 
                    } else {
                        cout << "--:--" ;
                    }
                } 
                cout << endl;
                */
            }
#endif
            int flag = 0;
            for(int ii=0;ii<N;ii++){
                if(permu[ii] == 0){
                    for(int rr=1;rr<R;rr++){
                        if(order[0][ii] != order[rr][ii]){
                            flag = 1;
                            break;
                        }
                    }
                    if(flag != 0){
                        break;
                    }
                }
            }
            if(flag == 0){
                cout << sizeVec << endl;
                return 0;
            }
        }while(next_permutation(permu.begin(), permu.end()));
    }
    
    return 0;
}
