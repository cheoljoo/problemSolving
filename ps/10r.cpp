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
bitset<ELIVATOR_MAX> elivatorGone;
bitset<FLOOR_MAX> floorGone;
vector<int> stack;
vector<int> result;
int floorCost[FLOOR_MAX];       // minus  --
int elivatorCost[ELIVATOR_MAX];     // minus  --

    set<int> from_elivator;     // value : elivator
    set<int> to_elivator;       // value : elivator
        vector<int> v(ELIVATOR_MAX);

#define DBG 1

void print_ef()
{
    cout << "print_ef "  << endl;
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
}
void print_from_to_elivator(int count)
{
    set<int>::iterator it;
    for(int i=0;i<count;i++){ cout << "__" ; }
    cout << "from_elivator :";
    for (it=from_elivator.begin(); it!=from_elivator.end(); ++it){
        cout << " " << *it;
    }
    cout << endl;

    for(int i=0;i<count;i++){ cout << "__" ; }
    cout << "to_elivator :";
    for (it=to_elivator.begin(); it!=to_elivator.end(); ++it){
        cout << " " << *it;
    }
    cout << endl;
}
void print_stack(int count)
{
    for(int i=0;i<count;i++){ cout << "__" ; }
    cout << "stack :";
    for (int i=0;i<stack.size();i++){
        cout << " " << stack[i];
    }
    cout << endl;
}
void print_cost(int count)
{
    for(int i=0;i<count;i++){ cout << "__" ; }
    cout << "floorCost :";
    for (int i=0;i<FLOOR_MAX;i++){
        if(floorCost[i] != 0){ cout << " " << i << ":" << floorCost[i]; }
    }
    cout << endl;
    /*
    cout << "elivatorCost :";
    for (int i=0;i<ELIVATOR_MAX;i++){
        if(elivatorCost[i] != 0){ cout << " " << i << ":" << elivatorCost[i]; }
    }
    cout << endl;
    */
}

void DFS(int from_floor,int to_floor,int count)
{
    for(int c=0;c<count;c++){ cout << "__" ; }
    cout << "DFS - from:" << from_floor << " to:" << to_floor << " count:" << count << endl;
    print_stack(count);
    print_cost(count);
    if(from_floor == to_floor){
        for(int c=0;c<count;c++){ cout << "__" ; }
        cout << "==stack :";
        for (int i=0;i<stack.size();i++){
            cout << " " << stack[i];
        }
        cout << endl;
        for(int c=0;c<count;c++){ cout << "__" ; }
        cout << "DFS1 : return count:"<< count << endl;

        if( (result.size() == 0) || (result.size() > stack.size()) ){
            result.clear();
            for(int i=0;i<stack.size();i++){
                result.push_back(stack[i]);
            }
        }
        return ;
    }
    if( (floorCost[from_floor] != 0) && (floorCost[from_floor] <= count) ){ 
        for(int c=0;c<count;c++){ cout << "__"; }
        cout << "DFS2: return count:"<< count << endl;
        return; 
    }
    floorCost[from_floor] = count;

    for(int i=0;i<floor[from_floor].size();i++){
        int myElivator = floor[from_floor][i];
        for(int c=0;c<count;c++){ cout << "__" ; }
        cout << "myElivator A:" << myElivator << " Gone:" << elivatorGone[myElivator] << " Cost:" << elivatorCost[myElivator] << endl;
        if(elivatorGone[myElivator] == 1){ continue; }
        //if( (elivatorCost[myElivator] != 0) && (elivatorCost[myElivator] <= count) ){ continue; }
        elivatorGone[myElivator] = 1;
        //elivatorCost[myElivator] = count+1;
        for(int c=0;c<count;c++){ cout << "__" ; }
        cout << "myElivator B:" << myElivator << endl;
        for(int c=0;c<count;c++){ cout << "__" ; }
        cout << "push_back:" << myElivator << endl;
        stack.push_back(myElivator);
        for(int j=0;j<elivator[myElivator].size();j++){
            int myFloor = elivator[myElivator][j];
            for(int c=0;c<count;c++){ cout << "__" ; }
            cout << "myFloor C:" << myFloor << " floorGone:" << floorGone[myFloor] << " Cost:" << floorCost[myFloor] <<  endl;
            if(floorGone[myFloor] == 1){ continue; }
            if( (floorCost[myFloor] != 0) && (floorCost[myFloor] <= count) ){ continue; }
            floorGone[myFloor] = 1;
            //floorCost[myFloor] = count+1;
            for(int c=0;c<count;c++){ cout << "__" ; }
            cout << "myFloor D:" << myFloor << endl;
            print_stack(count);
            print_cost(count);
            DFS(myFloor, to_floor,count+1);
            floorGone[myFloor] = 0;
        }
        elivatorGone[myElivator] = 0;
        int node = stack.back();
        for(int c=0;c<count;c++){ cout << "__" ; }
        cout << "pop_back" << endl;
        stack.pop_back();
    }
    for(int c=0;c<count;c++){ cout << "__" ; }
    cout << "DFS3: return count:"<< count << endl;
    return;
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

    print_ef();
    DFS(from,to,1);

    if(result.size() == 0){
        printf("-1\n");
    } else {
        printf("%lu\n",result.size());
        for (int i=0;i<result.size();i++){
            printf("%d\n",result[i] +1);
        }
    } 

    /*
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
    */
    //print_elivator(ELIVATOR_MAX);
    //printf("%d\n",cnt);

    return 0;
}
