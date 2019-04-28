#include <stdio.h>
 
int C;    // case size
int N;    // matrix size
int M;      // problem size

int m[1001][1001];

int main(int argc,char *argv[])
{
    scanf("%d", &C);
	for(int cnt = 0 ; cnt < C ; cnt++){
        scanf("%d %d", &N,&M);
        for(int r =1;r<=N;r++){
            for(int c =1;c<=N;c++){
                int value;
                scanf("%d",&value);
                m[r][c] = value;
            }
        }
        //print_m();
        int rfrom,cfrom,rto,cto,v;
        for(int mm =1;mm<=M;mm++){
            scanf("%d %d %d %d %d",&rfrom,&cfrom,&rto,&cto,&v);
            for(int rr=rfrom;rr<=rto;rr++){
                for(int cc=cfrom;cc<=cto;cc++){
                    m[rr][cc] += v;
                }
            }
            //printf("operation : %d %d ~ %d %d : v %d\n",rfrom,cfrom,rto,cto,v);
            //print_m();
        }
        for(int r =1;r<=N;r++){
            int sum=0;
            for(int c =1;c<=N;c++){
                sum += m[r][c];
            }
            printf("%d " , sum);
        }
        printf("\n");
        for(int c =1;c<=N;c++){
            int sum=0;
            for(int r =1;r<=N;r++){
                sum += m[r][c];
            }
            printf("%d " , sum);
        }
        printf("\n");

    }

    return 0;
}
