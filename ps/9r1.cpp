#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
#include <bitset>
#include <map>
#include <iterator>
#include <unistd.h>
 
using namespace std;
 
#define MAX 50
 
int C,K;
int N,M;

class node
{
    public:
        int parent;
        int depth;
        int height;
        vector<int> children;
        char c;
        bitset<26> cache[MAX];

        node() {};
        virtual ~node(){};
};
vector<class node> tree(2);

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    int t;
    char ch;
    
    // init
    tree[1].depth = 1;

    scanf("%d %d", &N,&M);
	for(int c = 1 ; c < N ; c++){
		scanf("%d",&t);
        class node node;
        node.parent = t;
        node.depth = tree[t].depth + 1;
        node.height=1;
        tree.push_back(node);
        tree[t].children.push_back(c+1);
        for(int s=c+1; s != 1 ; s = tree[s].parent){
            int p = tree[s].parent;
            if(tree[s].height+1 >  tree[p].height){
                tree[p].height = tree[s].height +1;
            }
        }
    }
    getchar();
	for(int c = 0 ; c < N ; ){
		scanf("%c",&ch);
        if (ch< 'a' || ch > 'z'){ continue; }
        tree[c+1].c = ch;
        c++;
    }

#if 0
    for(int i=0;i < tree.size();i++){
        cout << i ;
        cout << " : parent " << tree[i].parent ;
        cout << " : depth " << tree[i].depth ;
        cout << " : char  " << tree[i].c ;
        cout << " : height  " << tree[i].height ;
        cout << " : children [ ";
        for(int j=0;j < tree[i].children.size();j++){
            cout << tree[i].children[j];
        }
        cout << " ]" << endl;
    }
#endif

	for(int m = 0 ; m < M ; m++){
        int start,depth;
		scanf("%d %d",&start,&depth);
        vector<int> lStack;
        map< char,int > answer;
        lStack.push_back(start);
        while(lStack.size()){
			//;; cout << "{stack} "; for (auto i = lStack.begin(); i != lStack.end(); ++i){ cout << *i << ' '; } cout << endl;
            int node = lStack.back();
            lStack.pop_back();
			//;; cout << "node:" << node << " , tree.depth:" << tree[node].depth << " , depth:" << depth << " , height:" << tree[node].height << endl;
            if(tree[node].depth < depth){ 
				//;; cout << "{children} "; for (auto i = tree[node].children.begin(); i != tree[node].children.end(); ++i){ cout << *i << ' '; } cout << endl;
                if( (depth - tree[node].depth) < tree[node].height){
                    for(int j=0;j < tree[node].children.size();j++){
                        int child = tree[node].children[j];
                        //;; cout << "child:" << child << " , tree.depth:" << tree[child].depth << " , depth:" << depth << endl;
                        if(tree[child].depth == depth){
                            answer[tree[child].c]++;
                        } else {
                            lStack.push_back(child);
                        }
                    }
                }
            }
        };
        if(answer.size() == 0){ printf("Yes\n"); }
        else {
            int cnt=0;
            for (std::map<char,int>::iterator it=answer.begin(); it!=answer.end(); ++it){
                //;; cout << "answer: " << it->first << " => " << it->second << '\n';
                if(it->second %2 == 1){ cnt++; }
            }
            printf("%s\n", (cnt > 1) ? "No" : "Yes");
        }
    }

    return 0;
}
