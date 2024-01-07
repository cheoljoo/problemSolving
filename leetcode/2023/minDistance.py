from collections import defaultdict
from collections import Counter
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

# minDistance.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.mem = {}
        self.word1 = word1
        self.word2 = word2
        self.count = 0
        return self.dp(0,0)
    def dp(self,s1,s2) -> int:
        if (s1,s2) in self.mem:
            return self.mem[(s1,s2)]
        self.count += 1
        if s1 == len(self.word1) and s2 == len(self.word2):
            self.mem[(s1,s2)] = 0
            return 0
        elif s1 == len(self.word1) :  # s2 < len
            self.mem[(s1,s2)] = len(self.word2) - s2
        elif s2 == len(self.word2) :  # s1 < len
            self.mem[(s1,s2)] = len(self.word1) - s1
        else :
            if self.word1[s1] == self.word2[s2]:
                self.mem[(s1,s2)] = self.dp(s1+1,s2+1)
            else :
                self.mem[(s1,s2)] = 1 + min(self.dp(s1+1,s2+1),self.dp(s1,s2+1),self.dp(s1+1,s2))
        return self.mem[(s1,s2)]

def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.minDistance(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s,s1 , A.count, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minDistance.py',
        description=
        'minDistance'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minDistance problem :')

    run("horse", "ros",3)
    run("intention", "execution",5)