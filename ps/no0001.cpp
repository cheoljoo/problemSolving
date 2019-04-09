
#include <iostream>

#include <algorithm>

#include <vector>



using namespace std;



int tc,N,M,a[205][210];

int _min, ans;



void in()

{

    cin>>N>>M;

    for(int i = 1; i<=N; i++) {

        for(int j = 1; j<=M*2; j++) {

            cin>>a[i][j];

        }

    }

}



void out()

{

    for(int i = 1; i<=N; i++) {

        for(int j = 1; j<=M*2; j++) {

            cout<<a[i][j]<<' ';

        }cout<<endl;

    }

}





long long calc(int idx, int k)

{

    long long r1 = 0;

    long long total_price = 0;

    long long cur_price , cur_coupon;
    long long max_coupon = 0;
    long long max_coupon_price = 0;

    long long min_coupon = 987654321;
    long long min_price = 987654321;

    long long total_coupon =0;

    if(N == 1){ return static_cast<long long>(a[i][idx*2+1]) };

    for(int i = 1; i<=N; i++) {

        cur_price = static_cast<long long>(a[i][idx*2+1]);
        cur_coupon = static_cast<long long>(a[i][idx*2+2]);

        total_price += cur_price;
        if(max_coupon < cur_coupon){
            max_coupon = cur_coupon;
            max_coupon_price = cur_price;
        } else if(max_coupon == cur_coupon){
            max_coupon_price = min(max_coupon_price,cur_price); 
        }

        total_coupon += cur_coupon;

        min_coupon = min(min_coupon, cur_coupon);
        min_price = min(min_price, cur_price);

    }



    // r1 = total_price - min(total_price - max__price, total_coupon - min_coupon);
    r1 = total_price - min(total_price - max_coupon_price, total_coupon - min_coupon);

    cout << "total_price : " << total_price << " ,  totoal_coupon : " <<  total_coupon << "\n";
    cout << "max_coupon_price : " << max_coupon_price << " ,  min_coupon : " <<  min_coupon << "\n";
    cout << "min : total_price - max_coupon_price : " << total_price - max_coupon_price << " ,  total_coupon - min_coupon : " <<  total_coupon - min_coupon << "\n";
    cout << "r1 : " << r1 << "\n";



    return r1;

}



void go()

{

    for(int m = 0; m<M; m++) {

        ans = calc(m,0);

        _min = min(ans,_min);

    }

    cout<<_min<<endl;

}



int main()

{

    ios_base::sync_with_stdio(false);

    cin>>tc;

    while(tc--) {

        _min = 987654321;

        in();

        go();

    }

    return 0;

}
