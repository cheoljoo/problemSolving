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

int find_near(int e,int& result)
{
    int si = startIndex;
    int se = b.size() -1;;
    int mid;
    while(si < b.size()){
        mid =  (si + se) /2;
        //cout << "si:" << si << ",se:" << se << ",mid:" << mid << ",e:" << e << endl;
        //cout << "a:";
        //for(auto n : a){
            //cout << " " << n;
        //}
        //cout << endl;
        //cout << "b:";
        //for(auto n : b){
            //cout << " " << n;
        //}
        //cout << endl;
        if(b[si] == e){ 
            startIndex = si;
            break;
        }
        if(b[si] > e){
            startIndex = si;
            break;
        }
        if(si == se){
            startIndex = si;
            break;
        }
        if(si == mid){
            si++;
            startIndex = si;
            break;
        }

        if(b[mid] > e){
            si++;
            se = mid;
        }
        else {
            si = mid;
        }
    }
    //cout << "result index:" << si << endl;
    return startIndex;
}

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int v;
    int idx;
    int sum;
    int diff1,diff2;
    int near;
    
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
        int result=0;
        startIndex = 0;
        sum = 0;
        for(auto e : a){
            idx = find_near(e,result);
            if(idx == 0){
                //cout << "near : " << b[idx] << endl;
                sum += b[idx];
            } else if(idx == b.size()){
                //cout << "near : " << b[idx-1] << endl;
                sum += b[idx -1];
            } else {
                diff1 = e - b[idx-1];
                diff2 = b[idx] - e; 
                near = (diff1 <= diff2)? b[idx-1] : b[idx];
                //cout << "near : " << near << endl;
                sum += near;
            }
        }
        cout << sum << "\n";
        a.clear();
        b.clear();
    }

    return 0;
}
