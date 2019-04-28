#include <iostream>
#include <set>

using namespace std;

int main ()
{
  std::set<int> myset;
  std::set<int>::iterator itlow,itup;

  for (int i=1; i<10; i++) myset.insert(i*10); // 10 20 30 40 50 60 70 80 90

  itlow=myset.lower_bound (30);                //       ^
  std::cout << "30 itlow:" << *itlow << endl;
  itlow=myset.lower_bound (31);                //       ^
  std::cout << "31 itlow:" << *itlow << endl;
  itup=myset.upper_bound (60);                 //                   ^
  std::cout << "60 itup:" << *itup << endl;
  itup=myset.upper_bound (65);                 //                   ^
  std::cout << "65 itup:" << *itup << endl;

  myset.erase(itlow,itup);                     // 10 20 70 80 90

  std::cout << "myset contains:";
  for (std::set<int>::iterator it=myset.begin(); it!=myset.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';

  return 0;
}
