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
 
int N,K;

int main(int argc,char *argv[])
{
    std::vector<int> vec;

	ios_base::sync_with_stdio(false);
    
    scanf("%d %d", &N,&K);

	for(int i = 0 ; i < N ; i++){
        vec.push_back(i+1);
    }


    int index = K -1;
    cout << "<" ;
	for(int i = 0 ; i < N ; i++){
        if(i != 0){ cout << ", "; }
        cout << vec[index] ;
        vec.erase(vec.begin() + index);  // remove vec[K-1]
        if(vec.size() == 0) break;
        index += (K - 1);
        index %= vec.size();
    }
    cout << ">" << endl;

    return 0;
}
