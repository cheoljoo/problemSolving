from collections import defaultdict

import sys

T = int(input())
zeroCount = defaultdict(dict)
zeroCount[0] = 0
A = ord('A')
for i in range(T):
    x, y = input("").split(" ")
    x1,x2  = list(x)
    #print("The value of x & y are: ",x,y)
    #print("The value of x & y are: ",int(ord(x1)-A),x2)
    xcolor = (int(ord(x1)-A) + int(x2)) %2
    iy = int(y)-1
    ycolor = (int(iy/8) + (iy%2) + 1) %2
    #print("The color of x & y are: ",xcolor,ycolor)
    if xcolor == ycolor :
        print("YES")
    else :
        print("NO")
    


