#include <stdio.h>
 
#define PRIME  ((long long int)1000000007)
int C;    // case size
int N;    // matrix size
int M;      // problem size

int p[201];  // person's number
long long int m[201][201];
long long int sum[201];    // each level 1 ~ p[i]

long long int sumLevel(int level , int from , int end)
{
    long long int localsum = 0;
    for(int i=from;i<=end;i++){
        localsum += m[level][i];
    }

    //return localsum % PRIME;
    return localsum ;
}

int main(int argc,char *argv[])
{
    scanf("%d", &C);
    for(int cnt = 0 ; cnt < C ; cnt++){
        scanf("%d", &N);
        for(int r=N;r>=1;r--){
            int value;
            scanf("%d",&value);
            p[r] = value;
        }
        //printf("N: %d, person number : ",N);
        //for(int r=1;r<=N;r++){
            //printf("%d ",p[r]);
        //} printf("\n");


        for(int l=1;l<=N;l++){
            sum[l] = 0;
            for(int i=1;i<=p[l];i++){
                //printf("l %d ,i %d , p[l-1] %d\n", l,i,p[l-1]);
                //m[l][i] = (l == 1)? 1 : (sumLevel(l-1,i,p[l-1]) % PRIME);
                m[l][i] = (l == 1)? 1 : (sumLevel(l-1,i,p[l-1]) );
                //printf("m[l][i] : %lld\n", m[l][i]);
                sum[l] += m[l][i];
                sum[l] %= PRIME;
                //printf("sum[l] : %lld\n", sum[l]);
            }
        }
        printf("%lld\n", sum[N]);     // count of combination
        printf("%lld\n", sum[N] * N);     // count of combination
        printf("%lld\n", (sum[N] * N ) % PRIME);
    }

    return 0;
}
