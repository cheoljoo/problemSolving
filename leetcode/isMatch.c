#include <stdio.h>
#include <stdlib.h>



char tc[40];
int tlen =0;
char ta[40];
int slen=0;
int plen=0;

bool go(char *s,int sIndex,int patternIndex, int logLevel){
    return true;
}

bool isMatch(char * s, char * p){
    slen = strlen(s);
    plen = strlen(p);
    for(int i=0;i<plen;i++){
        if(p[i] == '*'){
            next;
        }
        if( (i+1) == plen){
            tc[tlen] = p[i];
            ta[tlen] = 0;
            tlen++;
        } else {
            if(p[i+1] == '*'){
                tc[tlen] = p[i];
                ta[tlen] = 1;
                tlen++;
            } else {
                tc[tlen] = p[i];
                ta[tlen] = 0;
                tlen++;
            }
        }
    }
    
    return go(s,0,0,0);
}

main()
{
    printf("%b",isMatch("aa","a*"));
    
}