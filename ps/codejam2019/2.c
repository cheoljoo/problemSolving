#include <stdio.h>


#define MAX 1001
 
int C;    // case size
int N;    // matrix size
int M;      // problem size

//int m[1001][1001];
int sumc[MAX];
int sumr[MAX];

void print_sum(){
    printf("=====sum====\n");
        for(int r =1;r<=N;r++){
            printf("%d " , sumr[r]);
        }
        printf("\n");
        for(int c =1;c<=N;c++){
            printf("%d " , sumc[c]);
        }
        printf("\n");
}

int main(int argc,char *argv[])
{
    scanf("%d", &C);
	for(int cnt = 0 ; cnt < C ; cnt++){
        scanf("%d %d", &N,&M);

        for(int i =1;i<=N;i++){
            sumr[i] = 0;
            sumc[i] = 0;
        }
        for(int r =1;r<=N;r++){
            for(int c =1;c<=N;c++){
                int value;
                scanf("%d",&value);
                sumr[r] += value;
                sumc[c] += value;
            }
        }
        //print_sum();
        int rfrom,cfrom,rto,cto,v;
        for(int mm =1;mm<=M;mm++){
            scanf("%d %d %d %d %d",&rfrom,&cfrom,&rto,&cto,&v);
            for(int rr=rfrom;rr<=rto;rr++){
                sumr[rr] += (v * (cto - cfrom +1));
            }
            for(int cc=cfrom;cc<=cto;cc++){
                sumc[cc] += (v * (rto - rfrom +1));
            }
            //printf("operation : %d %d ~ %d %d : v %d\n",rfrom,cfrom,rto,cto,v);
            //print_sum();
        }
        for(int r =1;r<=N;r++){
            printf("%d " , sumr[r]);
        }
        printf("\n");
        for(int c =1;c<=N;c++){
            printf("%d " , sumc[c]);
        }
        printf("\n");

    }

    return 0;
}
