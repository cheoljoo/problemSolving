#include <stdio.h>
#include <stdlib.h>

int main(){
    int C,N,H,W;
    int i;
    scanf("%d",&C);
    for(i=0;i<C;i++){
        scanf("%d",&H);
        scanf("%d",&W);
        scanf("%d",&N);
        printf("%d",(N-1)%H +1);
        printf("%02d\n", (int) ( (N-1) / H)   + 1     );
    }

}
