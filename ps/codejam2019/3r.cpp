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
 
int C;    // case size
int A;    // A size
int B;      // B size

vector<int> a;
vector<int> b;

int startIndex;

unsigned int find_near(int e)
{
    unsigned int i;
    int diff1,diff2;
    if(e <= b[0]){ return 0; }
    for(i=startIndex;i<b.size();i++){
        if(e == b[i]){
            return i;
        } else if(e < b[i]){
            diff1 = e - b[i-1];
            diff2 = b[i] - e; 
            return (diff1 <= diff2)? i-1 : i;
        }
    }
    return i-1;
}

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int v;
    unsigned int idx;
    int sum;
    
    cin >> C;
	for(int cnt = 0 ; cnt < C ; cnt++){
        cin >> A >> B;
        for(int i =0;i<A;i++){
            cin >> v;
            a.push_back(v);
        }
        for(int i =0;i<B;i++){
            cin >> v;
            b.push_back(v);
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        startIndex = 0;
        sum = 0;
        for(auto e : a){
            idx = find_near(e);
            startIndex = idx;
            //cout << idx << " " << b[idx] << " " << e << endl;
            sum += b[idx];
        }
        cout << sum << "\n";
        a.clear();
        b.clear();
    }

    return 0;
}
