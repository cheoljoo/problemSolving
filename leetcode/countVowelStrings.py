from collections import defaultdict
from collections import Counter
from collections import deque
import collections
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
import heapq
from bisect import bisect_left , bisect_right

timeFlag = 0
debugFlag = 0
import math

# countVowelStrings.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # fn(0) = 1
        # f1(1) = 1
        # f1(n) = 1
        # f2(1) = 2
        # f2(n) = f2(n-1) + f1(n-1)
        # f3(n) = f3(n-1) + f2(n-1) + f1(n-1)
        # f5(n) = f5(n-1) + f4(n-1) + f3(n-1) + f2(n-1) + f1(n-1)
        # n = 1 => a:1 + e:1 + i:1 + o:1 + u:1
        # n = 2 => a:5 + e:4 + i:3 + o:2 + u:1 => a:f5(1) + e:f4(1) + i:f3(1) + o:f2(1) + u:f1(1)
        # n = 3 => a:f5(2) + e:f4(2) + i:f3(2) + o:f2(2) + u:f1(2)
        if n == 1:
            return 5
        f = {}
        for i in range(1,5+1): # aeiou
            f[i] = {}
            f[i][1] = i
        for nn in range(2,n+1):
            for i in range(1,5+1):
                sum = 0
                for k in range(1,i+1):
                    sum += f[k][nn-1]
                f[i][nn] = sum
        return f[5][n]

           
def run(s,expect):
    # print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.countVowelStrings(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='countVowelStrings.py',
        description=
        'countVowelStrings'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('countVowelStrings problem :')

    run(1,5)
    run(2,15)
    run(3,10)
    run(33,66045)