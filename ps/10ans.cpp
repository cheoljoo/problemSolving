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
 
#define story_MAX 100000
#define ELIVATOR_MAX 1001
 
int N,M;

vector<int> elivator[ELIVATOR_MAX];     // story
vector<int> story[story_MAX];       // elivator
bitset<ELIVATOR_MAX> elivatorGone;
bitset<story_MAX> storyGone;
vector<int> stack;
vector<int> result;
int storyCost[story_MAX];       // minus  --
int elivatorCost[ELIVATOR_MAX];     // minus  --

    set<int> from_elivator;     // value : elivator
    set<int> to_elivator;       // value : elivator
        vector<int> v(ELIVATOR_MAX);

#define DBG 0

void print_ef()
{
#if DBG
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
    for(int i=0;i<story_MAX;i++){
        if(story[i].size()){
            cout << "story[" << i << "]:" ;
            for(int j=0;j<story[i].size();j++){
                cout << " " << story[i][j] ;
            }
            cout << endl;
        }
    }
#endif
}
void print_from_to_elivator(int count)
{
#if DBG
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
#endif
}
void print_stack(int count)
{
#if DBG
    for(int i=0;i<count;i++){ cout << "__" ; }
    cout << "stack :";
    for (int i=0;i<stack.size();i++){
        cout << " " << stack[i];
    }
    cout << endl;
#endif
}
void print_cost(int count)
{
#if DBG
    for(int i=0;i<count;i++){ cout << "__" ; }
    cout << "storyCost :";
    for (int i=0;i<story_MAX;i++){
        if(storyCost[i] != 0){ cout << " " << i << ":" << storyCost[i]; }
    }
    cout << endl;
    /*
    cout << "elivatorCost :";
    for (int i=0;i<ELIVATOR_MAX;i++){
        if(elivatorCost[i] != 0){ cout << " " << i << ":" << elivatorCost[i]; }
    }
    cout << endl;
    */
#endif
}

void DFS(int from_story,int to_story,int count)
{
    //;; for(int c=0;c<count;c++){ cout << "__" ; }
    //;; cout << "DFS - from:" << from_story << " to:" << to_story << " count:" << count << endl;
    print_stack(count);
    print_cost(count);
    if(from_story == to_story){
        //;; for(int c=0;c<count;c++){ cout << "__" ; }
        //;; cout << "==stack :";
        //;; for (int i=0;i<stack.size();i++){
            //;; cout << " " << stack[i];
        //;; }
        //;; cout << endl;
        //;; for(int c=0;c<count;c++){ cout << "__" ; }
        //;; cout << "DFS1 : return count:"<< count << endl;

        if( (result.size() == 0) || (result.size() > stack.size()) ){
            result.clear();
            for(int i=0;i<stack.size();i++){
                result.push_back(stack[i]);
            }
        }
        return ;
    }
    if( (storyCost[from_story] != 0) && (storyCost[from_story] <= count) ){ 
        //;; for(int c=0;c<count;c++){ cout << "__"; }
        //;; cout << "DFS2: return count:"<< count << endl;
        return; 
    }
    storyCost[from_story] = count;

    for(int i=0;i<story[from_story].size();i++){
        int myElivator = story[from_story][i];
        //;; for(int c=0;c<count;c++){ cout << "__" ; }
        //;; cout << "myElivator A:" << myElivator << " Gone:" << elivatorGone[myElivator] << " Cost:" << elivatorCost[myElivator] << endl;
        if(elivatorGone[myElivator] == 1){ continue; }
        //if( (elivatorCost[myElivator] != 0) && (elivatorCost[myElivator] <= count) ){ continue; }
        elivatorGone[myElivator] = 1;
        //elivatorCost[myElivator] = count+1;
        //;; for(int c=0;c<count;c++){ cout << "__" ; }
        //;; cout << "myElivator B:" << myElivator << endl;
        //;; for(int c=0;c<count;c++){ cout << "__" ; }
        //;; cout << "push_back:" << myElivator << endl;
        stack.push_back(myElivator);
        for(int j=0;j<elivator[myElivator].size();j++){
            int mystory = elivator[myElivator][j];
            //;; for(int c=0;c<count;c++){ cout << "__" ; }
            //;; cout << "mystory C:" << mystory << " storyGone:" << storyGone[mystory] << " Cost:" << storyCost[mystory] <<  endl;
            if(storyGone[mystory] == 1){ continue; }
            if( (storyCost[mystory] != 0) && (storyCost[mystory] <= count) ){ continue; }
            storyGone[mystory] = 1;
            //storyCost[mystory] = count+1;
            //;; for(int c=0;c<count;c++){ cout << "__" ; }
            //;; cout << "mystory D:" << mystory << endl;
            print_stack(count);
            print_cost(count);
            DFS(mystory, to_story,count+1);
            storyGone[mystory] = 0;
        }
        elivatorGone[myElivator] = 0;
        //int node = stack.back();
        //;; for(int c=0;c<count;c++){ cout << "__" ; }
        //;; cout << "pop_back" << endl;
        stack.pop_back();
    }
    //;; for(int c=0;c<count;c++){ cout << "__" ; }
    //;; cout << "DFS3: return count:"<< count << endl;
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
            story[f].push_back(b);
            elivator[b].push_back(f);
        }
    }
	scanf("%d %d",&from,&to);

    //;; cout << "1" << endl;
    //print_elivator(1);
    if(story[from].size() == 0){ printf("-1\n"); return 0; }
    else if(story[to].size() == 0){ printf("-1\n"); return 0; }
    //for(int i=0;i<story[from].size();i++){
        //from_elivator.insert(story[from][i]);
    //}
    //;; cout << "2" << endl;
    //print_elivator(2);
    //for(int i=0;i<story[to].size();i++){
        //to_elivator.insert(story[to][i]);
    //}
    //;; cout << "3" << endl;
    //print_elivator(3);
    //int cnt = 1;

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

    return 0;
}

