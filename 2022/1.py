from collections import defaultdict
import numpy as np

import sys
import argparse

#from memory_profiler import profile

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
    @profile
    def __init__(self, n , a , b, debug=0):
        self.debug = debug
        self.n = n
        self.a = a
        self.b = b
        self.x = np.zeros(n+1,dtype=np.int8)

        super().__init__()

        if self.debug :
            print(sys._getframe().f_code.co_name ,":",self.n , self.a , self.b,self.debug)

    @profile
    def get_count(self):
        count = self.n
        for i in range(1 , self.n+1):
            nxt = self.a*i+self.b
            if self.x[i] != 1 :
                if self.debug :
                    print("x:",i , ", x[i]:",self.x[i])
                if nxt > self.n :
                    break
                else :
                    self.x[nxt] = 1
                    if self.debug :
                        self.print_set()
                    count -= 1

        if self.debug :
            print("result : ",end="")
        print(count)

    def print_set(self):
        if self.debug :
            print("set elements : ",end="")
            for i in range(1 , self.n+1):
                if self.x[i] == 0 :
                    print(i,end=" ")
            print()

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

    sn ,sa , sb = input().split()
    n = int(sn)
    a = int(sa)
    b = int(sb)

    count_obj = CountAntiSet(n,a,b,debug)
    count_obj.get_count()

