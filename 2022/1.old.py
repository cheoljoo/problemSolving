from collections import defaultdict
#import numpy as np

import sys

sn ,sa , sb = input().split()
n = int(sn)
a = int(sa)
b = int(sb)
print(n , a , b)
"""ax+b = n
10 3 2  :  2x + 2 <= 10 
x=1 =>  4 remove  1 2 3 5 6 7 8 9 10 (count 9)
                  ^
x=2 =>  6 remove  1 2 3 5 7 8 9 10  (count 8)
                    ^
x=3 =>  8 remove  1 2 3 5 7 9 10 (count 7)
                      ^
x=4 =>  4 is not a element of set (count 7)
x=5 =>  2*5+2 > 10    the end (count 7)
"""

x = defaultdict(dict)
#x = np.zeros(n)
count = n
for i in range(1 , n+1):
    stridx = str(a*i+b)
    stri = str(i)
    print("element:",i, stri, x[stri])
    if x[stri] != 1 :
        print("x:",stridx, a*i+b , x[stridx])
        if (a*i+b) > n :
            break
        else :
            x[stridx] = 1
            print("set x:",stridx,a*i+b , x[stridx])
            count -= 1
print("count:" , count)
for i in range(1 , n+1):
    stridx = str(i)
    print("x:",i, x[stridx])
