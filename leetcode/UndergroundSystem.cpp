#include <map>
#include <string>



using namespace std;

class UndergroundSystem {
public:
    map<int,pair<string,int>> checkin;
    map<pair<string,string>,pair<int,int>> checkout;
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        map<int,pair<string,int>>::iterator f = checkin.find(id);
        if( f == checkin.end()){
            checkin.insert(make_pair(id,make_pair(stationName,t)));
        } else {
            checkin[id].first = stationName;
            checkin[id].second = t;
            //  f->second = t;   it has error : const int can not modify.
            // f->second is pair<sring,int>
            // f->first = id
        }
    }
    
    void checkOut(int id, string stationName, int t) {
        auto p = make_pair(checkin[id].first,stationName);
        auto itco = checkout.find(make_pair(checkin[id].first,stationName));
        if( itco == checkout.end()){
            checkout.insert(make_pair(p,make_pair(t - checkin[id].second,1)));
        } else {
            checkout[p].first += t - checkin[id].second;
            checkout[p].second ++;
        }
    }
    
    double getAverageTime(string startStation, string endStation) {
        auto p = make_pair(startStation,endStation);
        // cout << startStation << " ";
        // cout << endStation << " ";
        // cout << checkout[p].first << " ";
        // cout << checkout[p].second << " ";
        // printf("%f\n",(double) (1.0 * checkout[p].first / checkout[p].second));
        return (1.0 * checkout[p].first / checkout[p].second);
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */