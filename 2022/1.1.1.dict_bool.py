from collections import defaultdict
import numpy as np

import sys
import argparse

from memory_profiler import profile
#import requests

""" ax+b = n : hate a and b in set

10 2 2  :  2x + 2 <= 10 
x=1 =>  4 remove  1 2 3 5 6 7 8 9 10 (count 9)
                  ^
x=2 =>  6 remove  1 2 3 5 7 8 9 10  (count 8)
                    ^
x=3 =>  8 remove  1 2 3 5 7 9 10 (count 7)
                      ^
x=4 =>  4 is not a element of set (count 7)
x=5 =>  2*5+2 > 10    the end (count 7)
"""
class CountAntiSet :
    debug = 0

    @profile
    def get_count(self):
        sn ,sa , sb = input().split()
        n = int(sn)
        a = int(sa)
        b = int(sb)
        if debug :
            print(n , a , b,debug)

        x = defaultdict(bool)
        #x = np.zeros(n)
        count = n
        for i in range(1 , n+1):
            nxt = a*i+b
            if debug :
                print("element:",i, x[i])
            if x[i] != True :
                if debug :
                    print("x:",nxt, x[nxt])
                if nxt > n :
                    break
                else :
                    x[nxt] = True 
                    if debug :
                        print("set x:",nxt, a*i+b , x[nxt])
                    count -= 1

        if debug :
            print("result : ",end="")
        print(count)

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='set_ax_b.py',
        description=
        'this set hates a b'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    count_obj = CountAntiSet()
    count_obj.get_count()

