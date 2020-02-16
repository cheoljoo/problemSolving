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
#include <string.h>
 
using namespace std;

// webcolors.h
#define WEBRED   0xFF0000

int webcolor = WEBRED;   // should be 0xFF0000

enum class ColourScoped{
  red,
  blue,
  green
};

void useMe(ColourScoped color){

  switch(color){
  case ColourScoped::red:
    std::cout << "ColourScoped::red" << std::endl;
    break;
  case ColourScoped::blue:
    std::cout << "ColourScoped::blue" << std::endl;
    break;
  case ColourScoped::green:
    std::cout << "ColourScoped::green" << std::endl;
    break;
  }
}

enum Day { mon, tue, wed, thu, fri, sat, sun };

Day& operator++(Day& d)
{
    return d = (d == Day::sun) ? Day::mon : static_cast<Day>(static_cast<int>(d)+1);
}

Day today = Day::sat;
Day tomorrow = ++today;


enum class Colour1{
  red,
  blue,
  green
};

enum struct Colour2: char {
  red,
  blue,
  green
};

// enum that takes 16 bits
enum smallenum: int16_t
{
    a,
    b,
    c
};


// color may be red (value 0), yellow (value 1), green (value 20), or blue (value 21)
enum color
{
    red,
    yellow,
    green = 20,
    blue
};

// altitude may be altitude::high or altitude::low
enum class altitude: char
{
     high='h',
     low='l', // C++11 allows the extra comma
};

// the constant d is 0, the constant e is 1, the constant f is 3
enum
{
    d,
    e,
    f = e + 2
};

//enumeration types (both scoped and unscoped) can have overloaded operators
std::ostream& operator<<(std::ostream& os, color c)
{
    switch(c)
    {
        case red   : os << "red";    break;
        case yellow: os << "yellow"; break;
        case green : os << "green";  break;
        case blue  : os << "blue";   break;
        default    : os.setstate(std::ios_base::failbit);
    }
    return os;
}

std::ostream& operator<<(std::ostream& os, altitude al)
{
    return os << static_cast<char>(al);
}

// The cstdint header includes types such as std::int8_t, std::int16_t, std::int32_t, and std::int64_t (as well as unsigned versions that begin with u: std::uint8_t).
#include <cstdint>
enum class Colors : std::int8_t { RED = 1, GREEN = 2, BLUE = 3 };

// Enter nullptr. In C++11, nullptr is a new keyword that can (and should!) be used to represent NULL pointers


int main(int argc,char *argv[])
{
	ios_base::sync_with_stdio(false);


  std::cout <<  static_cast<int>(ColourScoped::red) << std::endl;   // 0
  std::cout <<  static_cast<int>(ColourScoped::red) << std::endl;   // 0

  std::cout << std::endl;

  ColourScoped colour{ColourScoped::red};
  useMe(colour);                                                     // ColourScoped::red

  std::cout << sizeof(Colour1) << std::endl;  // 4
  std::cout << sizeof(Colour2) << std::endl;  // 1

    color col = red;
    altitude a;
    a = altitude::low;

    std::cout << "col = " << col << '\n'
              << "a = "   << a   << '\n'
              << "f = "   << f   << '\n';

}
