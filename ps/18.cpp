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

int N,M,D;
char *SS;
char *DD;
int maxCnt=0;

map<string,int> country;
map<int,string> countryName;
int vs[6][2];   // A vs B 
float WEL[6][3];   // A_Win A_Equal A_Lose
float resultProportion[4];  // each country's proportion

int gCnt = 1;

void setValue(char *s,int rmax,int cmax,int row,int col,char tt)
{
    s[row*cmax + col] = tt;
}

void PRINT(char *s)
{
    int rmax = N;
    int cmax = M;
	for(int i = 0 ; i < rmax ; i++){
	    for(int j = 0 ; j < cmax ; j++){
            printf("%d",(int) s[i*cmax + j]);
        }
        printf("\n");
    }
    
    return ;
}

int cal1(int r , int idx , int& dist,int& row,int& col)
{
    for(int dd=0;dd<D;dd++){
        for(int jj=dd;jj>0;jj--){
            int lrow = r+dd-jj;
            if(lrow >= N){ lrow = N-1; }
            int lcol = idx -jj;
            if(lcol < 0){ lcol = 0; }
            if(lcol >= M){ lcol = M-1; }
            if(DD[lrow*M+lcol] == 1){
                row = lrow;
                col = lcol;
                dist = dd;
                return 1;
            }
        }
        for(int jj=0;jj<=dd;jj++){
            int lrow = r+dd-jj;
            if(lrow >= N){ lrow = N-1; }
            int lcol = idx +jj;
            if(lcol < 0){ lcol = 0; }
            if(lcol >= M){ lcol = M-1; }
            if(DD[lrow*M+lcol] == 1){
                row = lrow;
                col = lcol;
                dist = dd;
                return 1;
            }
        }
    }
    return 0;
}

void cal(int a , int b , int c)
{
    int flaga = 0;
    int flagb = 0;
    int flagc = 0;
    for(int i=0;i<N;i++){
        int ra=-1,ca=-1,dista=-1;
        flaga = cal1(i,a-1,dista,ra,ca);
        int rb=-1,cb=-1,distb=-1;
        flagb = cal1(i,b-1,distb,rb,cb);
        int rc=-1,cc=-1,distc=-1;
        flagc = cal1(i,c-1,distc,rc,cc);
        //;;if(flaga + flagb + flagc) printf("line=%d",i);
        if(flaga){ 
            //;;if(flaga) printf(",ra=%d,ca=%d,dista=%d",ra,ca,dista);
            setValue(DD,N,M,ra,ca,(char) 0);
        }
        if(flagb){
            //;;if(flagb) printf(",rb=%d,cb=%d,distb=%d",rb,cb,distb);
            setValue(DD,N,M,rb,cb,(char) 0);
        }
        if(flagc){
            //;;if(flagc) printf(",rc=%d,cc=%d,distc=%d",rc,cc,distc);
            setValue(DD,N,M,rc,cc,(char) 0);
        }
        if(flaga + flagb + flagc){ 
            //;;printf("\n");
            //;;PRINT(DD);
        }
    }
    return ;
}

void combination(int start , int cnt , int a , int b , int c)
{
    if(cnt == 0){
        //;;printf("[%3d] N:%d,M:%d,a:%2d,b:%2d,c:%2d\n",gCnt++,N,M,a-1,b-1,c-1);
        memcpy(DD,SS,N*M);
        cal(a,b,c);
        int cc=0;
        for(int i=0;i< N*M;i++){
            if(SS[i] != DD[i]){
                //;;printf("%d\n",i);
                cc++;
            }
        }
        if(maxCnt < cc){ maxCnt = cc; }
        //;;PRINT(SS);
        //;;printf("combination : cc=%d , maxCnt=%d\n",cc,maxCnt);
        //;;PRINT(DD);
        return ;
    }
    if(start > M){
        return ;
    }

    combination(start+1 , cnt,a,b,c);    // not include start #

    if(a == 0){
        a = start;
    } else if(b == 0){
        b = start;
    } else if(c == 0){
        c = start;
    } else {
        printf("error : %d %d %d\n",a,b,c);
        return ;
    }
    combination(start+1 , cnt-1,a,b,c);    // include start #

    return ;
}

int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);
    
    scanf("%d",&N);
    scanf("%d",&M);
    scanf("%d",&D);

    int tt;
    SS = (char *) malloc(N*M);
    DD = (char *) malloc(N*M);
	for(int i = 0 ; i < N ; i++){
	    for(int j = 0 ; j < M ; j++){
            scanf("%d",&tt);
            setValue(SS,N,M,N-1-i,j,(char) tt);
        }
    }
    //;;PRINT(SS);

    combination(1,3,0,0,0);

    printf("%d\n",maxCnt);

    free(SS);
    free(DD);

    return 0;
}
