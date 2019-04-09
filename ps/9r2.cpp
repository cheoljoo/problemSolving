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
 
#define CACHEMAX 70
 
int C,K;
int N,M;

class node
{
    public:
        int parent;
        int depth;
        char c;

        int height;
        vector<int> children;
        bitset<26> cache[CACHEMAX];
        int cacheMaxLevel=0;

        node() {};
        virtual ~node(){};
};
vector<class node> tree(2);

int inputParent[500000];
char inputChar[500000];

bitset<26>
reverse_bitset(bitset<26> a)
{
    std::string str = a.to_string();
    std::reverse(str.begin(), str.end());
    bitset<26> y = bitset<26>(str);

    return y;
}

void
print_bitset(const char *s, int n, bitset<26> bs)
{
    cout << s << " " << n << " : " ;
    for(char ch='a'; ch <= 'z'; ch++){
        cout << ch;
    }
    cout << endl;
    cout << s << " " << n << " : " ;
    bitset<26> a = reverse_bitset(bs);
    cout << a << endl;
}

int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);
    int t;
    char ch;
    

    scanf("%d %d", &N,&M);
	for(int c = 1 ; c < N ; c++){
		scanf("%d",&t);
        inputParent[c] = t;
    }
    //getchar();
	for(int c = 0 ; c < N ; ){
		scanf("%c",&ch);
        if (ch< 'a' || ch > 'z'){ continue; }
        inputChar[c] = ch;
        c++;
    }
    // init
    tree[1].parent = 0;
    tree[1].depth = 1;
    tree[1].c = inputChar[0];
	tree[1].cache[0][static_cast<int>(inputChar[0] - 'a')] = 1;
	for(int c = 1 ; c < N ; c++){
		int t = inputParent[c];
        class node node;
        node.parent = t;
        node.depth = tree[t].depth + 1;
        node.height=1;
        tree.push_back(node);
        tree[t].children.push_back(c+1);
        tree[c+1].c = inputChar[c];
        int cacheDepth = 0;
        for(int s=c+1; s != 0 ; s = tree[s].parent,cacheDepth++){
            int p = tree[s].parent;
            //;; cout << "[S:" << s << "]";
            //;; cout << s << ":" << p << "," << tree[s].c << ":" << static_cast<int>(tree[s].c - 'a') << ",D" << cacheDepth << "|" ;
            if( (tree[s].height+1) >  tree[p].height ){
                tree[p].height = tree[s].height +1;
            }
            if(cacheDepth >= CACHEMAX){ continue; } 
            int v = tree[s].cache[cacheDepth][static_cast<int>(inputChar[c] - 'a')];
            tree[s].cache[cacheDepth][static_cast<int>(inputChar[c] - 'a')] = (v == 0) ? 1 : 0 ;    
            if(tree[s].cacheMaxLevel < cacheDepth){ tree[s].cacheMaxLevel = cacheDepth; } 
        }
        //;; cout << endl;
    }

#if 0
    for(int i=0;i < tree.size();i++){
        cout << i ;
        cout << " : parent " << tree[i].parent ;
        cout << " : depth " << tree[i].depth ;
        cout << " : char  " << tree[i].c ;
        cout << " : height  " << tree[i].height ;
        cout << " : cacheMaxLevel  " << tree[i].cacheMaxLevel ;
        cout << " : children [ ";
        for(int j=0;j < tree[i].children.size();j++){
            cout << tree[i].children[j];
        }
        cout << " ]" << endl;
        for(int j=0;j <= tree[i].cacheMaxLevel;j++){
            print_bitset("  cache",j,tree[i].cache[j]);
        }
    }
#endif

	for(int m = 0 ; m < M ; m++){
        int start,depth;
		scanf("%d %d",&start,&depth);
        vector<int> lStack;
        bitset<26>  answer;
        lStack.push_back(start);
        while(lStack.size()){
			//;; cout << "{stack} "; for (auto i = lStack.begin(); i != lStack.end(); ++i){ cout << *i << ' '; } cout << endl;
            int node = lStack.back();
            lStack.pop_back();
			//;; cout << "node:" << node << " , tree.depth:" << tree[node].depth << " , depth:" << depth << " , height:" << tree[node].height << " ,cacheMaxLevel:" << tree[node].cacheMaxLevel << " ,diffDepth:" << depth - tree[node].depth << endl;
            if(tree[node].depth <= depth){ 
				//;; cout << "{children} "; for (auto i = tree[node].children.begin(); i != tree[node].children.end(); ++i){ cout << *i << ' '; } cout << endl;
                int diffDepth = depth - tree[node].depth;
                if( diffDepth < tree[node].height){
                    if( diffDepth <= tree[node].cacheMaxLevel ){
                        //;; cout << "set" << endl;
                        answer ^= tree[node].cache[diffDepth];
                    } else {
                        for(int j=0;j < tree[node].children.size();j++){
                            int child = tree[node].children[j];
                            //;; cout << "go child:" << child << " , tree.depth:" << tree[child].depth << " , depth:" << depth << endl;
                            //if(tree[child].depth == depth){
                                //answer[tree[child].c]++;
                            //} else {
                                lStack.push_back(child);
                            //}
                        }
                    }
                }
            }
        };
        //;; print_bitset("Answer",0,answer);
        printf("%s\n", (answer.count() > 1) ? "No" : "Yes");
    }

    return 0;
}
