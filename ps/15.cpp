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
 
using namespace std;
 
std::vector<long> input;

#define ADD 0
#define SUB 1
#define MUL 2
#define DIV 3

int cal(int a , int b , int oper)
{
    switch(oper){
        case DIV:
            {
                if( (a % b) != 0 ){
                    return -1;
                }
                return a / b;
            }
            break;
        case ADD:
            return a+b;
        case SUB:
            return a-b;
        case MUL:
            return a*b;
        default:
            return -1;
    }
    return -1;
}

void print_cal(int a , int b , int c , int loc, int oper)
{
    if(loc == 0){
        switch(oper){
        case DIV:
            printf("%d=%d/%d\n",a,b,c);
            break;
        case ADD:
            printf("%d=%d+%d\n",a,b,c);
            break;
        case SUB:
            printf("%d=%d-%d\n",a,b,c);
            break;
        case MUL:
            printf("%d=%d*%d\n",a,b,c);
            break;
        }
    } else if(loc == 2){
        switch(oper){
        case DIV:
            printf("%d/%d=%d\n",a,b,c);
            break;
        case ADD:
            printf("%d+%d=%d\n",a,b,c);
            break;
        case SUB:
            printf("%d-%d=%d\n",a,b,c);
            break;
        case MUL:
            printf("%d*%d=%d\n",a,b,c);
            break;
        }
    }
}

int set_cal(int a,int b , int c, int loc)
{
    if(loc == 0){
        for(int oper=0;oper<4;oper++){
            if(a == cal(b,c,oper)){
                print_cal(a,b,c,loc,oper);
                return 1;
            }
        }
    } else if(loc == 2){
        for(int oper=0;oper<4;oper++){
            if(cal(a,b,oper) == c){
                print_cal(a,b,c,loc,oper);
                return 1;
            }
        }
    }
    return 0;
}

int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);
    
    int temp;
	for(int i = 0 ; i < 3 ; i++){
        scanf("%d",&temp);
        input.push_back(temp);
    }

//;; for(int i=0;i<input.size();i++){ cout << input[i] << " "; } cout << endl;

    if(set_cal(input[0],input[1],input[2],0)){ return 0; }
    if(set_cal(input[0],input[1],input[2],2)){ return 0; }

    return 0;
}
