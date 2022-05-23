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

# coinChange.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode
# https://leetcode.com/problems/coin-change/discuss/2061340/Python-Bruteforce-searh-%2B-few-optimizations-greater-99-time-99-space-(strangely)

class Solution:
    def __init__(self):
        self.count = 0
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ math.inf for _ in range(amount + 1) ]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],1 + dp[i-coin])
        return -1 if dp[-1] == math.inf else dp[-1] 
           
def run(s,s1,expect):
    print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.coinChange(s,s1)
    print(" count:",A.count," total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='coinChange.py',
        description=
        'coinChange'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('coinChange problem :')

    run([1,2,5],11,3)
    run([2],3,-1)
    run([1],0,0)
    run([186,419,83,408],6249,20)
    run([1,4,6,9,15,45,32,24,19],9900,220)
    run([411,412,413,414,415,416,417,418,419,420,421,422],9864,24)
    run([346,29,395,188,155,109],9401,26)
    run([429,171,485,26,381,31,290],8440,20)
    run([88,227,216,96,209,172,259],6928,28)
    run([271,5,343,254,112],4853,17)
    run([1,412,413,414,415,416,417,418,419,720,4,6000],9864,15)
    run([265,398,46,78,52],7754,25)
    run([1,412,413,414,415,416,417,418,419,720,4,6000,300,313,43,44,45,56,57,58,99,88,77,66,55],9864,9)
    run([2,4,6,8,10,12,14,16,18,20,22,24],9999,-1)
    