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

# summitMeeting.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

H=987654321
class Solution:
    def __init__(self):
        self.dp = {}
        self.dp[0] = 1
        self.dp[2] = 1
        self.dp[4] = 2
    def handShake(self, i: int) -> int:
        return self.hs(i) % H
    def hs(self,i):
        if i in self.dp:
            return self.dp[i]
        else :
            mx = 0
            r = i-2
            for ii in range(r,-2,-2):
                mx += self.hs(ii) * self.hs(r-ii)
                #print("mx:",mx)
            self.dp[i] = mx
            #print("dp:",i,mx)
            return mx

def run(s,expect):
    print(s,end="")
    start = time.time()
    A = Solution()
    r = A.handShake(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(s, r , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='summitMeeting.py',
        description=
        'summitMeeting'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('summitMeeting problem :')

    run(2,1)
    run(4,2)
    run(6,5)
    run(8,14)
    run(12,132)

