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
 
int N;    // opeation size
int O;  // order
long long int val1,val2,old;

set<long long int> s;     // keys to find closest : orderd
map<long long int,long long int> m;   // key , value

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long int sum = 0.0;
    set<long long int>::iterator itlow,itup;

    cin >> N;
	for(int cnt = 0 ; cnt < N ; cnt++){
        cin >> O ;
        //cout << "operation:" << O << "  ";;
        if(O == 3){
            cin >> val1;
            //cout << val1 << " __ \n";
        } else {
            cin >> val1 >> val2;
            //cout << val1 << " " << val2 << " __ ";
        }
        if(O == 1){
            //m.insert( pair<long long int,long long int>(val1 , val2) );     // key , value
            old = m[val1];
            //cout << "val1:" << val1 << " ,val2: " << val2 << " ,old:" << old << endl;
            m[val1] += val2;
            ////cout << "debug val1:" << val1 << ",ret:" << m[val1] << endl;
            ////cout << "debug:" << m[25] << endl;      // not exist , return 0
            ////cout << "debug:" << m[24] << endl;
            s.insert( (long long int) val1 );     // key
            sum += val2;
            cout << sum << '\n';
        } else if(O == 2){
            long long int localsum = 0;
            //cout << "val1:" << val1 << " ,val2: " << val2 << endl;
            itlow=s.lower_bound (val1); 
            itup=s.upper_bound (val2);
            //std::cout << "s O 2:";
            for (std::set<long long int>::iterator it=itlow; it!=itup; ++it){
                //std::cout << ' ' << *it << "[" << m[*it] << "]" ;
                localsum += m[*it];
            }
            //std::cout << '\n';
            cout << localsum << '\n';
        } else {
            old = m[val1];
            m[val1] = 0;
            sum -= old;
            cout << sum << '\n';
        }
        /*
        std::cout << "s contains:";
        for (std::set<long long int>::iterator it=s.begin(); it!=s.end(); ++it)
            std::cout << ' ' << *it;
        std::cout << '\n';
        */
    }

    return 0;
}
