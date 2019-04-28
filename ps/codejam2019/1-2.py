from collections import defaultdict

import sys

T = int(input())
zeroCount = defaultdict(dict)
zeroCount[0] = 0
A = ord('A')
for i in range(T):
    x, y = input("").split(" ")
    num = int(y)
    #print("The value of x & y are: ",x,y,num)
    rem = num % 8;
    if rem == 0 :
        rem = 8
    str = "%s%d"%(chr(A + rem -1) , int((num-1)/8 + 1))
    #print("str=" , str)
    if x == str :
        print("YES")
    else :
        print("NO")
    


