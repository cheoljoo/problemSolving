#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <iterator>
#include <unistd.h>
#include <math.h>
#include <string.h>
 
using namespace std;
 
#define MAX1 2504
#define MAX2 26
char inS[MAX1];
char ins[4][MAX2];
int insLen[4];
int offset[4][MAX1];
int size[4];
int sum=0;
int remain[4];

int sortCal(int *off,int size)
{
    int b = 0;
    char *offFlag = (char *) &b;
    int bOffset[5];
    int bLen[5];
    int retvs = 0;

#if 0
    printf("off size %d : ",size);
    for(int i=0;i<size;i++){
        printf("[%d] %d {%d} ",i,off[i],insLen[i]);
    }
    printf("\n");
#endif

    // sort
    for(int i=0;i<size;i++){
        int minoff=MAX1;
        int minidx=0;
        for(int j=0;j<size;j++){
            //printf("i%d , j%d , offFlag %d , minoff %d , off %d\n",i,j,offFlag[j],minoff,off[j]);
            if( (offFlag[j] == 0) && (off[j] < minoff) ){
                minoff = off[j];
                minidx = j;
            }
        }
        //printf("minidx : %d , i%d\n",minidx,i);
        offFlag[minidx] = 1;
        bOffset[i] = off[minidx];
        bLen[i] = insLen[minidx];
    }

#if 0
    printf("bOffset size %d : ",size);
    for(int i=0;i<size;i++){
        printf("[%d] %d {%d} ",i,bOffset[i],bLen[i]);
    }
    printf("\n");
#endif


    // method 1  : ---++--++--++++++++++++---
    // method 2 : calculate , but it 's hard to cal...
    for(int i=1;i<size;i++){
        if( (bOffset[i-1] <= bOffset[i]) 
         && (bOffset[i] < bOffset[i-1] + bLen[i-1]) ){
            if( (bOffset[i] + bLen[i]) > (bOffset[i-1] + bLen[i-1]) ){
                bLen[i] = bOffset[i] + bLen[i] - bOffset[i-1];
                bOffset[i] = bOffset[i-1];
                bLen[i-1]=0;
            } else {
                bLen[i] = bLen[i-1];
                bOffset[i] = bOffset[i-1];
                bLen[i-1]=0;
            }
        }
    }
    for(int i=0;i<size;i++){
        retvs += bLen[i];
    }

#if 0
    printf("retvs %d, bOffset size %d : ",retvs,size);
    for(int i=0;i<size;i++){
        printf("[%d] %d {%d} ",i,bOffset[i],bLen[i]);
    }
    printf("\n");
#endif
    
    return retvs;
}

int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);

    char *result;
    int loffset[4];

    scanf("%s",inS); 
    scanf("%s",ins[0]); 
    scanf("%s",ins[1]); 
    scanf("%s",ins[2]); 
    scanf("%s",ins[3]); 

#if 0
    printf("%s\n",inS);
    printf("%s\n",ins[0]);
    printf("%s\n",ins[1]);
    printf("%s\n",ins[2]);
    printf("%s\n",ins[3]);
#endif

    for(int i=0;i<4;i++){
        int sz=0;
        insLen[i] = strlen(ins[i]);
        sum += insLen[i];
        result = inS;
        while ((result = std::strstr(result, ins[i])) != NULL) {
            offset[i][sz] = result - inS;
            ++sz;
            ++result;
        }    
        size[i] = sz;
    }

#if 0
    for(int i=0;i<4;i++){
        printf("[%d:len%d] ",i,insLen[i]);
        for(int j=0;j<size[i];j++){
            printf("%d ",offset[i][j]);
        }
        printf("\n");
    }
#endif

#if 1
    { 
#if 0
        for(int i=0;i<4;i++){
            printf("[%d] %d ",i,size[i]);
        }
        printf("\n");
#endif

        // sort
        for(int i=0;i<4;i++){
            int minsize=MAX1;
            int minidx=0;
            for(int j=i;j<4;j++){
                if(size[j] < minsize){
                    minsize = size[j];
                    minidx = j;
                }
            }
            //printf("minsize %d , minidx : %d , i %d\n",minsize,minidx,i);
            if(i != minidx){
                int temp;
                for(int j=0;j<size[i];j++){
                    temp = offset[i][j];
                    offset[i][j] = offset[minidx][j];
                    offset[minidx][j] = temp;
                }
                temp = insLen[i];
                insLen[i] = insLen[minidx];
                insLen[minidx] = temp;
                temp = size[i];
                size[i] = size[minidx];
                size[minidx] = temp;
            }
        }
    }
#endif

    remain[0] = sum - insLen[0];
    remain[1] = remain[0] - insLen[1];
    remain[2] = remain[1] - insLen[2];
    remain[3] = remain[2] - insLen[3];

#if 0
    for(int i=0;i<4;i++){
        printf("[%d:len%d] ",i,insLen[i]);
        for(int j=0;j<size[i];j++){
            printf("%d ",offset[i][j]);
        }
        printf("\n");
    }
#endif


    int mi=MAX1;
    int mx=0;
    int vs;
    for(int idx0=0;idx0<size[0];idx0++){
        loffset[0] = offset[0][idx0];
        for(int idx1=0;idx1<size[1];idx1++){
            loffset[1] = offset[1][idx1];
            vs = sortCal(loffset,2);
            if( (vs >= mi) && ((vs + remain[1]) <= mx) ){ 
                //printf("skip : vs %d , mi %d , vs+remain[1] %d , mx %d\n",vs,mi,vs+remain[1],mx);
                break;
            }
            for(int idx2=0;idx2<size[2];idx2++){
                loffset[2] = offset[2][idx2];
                vs = sortCal(loffset,3);
                if( (vs >= mi) && ((vs + remain[2]) <= mx) ){ 
                    //printf("skip : vs %d , mi %d , vs+remain[2] %d , mx %d\n",vs,mi,vs+remain[2],mx);
                    break;
                }
                for(int idx3=0;idx3<size[3];idx3++){
                    loffset[3] = offset[3][idx3];
                    vs = sortCal(loffset,4);
                    if(vs < mi){mi = vs; }
                    if(vs > mx){mx = vs; }
                }
            }
        }
    }
    
    printf("%d %d\n",mi,mx);

    return 0;
}
