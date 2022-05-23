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

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.ans = math.inf
        self.coins = coins
        self.count = 0
        self.dp = {}
        self.go(0,amount,0)
        print("count",self.count,"",end="")
        if self.ans == math.inf:
            return -1
        return self.ans
    def go(self,s,amount,count):
        if s == len(self.coins) : 
            return 0
        if amount % self.coins[s] == 0:
            self.ans = min(self.ans,count+amount//self.coins[s])
            return 1
        if amount == 0:
            self.ans = min(self.ans,count)
            return 1
        if self.ans <= count:
            return 1
        N = amount // self.coins[s]
        self.changeFlag = 0
        self.count += 1
        if self.count % 1000000 == 0: print(":",self.count,s,count,end="")
        for i in reversed(range(N+1)):
            if (s+1,amount - i*self.coins[s]) not in self.dp:
                t = self.go(s+1,amount - i*self.coins[s],count + i)
                if t == 0:
                    self.dp[(s+1,amount - i*self.coins[s])] = 0
                else : 
                    self.changeFlag = 1
            # t = self.go(s+1,amount - i*self.coins[s],count + i)
        return self.changeFlag
        return 0
           
def run(s,s1,expect):
    print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.coinChange(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
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
    