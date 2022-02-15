import numpy as np
import math
 
 
if (__name__ == "__main__"):
 
    #a = 3
    #b = 4
    log = False
    cal = [0, 1]
 
    nn = int(input())
    out = np.arange(nn)
 
    for i in range(nn):
        if log: print(i)
 
        a, b, n, m = map(int, input().split())
        x = n
        if n < m: x = m
        for j in range(2,x+1):
            y = a*cal[j-1] + b*cal[j-2]
            cal.append(y)
 
        if log: print(cal)
        out[i] = math.gcd(cal[n], cal[m])
        if log: print(out)
 
        for j in range(2, x+1): cal.pop()
        if log: print(cal)
 
    for i in range(nn): print(out[i])