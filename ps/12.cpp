#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
#include <map>
#include <iterator>
#include <unistd.h>
 
using namespace std;
 
#define NMAX 1001
int N,V;    // jewel number , value
struct Jewel {      // index : weight
    int value;
    int left;
    int right;
    int calculated;
    int count;      // for result in printWeight
};
struct Jewel jewel[NMAX]; // jewel[weight]  weight start from 1.

int minJewelWeight = NMAX;

void
printWeight(int w)  // weight
{
    cout << "{ ";
    if(jewel[w].value == 0){
        cout << "x" ;
    } else if(jewel[w].left == 0){
        cout << "l" << w ;
        jewel[w].count ++;
    } else {
        cout << w << ":" << jewel[w].left << "+" << jewel[w].right;
        printWeight(jewel[w].left);
        printWeight(jewel[w].right);
    }
    cout << " }";
}

void 
printCalculated(const char *s)
{
    cout << "=== " << s << " ===" << endl;
    cout << "minJewelWeight:" << minJewelWeight << endl;
    for(int i=0;i<NMAX;i++){
        if(jewel[i].calculated != 0){
            cout << "weight " << i << " > value:" << jewel[i].value ;
            cout << " , left:" << jewel[i].left ;
            cout << " , right:" << jewel[i].right ;
            cout << " , calculated:" << jewel[i].calculated ;
            cout << endl;
        }
    }
}

void 
printJewel(const char *s)
{
    cout << "=== " << s << " ===" << endl;
    for(int i=1;i<NMAX;i++){
        if(jewel[i].value != 0){
            cout << "weight " << i << " > value:" << jewel[i].value ;
            cout << " , left:" << jewel[i].left ;
            cout << " , right:" << jewel[i].right ;
            cout << " , calculated:" << jewel[i].calculated ;
            cout << endl;
        }
    }
}

int
getMaxValue(int weight)
{
    if(jewel[weight].calculated != 0){      // calculated 
            cout << "\treturn weight " << weight << " > value:" << jewel[weight].value ;
            cout << " , left:" << jewel[weight].left ;
            cout << " , right:" << jewel[weight].right ;
            cout << " , calculated:" << jewel[weight].calculated ;
            cout << endl;
        return jewel[weight].value; 
    }

    for(int i = 1 ; i <= int(weight/2) ; i++){
        cout << "1]" << weight << " left:" << i << " ,right:" << weight-i << endl;
        int val = getMaxValue(i) + getMaxValue(weight -i);
        cout << "2]" << weight << " left:" << i << " ,right:" << weight-i << endl;
        cout << "val:" << val << " ,old val:" << jewel[weight].value << endl;;
        if(val > jewel[weight].value){
            jewel[weight].value = val;
            jewel[weight].left = i;
            jewel[weight].right = weight-i;
            cout << "\tfor weight " << weight << " > value:" << jewel[weight].value ;
            cout << " , left:" << jewel[weight].left ;
            cout << " , right:" << jewel[weight].right ;
            cout << " , calculated:" << jewel[weight].calculated ;
            cout << endl;
        }
    }
    jewel[weight].calculated = 1;
    printJewel("getMaxValue");
    return jewel[weight].value;
}

int main(int argc,char *argv[])
{
    std::vector<int> vec;

	ios_base::sync_with_stdio(false);
    
    scanf("%d %d", &N,&V);

    printJewel("input start");

	for(int i = 0 ; i < N ; i++){
        int jw,jv;  // weight , value
        scanf("%d %d", &jw,&jv);
        if(jw < minJewelWeight){ minJewelWeight = jw; }
        if(jv > jewel[jw].value){ jewel[jw].value = jv; }
        jewel[jw].left = 0;
        jewel[jw].right = jw;
    }

    for(int i=0; i < minJewelWeight ; i++){
        jewel[i].value = 0;
        jewel[i].left = 0;
        jewel[i].right = i;
        jewel[i].calculated = 1;
    }

    printCalculated("input start2");

    printJewel("input end");

    int maxValue = getMaxValue(V);
    cout << maxValue << endl;

    printWeight(V);
    cout << endl;

    int sum = 0;
    cout << "jewels list: ";
    for(int i=1;i<NMAX;i++){
        if(jewel[i].count > 0){
            cout << i << "*" << jewel[i].count << " + ";;
            sum += jewel[i].count;
        }
    }
    cout << endl;
    cout << "jewels total count : " << sum << endl;
    cout << "jewels max value : " << maxValue << endl;

    return 0;
}
