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

struct comp
{
    bool operator()(const vector<char>& lhs, const vector<char>& rhs) const
    {
        if(lhs.size() !=  rhs.size()){
            return lhs.size() < rhs.size();
        }

        return lhs < rhs;
    }
};

 
int N;    // opeation size
int O;  // order
long long int val1,val2,old;

set< vector<char>,comp > ss;     // keys to find closest : orderd
map< vector<char> ,long long int> mm;   // key , value

vector<char> in1,in2;

long long int getin(vector<char>& in)
{
    char charin[201];
    cin >> charin;
    in.clear();
    for(int i=0;charin[i] != 0;i++){
        in.push_back(charin[i]);
    }

    //cout << " ~"; for(auto a : in) { cout << a; } cout << "~ ";

    return (long long int) ( atoi(charin) );

}

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long int sum = 0.0;
    set<long long int>::iterator itlow,itup;

    cin >> N;
	for(int cnt = 0 ; cnt < N ; cnt++){
        cin >> O ;
        cout << "operation:" << O << "  ";;
        if(O == 3){
            val1 = getin(in1);
            cout << val1 << " __ ";
        } else {
            val1 = getin(in1);
            val2 = getin(in2);
            cout << val1 << " " << val2 << " __ ";
        }
        if(O == 1){
            sum += val2;
            cout << sum << ' ';

            old = mm[in1];
            mm[in1] += val2;
            ss.insert(in1);     // key

        } else if(O == 2){
            long long int localsum = 0;

            set< vector<char>, comp >::iterator ssitlow, ssitup;
            ssitlow=ss.lower_bound (in1); 
            ssitup=ss.upper_bound (in2);
            if(ssitlow == ss.end()){
                cout << 0 << ' ';
            } else {
                std::cout << "ss ";
                for(auto a : *ssitlow) { cout << a; } cout << '~'; 
                if(ssitup != ss.end()){ for(auto a : *ssitup) { cout << a; } cout << " : "; }
                else { cout << "end : "; }
                for (std::set< vector<char>, comp >::iterator it=ssitlow; it!=ssitup; ++it){
                    cout << ' '; for(auto a : *it) { cout << a; } cout << "[" << mm[*it] << "] ";
                    localsum += mm[*it];
                }
                cout << " __ ";
                cout << localsum << ' ';
            }

        } else {
            old = mm[in1];
            mm[in1] = 0;
            sum -= old;
            cout << sum << ' ';
        }
        std::cout << "ss contains:";
        for (std::set< vector<char>, comp >::iterator it=ss.begin(); it!=ss.end(); ++it){
            cout << " "; for(auto a : *it) { cout << a; } cout << "[" << mm[*it] << "] ";
        }
        std::cout << '\n';
        /*
        */
    }
    cout << '\n';

    return 0;
}
