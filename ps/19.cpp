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
 
std::vector<long> input;

int N,R;
char *SS;
char *DD;
int maxCnt=0;

int table[3][200000];
int order[3][200000];


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

    for(int i=N,j=0;i>2;i--,j++){
        //??cout << "====" << i << endl;
        vector<int> permu(N);
        for(int kk=0;kk<j;kk++){
            permu[N-1-kk] = 1;          // 0 is selected
        }
        //std::sort(permu.begin(), permu.end());
        do{
            //cout << "permu size : " << permu.size() << endl;
            //??cout << "---- ";
            //??for(auto ii : permu){ cout << ii << " "; }
            /*
            for(int ii=0;ii< permu.size();ii++){
                cout << permu[ii] << " ";
            }
            */
            //??cout << endl;
            int sizeVec=0;
            for(int r=0;r<R;r++){
                vector< pair <int,int> > vect; 
                //cout << "--vector size 1: " << vect.size() << endl;
                for(int p=0,o=0;p<N;p++){
                    if(permu[p] == 0){
                        vect.push_back( make_pair(table[r][p],o) ); 
                        o++;
                    }
                }
                //cout << "--vector size 2: " << vect.size() << endl;
                sort(vect.begin(), vect.end());
#if 0
                cout << "The vector after applying sort is:\n" ; 
                for (int ii=0; ii<vect.size(); ii++) 
                { 
                    // "first" and "second" are used to access 
                    // 1st and 2nd element of pair respectively 
                    cout << vect[ii].first << ":" 
                    << vect[ii].second << " "; 
                } 
                cout << endl;
#endif
                for (int ii=0; ii<vect.size(); ii++) 
                {
                    order[r][vect[ii].second] = ii+1;
                }
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
                sizeVec = vect.size();
                //cout << "--vector size 3: " << vect.size() << endl;
                vect.clear();
                //cout << "--vector size 4: " << vect.size() << endl;
            }
            int flag = 0;
            //??cout << "sizeVec : " << sizeVec << endl;
            for(int ii=0;ii<sizeVec;ii++){
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
            if(flag == 0){
                cout << sizeVec << endl;
                return 0;
            }
        }while(next_permutation(permu.begin(), permu.end()));
    }
    
    return 0;
}
