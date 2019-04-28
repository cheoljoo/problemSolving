#include <stdio.h>
 
int N;    // matrix size
int R,C,sr,sc;

#define MAX 104
char b[MAX][MAX];  // board
char path[MAX*MAX];
int pathCounter=0;
int isEnd = 0;
int fillCounter=0;

void print_map()
{
    printf("   ");
    for(int i=0;i<=C+1;i++){
        printf("%d ",i%10);
    }
    printf("\n");
    for(int r=0;r<= R+1;r++){
        printf("%-3d",r);
        for(int c=0;c<=C+1;c++){
            printf("%d ",b[r][c]);
        }
        printf("\n");
    }
    // print path
    printf("pathCounter:%d\n",pathCounter);
    for(int i=0;i<pathCounter;i++){
        printf("%c",path[i]);
    }
    printf("\n");
}

void go(char sr,char sc,int SIZE)
{
    if(isEnd == 1){ return ; }

    b[sr][sc] = 1;
    fillCounter ++;

    printf("sr:%d sc:%d\n",sr,sc);
    print_map();

    if(fillCounter == SIZE){
        isEnd = 1;

        // print path
        for(int i=0;i<pathCounter;i++){
            printf("%c",path[i]);
        }
        printf("\n");
    }

    if(b[sr-1][sc] == 0){   // north
        path[pathCounter++] = 'U';
        go(sr-1,sc,SIZE); 
        pathCounter--;
    }    
    if(b[sr][sc+1] == 0){   // east
        path[pathCounter++] = 'R';
        go(sr,sc+1,SIZE); 
        pathCounter--;
    }    
    if(b[sr][sc-1] == 0){   // west
        path[pathCounter++] = 'L';
        go(sr,sc-1,SIZE); 
        pathCounter--;
    }    
    if(b[sr+1][sc] == 0){   // south
        path[pathCounter++] = 'D';
        go(sr+1,sc,SIZE); 
        pathCounter--;
    }    

    b[sr][sc] = 0;
    fillCounter --;
}

int main(int argc,char *argv[])
{
    scanf("%d", &N);
    for(int i=0;i<MAX;i++){
        b[0][i] = 1;
        b[i][0] = 1;
    }
    for(int cnt = 0 ; cnt < N ; cnt++){
        scanf("%d %d %d %d", &R,&C,&sr,&sc);
        printf("R%d C%d c%d r%d\n",R,C,sr,sc);

        // init
        for(int r = 1;r<=R;r++){
            for(int c = 1;c<=C;c++){
                b[r][c] = 0;
            }
        }
        for(int i=0;i<MAX;i++){
            b[R+1][i] = 1;
            b[i][C+1] = 1;
        }

        pathCounter=0;
        fillCounter=0;
        isEnd = 0;
        go(sr,sc,R*C);
        if(isEnd == 0){
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;
}
