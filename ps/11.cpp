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

//;; for(int i=0;i<vec.size();i++){ cout << vec[i] << " "; } cout << endl;
//;; cout << "N:" << N << ",K:" << K << endl;

    int index = K -1;
//;; cout << "index:" << index << endl;
    cout << "<" ;
	for(int i = 0 ; i < N ; i++){
        if(i != 0){ cout << ", "; }
        cout << vec[index] ;
        vec.erase(vec.begin() + index);  // remove vec[K-1]
        if(vec.size() == 0) break;
//;; for(int i=0;i<vec.size();i++){ cout << vec[i] << " "; } cout << endl;
//;; cout << "i:" << i << ",index:" << index << ",size:" << vec.size() << endl;
        index += (K - 1);
//;; cout << "i:" << i << ",index:" << index << ",size:" << vec.size() << endl;
        index %= vec.size();
//;; cout << "i:" << i << ",index:" << index << ",size:" << vec.size() << endl;
    }
    cout << ">" << endl;

    return 0;
}
