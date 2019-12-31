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
 
int N,K;

int main(int argc,char *argv[])
{
    std::vector<int> vec;

	ios_base::sync_with_stdio(false);
    
    scanf("%d %d", &N,&K);

    int temp;
	for(int i = 0 ; i < N ; i++){
        scanf("%d",&temp);
        vec.push_back(temp);
    }

//;; for(int i=0;i<vec.size();i++){ cout << vec[i] << " "; } cout << endl;
//;; cout << "N:" << N << ",K:" << K << endl;

    double min = -1;
    double sd = 0.0;
    long squareSum = 0;
    long sum = 0;
	for(int j = 0 ; j < K ; j++){
        squareSum += vec[j] * vec[j];
        sum += vec[j];
    }
    min = sqrt((double) squareSum / (double) K - ((double) sum / (double) K)*((double) sum/(double) K));
    //cout << "[0]squareSum:" <<  squareSum << endl;
    //cout << "[0]sum:" <<  sum << endl;
    //cout << "[0]min:" <<  min << endl;

	for(int i = 1 ; i < (N -K +1) ; i++){
        squareSum -= vec[i-1] * vec[i-1];
        squareSum += vec[i+K-1] * vec[i+K-1];
        sum -= vec[i-1];
        sum += vec[i+K-1];
        sd = sqrt((double)squareSum / (double)K - ((double)sum / (double)K)*((double)sum/(double)K));
        //cout << "[" << i << "]squareSum:" <<  squareSum << endl;
        //cout << "[" << i << "]sum:" <<  sum << endl;
        //cout << "[" << i << "]sd:" <<  sd << endl;
        if(sd < min) { min = sd; }
    }

    printf("%.7f",min);
    return 0;
}
