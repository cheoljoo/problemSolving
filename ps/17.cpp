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

// result
#define WIN 0
#define EQUAL 1
#define LOSE 2

map<string,int> country;
map<int,string> countryName;
int vs[6][2];   // A vs B 
float WEL[6][3];   // A_Win A_Equal A_Lose
float resultProportion[4];  // each country's proportion


void plusPoint(int country , int point, int& a,int& b,int& c,int& d)        
{
    switch(country){
        case 0:
            a += point;
            break;
        case 1:
            b += point;
            break;
        case 2:
            c += point;
            break;
        case 3:
            d += point;
            break;
        default:
            cerr << "plusPoint ERROR : default" << endl;
            break;
    }
}

void cal(int index , int wel, int a,int b,int c,int d,float proportion,string s) 
    // index 0~5
    // a,b,c,d is for country's winning point.
{
#if 0
    cout << "process:" << s << endl;
    cout << "cal1: index=" << index << ",wel=" << wel << ",a=" << a << ",b=" << b << ",c=" << c << ",d=" << d << ",proportion=" << proportion << endl;
#endif

    switch(wel){
        case WIN:
            plusPoint(vs[index][0],3,a,b,c,d); // 3 point
            break;
        case EQUAL:
            plusPoint(vs[index][0],1,a,b,c,d); // 1 point
            plusPoint(vs[index][1],1,a,b,c,d); // 1 point
            break;
        case LOSE:
            plusPoint(vs[index][1],3,a,b,c,d); // 3 point
            break;
        default:
            cerr << "cal ERROR : default" << endl;
            break;
    }

    proportion *= WEL[index][wel];

#if 0
    cout << "cal2: index=" << index << ",wel=" << wel << ",a=" << a << ",b=" << b << ",c=" << c << ",d=" << d << ",proportion=" << proportion << endl;
#endif

    if(index == 5){
        // this is end. so you can calculate who is winner.
        vector< pair<int,int> > vec;
        vec.push_back(make_pair(a,0));
        vec.push_back(make_pair(b,1));
        vec.push_back(make_pair(c,2));
        vec.push_back(make_pair(d,3));
        // Using simple sort() function to sort
        sort(vec.begin(), vec.end());
#if 0
        for (int i=0; i<4; i++)
        {
            // "first" and "second" are used to access
            // 1st and 2nd element of pair respectively
            cout << "idx:" << i << " -- " << vec[i].first << " "
                << vec[i].second << endl;
        }
#endif
        if(vec[3].first != vec[2].first){
            int cnt = 0;
            for (int i=0; i<4; i++)
            {
                if(vec[i].first == vec[2].first){
                    cnt ++;
                }
            }
            // vec[3].second is 1st winner.
            resultProportion[vec[3].second] += proportion;
            for (int i=0; i<4; i++)
            {
                if(vec[i].first == vec[2].first){
                    resultProportion[vec[i].second] += (proportion/cnt);
                }
            }
        } else {
            int cnt = 0;
            for (int i=0; i<4; i++)
            {
                if(vec[i].first == vec[2].first){
                    cnt ++;
                }
            }
            for (int i=0; i<4; i++)
            {
                if(vec[i].first == vec[2].first){
                    resultProportion[vec[i].second] += ((2*proportion)/cnt);
                }
            }
        }
#if 0
        for(int i=0;i<4;i++){
            cout << countryName[i] << " " << resultProportion[i] << endl;
        }
#endif
    } else {
        string s0 = s + "-0";
        cal(index+1,WIN,a,b,c,d,proportion , s0);
        string s1 = s + "-1";
        cal(index+1,EQUAL,a,b,c,d,proportion , s1);
        string s2 = s + "-2";
        cal(index+1,LOSE,a,b,c,d,proportion , s2);
    }
    return;
}

int main(int argc,char *argv[])
{

	ios_base::sync_with_stdio(false);
    
    char ss[11];
    float pp;
	for(int i = 0 ; i < 4 ; i++){
        scanf("%s",ss);
        country[ss] = i;
        countryName[i] = ss;
        resultProportion[i] = 0.0;
    }
#if 0
    for(auto const &vk : country){
        cout << vk.second << ": " << vk.first << endl;
    }
#endif
	for(int i = 0 ; i < 6 ; i++){
        scanf("%s",ss);
        vs[i][0] = country[ss];
        scanf("%s",ss);
        vs[i][1] = country[ss];
        scanf("%f",&pp);
        WEL[i][0] = pp;
        scanf("%f",&pp);
        WEL[i][1] = pp;
        scanf("%f",&pp);
        WEL[i][2] = pp;
    }
#if 0
	for(int i = 0 ; i < 6 ; i++){
        cout << countryName[vs[i][0]] << " : ";
        cout << countryName[vs[i][1]] << " = ";
        cout << "Win-" << WEL[i][0] << " , ";
        cout << "Equal-" << WEL[i][1] << " , ";
        cout << "Lose-" << WEL[i][2] << endl;
    }
#endif

    cal(0,WIN,0,0,0,0,1.0,"0");
    cal(0,EQUAL,0,0,0,0,1.0,"0");
    cal(0,LOSE,0,0,0,0,1.0,"0");

    for(int i=0;i<4;i++){
        //;;cout << countryName[i] << " " << resultProportion[i] << endl;
        printf("%.10f\n", resultProportion[i]);
    }

    return 0;
}
