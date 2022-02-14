#include <iostream>
#include <string>
#include <cstring>



char tc[40];
int tlen =0;
char ta[40];
int slen=0;
int plen=0;

bool go(char *s,int sIndex,int patternIndex, int loopLevel){
    if( (sIndex == slen) && (patternIndex == tlen)){
        return true;
    } else if(patternIndex == tlen){
        return false;
    } else if(sIndex == slen){
        for(int i=patternIndex;i<tlen;i++){
            if(ta[i] == 0){
                return false;
            }
        }
        return true;
    }

    if(ta[patternIndex] == 1){
        if(tc[patternIndex] == '.'){
            for(int i=slen-sIndex;i>=0;i--){
                if(true == go(s,sIndex+i,patternIndex+1,loopLevel+1)){
                    return true;
                }
            }
            return false;
        }
        else {
            if(tc[patternIndex] == s[sIndex]){
                return go(s,sIndex+1,patternIndex,loopLevel+1) || go(s,sIndex,patternIndex+1,loopLevel+1) || go(s,sIndex+1,patternIndex+1,loopLevel+1) ;
            } else {
                return go(s,sIndex,patternIndex+1,loopLevel+1);
            }
        }
    } else {
        if(tc[patternIndex] == '.'){
            return go(s,sIndex+1,patternIndex+1,loopLevel+1);
        } else if(tc[patternIndex] == s[sIndex]){
            return go(s,sIndex+1,patternIndex+1,loopLevel+1);
        } else {
            return false;
        }
    }

    return true;
}

bool isMatch(char * s, char * p){
    slen = strlen(s);
    plen = strlen(p);
    for(int i=0;i<plen;i++){
        if(p[i] == '*'){
            continue;
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

void run(bool e,char *s , char *p)
{
    for(int i=0;i<40;i++){
        tc[i] = 0;
        ta[i]=0;
    }
    tlen = 0;
    slen = 0;
    plen = 0;

    if(e == isMatch(s,p)){
        printf("success -> %s %s\n",s,p);
    } else {
        printf("error -> %s %s\n",s,p);
    }

}

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {

    }
};

int main()
{

    run(true,"aa","a*");
    run(false,"abbccc", ".*c.*b.*c");
    run(false,"acbbcbcbcbaaacaac", "ac*.a*ac*.*ab*b*ac");
    run(true,"bbcacbabbcbaaccabc", "b*a*a*.c*bb*b*.*.*");

    run(true,"mississipppu","mis*is*ip*.u");
    run(true,"mississippi","mis*is*ip*.");

    run(false,"abcccccc","abb*bc*");
    run(true,"abbcccccc","abb*bc*");
    run(true,"abc", "ab*bc*" );

    run(false,"aa","ab*");
    run(true,"a","ab*");
    run(false,"atbtd","a.bc*d");
    run(true,"aaabbb","aa*b*c*b");

    return 0;
}
