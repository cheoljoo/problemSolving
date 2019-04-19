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
};
struct Jewel jewel[NMAX]; // jewel[weight]  weight start from 1.

int minJewelWeight = NMAX;

void
printWeight(int w)  // weight
{
    cout << "{ ";
    if(jewel[w].left == 0){
        cout << "l" << w ;
    } else {
        cout << w << ":" << jewel[w].left << "+" << jewel[w].right;
        printWeight(jewel[w].left);
        printWeight(jewel[w].right);
    }
    cout << " }";
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
            cout << endl;
        }
    }
}

int
getMaxValue(int weight)
{
    if(weight < minJewelWeight){ 
            cout << "\treturn minweight " << weight << " > value:" << jewel[weight].value ;
            cout << " , left:" << jewel[weight].left ;
            cout << " , right:" << jewel[weight].right ;
            cout << endl;
        return 0; 
    }
    if(jewel[weight].value > 0){ 
            cout << "\treturn weight " << weight << " > value:" << jewel[weight].value ;
            cout << " , left:" << jewel[weight].left ;
            cout << " , right:" << jewel[weight].right ;
            cout << endl;
        return jewel[weight].value; 
    }

    for(int i = minJewelWeight ; i <= int(weight/2) ; i++){
        cout << weight << " left:" << i << " ,right:" << weight-i << endl;
        int val = getMaxValue(i) + getMaxValue(weight -i);
        cout << "val:" << val << " ,old val:" << jewel[weight].value << endl;;
        if(val > jewel[weight].value){
            jewel[weight].value = val;
            jewel[weight].left = i;
            jewel[weight].right = weight-i;
            printJewel("getMaxValue");
        }
    }
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
        jewel[jw].value = jv;
        jewel[jw].left = 0;
        jewel[jw].right = jw;
    }

    printJewel("input end");

    int maxValue = getMaxValue(V);
    cout << maxValue << endl;

    printWeight(V);
    cout << endl;

    return 0;
}
