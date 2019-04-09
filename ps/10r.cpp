#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
#include <map>
#include <iterator>
#include <bitset>
#include <unistd.h>
 
using namespace std;
 
#define FLOOR_MAX 100000
#define ELIVATOR_MAX 1001
 
int N,M;

vector<int> elivator[ELIVATOR_MAX];     // floor
vector<int> floor[FLOOR_MAX];       // elivator
int elivatorCost[ELIVATOR_MAX];     // minimal cost
bitset<ELIVATOR_MAX> elivatorGone;

    set<int> from_elivator;     // value : elivator
    set<int> to_elivator;       // value : elivator
        vector<int> v(ELIVATOR_MAX);

#define DBG 1

void print_elivator(int cnt)
{
#if DBG
    cout << "print_elivator : cnt=" << cnt << endl;
    for(int i=0;i<ELIVATOR_MAX;i++){
        if(elivator[i].size()){
            cout << "elivator[" << i << "]:" ;
            for(int j=0;j<elivator[i].size();j++){
                cout << " " << elivator[i][j] ;
            }
            cout << endl;
        }
    }
    for(int i=0;i<FLOOR_MAX;i++){
        if(floor[i].size()){
            cout << "floor[" << i << "]:" ;
            for(int j=0;j<floor[i].size();j++){
                cout << " " << floor[i][j] ;
            }
            cout << endl;
        }
    }
    set<int>::iterator it;
    cout << "from_elivator :";
    for (it=from_elivator.begin(); it!=from_elivator.end(); ++it){
        cout << " " << *it;
    }
    cout << endl;
    cout << "to_elivator :";
    for (it=to_elivator.begin(); it!=to_elivator.end(); ++it){
        cout << " " << *it;
    }
    cout << endl;
    if(cnt == ELIVATOR_MAX){
        cout << "Intersection: " ;
        for(int i=0;i<v.size();i++){
            cout << v[i] << " ";
        }
        cout << endl;
    }
#endif
}

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    int start,jump;
    int from,to;
    
    scanf("%d %d", &N,&M);
	for(int b = 0 ; b < M ; b++){
		scanf("%d %d",&start,&jump);
        for(int f=start;f <= N ; f += jump){
            floor[f].push_back(b);
            elivator[b].push_back(f);
        }
    }
	scanf("%d %d",&from,&to);

    cout << "1" << endl;
    //print_elivator(1);
    if(floor[from].size() == 0){ printf("-1\n"); return 0; }
    else if(floor[to].size() == 0){ printf("-1\n"); return 0; }
    for(int i=0;i<floor[from].size();i++){
        from_elivator.insert(floor[from][i]);
    }
    cout << "2" << endl;
    //print_elivator(2);
    for(int i=0;i<floor[to].size();i++){
        to_elivator.insert(floor[to][i]);
    }
    cout << "3" << endl;
    //print_elivator(3);
    int cnt = 1;
    while(1){
        vector<int> temp1;
        vector<int> temp2;
        set<int>::iterator it;
        vector<int>::iterator vit;
        int sizeFrom = from_elivator.size();
        int sizeTo = to_elivator.size();

        print_elivator(cnt);
        vit = set_intersection(from_elivator.begin(),from_elivator.end(),to_elivator.begin(),to_elivator.end(),v.begin());
        cout << "size:" << v.size() << ",resize:" << vit-v.begin() << endl;
        if(vit-v.begin()){ v.resize(vit-v.begin()); break; }
        cout << "size:" << v.size() << ",resize:" << vit-v.begin() << endl;
        for (it=from_elivator.begin(); it!=from_elivator.end(); ++it){
            cout << cnt << " from *it:" << *it << ",elivator size:" << elivator[*it].size() << endl;
            for(int i=0;i<elivator[*it].size();i++){
                for(int j=0;j<floor[elivator[*it][i]].size();j++){
                    cout << "[" << i << "][" << j << "] floor " <<  elivator[*it][i] << " : elivator " << floor[elivator[*it][i]][j] << endl;
                    temp1.push_back(floor[elivator[*it][i]][j]);
                }
            }
        }
        for(int i=0;i<temp1.size();i++){
            from_elivator.insert(temp1[i]);
        }
        cnt++;

        print_elivator(cnt);
        cout << "4.1" << endl;
        vit = set_intersection(from_elivator.begin(),from_elivator.end(),to_elivator.begin(),to_elivator.end(),v.begin());
        cout << "4.2" << endl;
        cout << "size:" << v.size() << ",resize:" << vit-v.begin() << endl;
        if(vit-v.begin()){ v.resize(vit-v.begin()); break; }
        cout << "size:" << v.size() << ",resize:" << vit-v.begin() << endl;
        cout << "4.3" << endl;
        for (it=to_elivator.begin(); it!=to_elivator.end(); ++it){
            cout << cnt << " to *it:" << *it << ",elivator size:" << elivator[*it].size() << endl;
            for(int i=0;i<elivator[*it].size();i++){
                for(int j=0;j<floor[elivator[*it][i]].size();j++){
                    cout << "[" << i << "][" << j << "] floor " <<  elivator[*it][i] << " : elivator " << floor[elivator[*it][i]][j] << endl;
                    temp2.push_back(floor[elivator[*it][i]][j]);
                }
            }
        }
        for(int i=0;i<temp2.size();i++){
            to_elivator.insert(temp2[i]);
        }
        cnt++;
        if( (sizeFrom == from_elivator.size()) && (sizeTo == to_elivator.size()) ){ 
            printf("-1\n");    
            return 0;
        }
    };
    print_elivator(ELIVATOR_MAX);
    printf("%d\n",cnt);

    return 0;
}
