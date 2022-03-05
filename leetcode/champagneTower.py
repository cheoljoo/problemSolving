from collections import defaultdict
import enum
from re import A
#import numpy as np

import sys
import argparse
import math
import random
from tkinter import N
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import time

# champagneTower.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0 :
            return 0.0
        # max of row and glass is 100
        # 2**100 is about  10**30
        # ln = [[0] * 101] * (query_row+1)
        ln = [[0 for c in range(101)] for r in range(query_row+1)]
        ln[0][0] = poured  # row (level) , glass
        # f(L,n) = ( f(L-1,n-1) + f(L-1,n) ) / 2   
        # f(0,0) = 1
        # f(L,0) = f(L,L) = 1 / 2**L
        for row in range(1,query_row+1):
            if ln[row-1][0] - 1 > 0 :
                ln[row][0] = (ln[row-1][0] - 1)/2
            if ln[row-1][row-1] - 1 > 0 :
                ln[row][row] = (ln[row-1][row-1] - 1)/2
            for glass in range(1,row):
                leftFlow = 0.0
                rightFlow = 0.0
                if ln[row-1][glass-1] - 1 > 0 :
                    leftFlow = (ln[row-1][glass-1] -1)/2
                if ln[row-1][glass] - 1 > 0 :
                    rightFlow = (ln[row-1][glass] -1)/2
                ln[row][glass] =  leftFlow + rightFlow
        
        if ln[query_row][query_glass] >= 1.0 :
            return 1.0
        return ln[query_row][query_glass]

           
def run(s,s1,s2,expect):
    start = time.time()
    A = Solution()
    r = A.champagneTower(s,s1,s2)
    print(" total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print( r , ": " , end="")  
    print(s ,s1,s2, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='champagneTower.py',
        description=
        'champagneTower'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('champagneTower problem :')

    run(1,1,1,0.0)
    run(2,1,1,0.5)
    run(100000009,33,17,1.0)
    
    
# algorithm
# ```
# f(L,n) = ( f(L-1,n-1) + f(L-1,n) ) / 2   
# f(0,0) = 1
# f(L,0) = f(L,L) = 1 / 2**L


# f(1,0) = 1/2  , f(1,1) = 1/2
# f(2,0) = 1/4 , f(2,1) = (f(1,0)+f(1,1))/2 = 2/4
# f(3,0) = 1/8 , f(3,1) = (f(2,0)+f(2,1))/2 = 3/8

# we can calulate with only integer.  
# we can predict that denominator is 2**L with Level L.

# (L=33,n=17) = 32,16 and 32,17 should be full. 
# ```