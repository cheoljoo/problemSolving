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

vector<long long int> a;
set<long long int> b;

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long int v;
    std::set<long long int>::iterator itlow,itup;

    long long int sum;
    long long int diff1,diff2;
    long long int p1,p2;
    long long int near;
    
    cin >> C;
	for(int cnt = 0 ; cnt < C ; cnt++){
        cin >> A >> B;
        for(int i =0;i<A;i++){
            cin >> v;
            a.push_back(v);
        }
        for(int i =0;i<B;i++){
            cin >> v;
            b.insert(v);
        }
        //std::cout << "b contains:";
        //for (std::set<int>::iterator it=b.begin(); it!=b.end(); ++it)
            //std::cout << ' ' << *it;
        //std::cout << '\n';
        sum = 0;
        for(auto e : a){
            itlow=b.lower_bound (e);
            if((e == *itlow) || (itlow == b.begin()) ){
                //cout << "e:" << e << " ,near : " << *itlow << endl;
                sum += (*itlow);
            } else if(itlow == b.end()){
                itlow--;
                //cout << "e:" << e << " ,near : " << *itlow << endl;
                sum += (*itlow);
            } else {
                p2 = *itlow;
                p1 = *(--itlow);
                diff1 = e-p1;
                diff2 = p2-e; 
                near = (diff1 <= diff2)? p1 : p2;
                //cout << "e:" << e << " ,near : " << near << endl;
                sum += near;
            }
        }
        cout << sum << "\n";
        a.clear();
        b.clear();
    }

    return 0;
}
