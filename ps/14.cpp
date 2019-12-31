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
 
int N;
int total = 0;
std::vector<long> chu;
std::vector<int> exist;

void Calculate(int chosen , int index,long sum)
{
    //;;cout << "cal - " ;
    //;;cout << "chosen:" << chosen;
    //;;cout << ",index:" << index;
    //;;cout << ",sum:" << sum;
    //;;cout << ",abs(sum):" << abs(sum);
    //;;cout << endl;
    if(index >= N){  
        exist[abs(sum)] = 1;
        //;;cout << "return exist : " << abs(sum) << endl;
        return ; 
    }
    sum += (long) chosen * chu[index];
	for(int choose = -1 ; choose < 2 ; choose++){
        Calculate(choose,index+1,sum);    
    }
}

int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);
    
    scanf("%d", &N);

    int temp;
	for(int i = 0 ; i < N ; i++){
        scanf("%d",&temp);
        chu.push_back(temp);
        total += temp;
    }
    for(int i=0; i <= total ; i++){
        exist.push_back(0);
    }

//;; for(int i=0;i<chu.size();i++){ cout << chu[i] << " "; } cout << endl;
//;; cout << "N:" << N << endl;

	for(int choose = -1 ; choose < 2 ; choose++){
        Calculate(choose,0,0L);    
    }

    int cnt = 0;
    for(int i=1; i <= total ; i++){
        if(exist[i] == 0){
            cnt ++;
        }
    }

    printf("%d\n",cnt);

    return 0;
}
