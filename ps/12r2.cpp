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
 
#define NMAX 10001
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
calculateWeight(int w)  // weight
{
    cout << "{ ";
    if(jewel[w].value == 0){
        cout << "x" ;
    } else if(jewel[w].left == 0){
        cout << "l" << w ;
        jewel[w].count ++;
    } else {
        cout << w << ":" << jewel[w].left << "+" << jewel[w].right;
        calculateWeight(jewel[w].left);
        calculateWeight(jewel[w].right);
    }
    cout << " }";
}

int
getMaxValue(int weight)
{
    // DFS
    vector<tuple<int,int,int>> stack;
    tuple<int,int,int> t;

    t = make_tuple(weight, weight-1, 1);
    stack.push_back(t);
    //cout << "push w:" <<  weight << " l:" << weight-1 << " r:" << 1 << endl;

    int maxValue = 0;
    int w,l,r;
    //int stackSize = 0;
    while(!stack.empty()){
        //if(stackSize < stack.size()){ stackSize = stack.size(); }
        t = stack.back();
        w  =  get<0>(t);
        l  =  get<1>(t);
        r  =  get<2>(t);
        //cout << "w:" << w << " ,l:" << l << " ,r:" << r ;
        //cout << ",val:" << jewel[w].value << " ,lval:" << jewel[l].value << " ,rval:" << jewel[r].value ;
        //cout << ",cal:" << jewel[w].calculated << " ,lcal:" << jewel[l].calculated << " ,rcal:" << jewel[r].calculated ;
        //cout << endl;
        if(jewel[l].calculated && jewel[r].calculated){
            int val = jewel[l].value + jewel[r].value;
            if(val > jewel[w].value){
                jewel[w].value = val;
                jewel[w].left = l;
                jewel[w].right = r;
            }
            stack.pop_back();
            //cout << "pop[c] w:" <<  w << " l:" << l << " r:" << r << endl;

            if(r == int(w/2)){
                jewel[w].calculated = 1;
            } else {
                t = make_tuple(w, l-1, r+1);
                stack.push_back(t);
                //cout << "push[c] w:" <<  w << " l:" << l-1 << " r:" << r+1 << endl;
            }
        } else {
            if( !jewel[l].calculated ){
                t = make_tuple(l, l-1, 1);
                stack.push_back(t);
                //cout << "push w:" <<  l << " l:" << l-1 << " r:" << 1 << endl;
            }
            if( !jewel[r].calculated ){
                t = make_tuple(r, r-1, 1);
                stack.push_back(t);
                //cout << "push w:" <<  r << " l:" << r-1 << " r:" << 1 << endl;
            }
        }
    };

    //cout << "stackSize:" << stackSize << endl;
    return jewel[weight].value;
}

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    
    scanf("%d %d", &N,&V);

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

    int maxValue = getMaxValue(V);
    cout << maxValue << endl;

/*
    calculateWeight(V); cout << endl;

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
*/

    return 0;
}
