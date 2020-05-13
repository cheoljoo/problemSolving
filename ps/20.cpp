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
 
int n,X,y,Z,T;
int value[100000];


int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);

    int mx=0;

    scanf("%d",&T); 
    for(int i=0;i<T;i++){
        scanf("%d %d %d %d",&n,&X,&y,&Z);
        ;;//printf("\n\nn%d X%d y%d Z%d\n",n,X,y,Z);
        for(int j=0;j<n;j++){
            scanf("%d",&value[j]);
        }
        ;;//for(int j=0;j<n;j++){
            ;;//printf("%d ",value[j]);
        ;;//}
        ;;//printf("\n");
        if(y == 0){
            mx = n;
        } else {
            mx = (int) (X / y);
        }
        if(mx > n){ mx = n; }
        int mxi;
        double dSum;
        dSum = 0;
        double initSum;
        ;;//printf("mx:%d , dSum=%f , iSum=%f\n",mx,dSum,initSum);
        for(mxi=1;mxi <= mx;mxi++){ 
            initSum=0;
            for(int s=0;s<mxi;s++){
                initSum += (double)value[s];
            }
            double oSum = (double) y * (double) mxi;
            ;;//printf("mxi:%d , iSum=%f , oSum=%f\n",mxi,initSum,oSum);
            double dSum = 0;
            int x=0;
            int correctIndex=-1;
            for(x=0;x< n-mxi+1;x++){
                if(0 == x){
                    dSum = initSum;
                } else {
                    dSum -= (double) value[x-1];
                    dSum += (double) value[x+mxi-1];
                }
                ;;//printf("x:%d , dSum=%f , x+mxi-1=%d\n",x,dSum,x+mxi-1);
                if( (dSum - oSum) >= (double)Z){
                    correctIndex = x+1;
                }
            }
            if(correctIndex != -1){ 
                printf("%d %d\n",correctIndex,correctIndex + mxi -1);
                break; 
            }
        }
        if(mxi > mx){
            printf("-1\n");
        }
    }

    return 0;
}
