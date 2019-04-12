#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
 
using namespace std;
 
 
int main(int argc,char *argv[])
{
std::vector<int> vec;

vec.push_back(1);
vec.push_back(2);
vec.push_back(3);
vec.push_back(4);
vec.push_back(5);
vec.push_back(6);

for(int i=0;i<vec.size();i++){ cout << vec[i] << " "; } cout << endl;

// Deletes the second element (vec[1])
vec.erase(vec.begin() + 1); 
for(int i=0;i<vec.size();i++){ cout << vec[i] << " "; } cout << endl;

vec.erase(vec.begin() + 1); 
for(int i=0;i<vec.size();i++){ cout << vec[i] << " "; } cout << endl;
   
    return 0;
}
