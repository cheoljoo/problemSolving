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

# countBits.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

# hamming-weight-bit-count : http://shumin.co.kr/algorithm-hamming-weight-bit-count/
class Solution:
    def countBits(self, n: int) -> List[int]:
        r = []
        for i in range(n+1):
            count = 0
            while i:
                i &= i - 1
                count += 1
            r.append(count)
        return r

class Sol2:
    def countBits(self,n:int) -> List[int]:
        r = [0]
        mem = [0] * (n+1)
        if n == 0:
            return r
        r.append(1)
        if n == 1:
            return r 
        mem[0] = 0
        mem[1] = 1
        exp = 1
        P = 2**(exp-1)
        E = 2**exp
        for i in range(2,n+1):
            if i == E:
                mem[i] = 1
                r.append(1)
                P = E
                exp += 1
                E = 2**exp
            else :
                mem[i] = mem[P] + mem[i-P]
                r.append(mem[i])
        return r
                

           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.countBits(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    start = time.time()
    A = Sol2()
    r2 = A.countBits(s)
    print(" total_time2 :", time.time() - start , "-> ", end="") 
    
    if r2 == r :
        print(" [SAME] ",end="")
    else:
        print(" [DIFF] ",end="")
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print( r , r2,": " , end="")  
    print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='countBits.py',
        description=
        'countBits'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('countBits problem :')

    run(2,[0,1,1])
    run(5,[0,1,1,2,1,2])
    run(100000,[0,1,1,2,1,2])

    
 