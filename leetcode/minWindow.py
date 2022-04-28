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

timeFlag = 0
debugFlag = 0
import math


# minWindow.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode
# make dictionary of index of s , t
# self.loc (s) , self.target (t) 
# 1. check length of charater in target
#   it chooses the length of characters
# 2. search all combination.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        self.loc = {}
        for i in range(len(s)):
            v = s[i]
            if v in self.loc:
                self.loc[v].append(i)
            else :
                self.loc[v] = [i]
        self.target = {}
        for i in range(len(t)):
            v = t[i]
            if v in self.target:
                self.target[v].append((i,self.loc[v]))
            else :
                self.target[v] = ([i],self.loc[v])
        self.loc['A'] = [1,2]
        self.loc['B'][0] = -1
        # for target in self.target.keys():
        #     targetLength = self.target[target].len()
        #     go ()
        # go()
        return ""

           
def run(s,t,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.minWindow(s,t)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minWindow.py',
        description=
        'minWindow'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minWindow problem :')

    run("ADOBECODEBANC","ABC","BANC")
    run("a","a","a")
    run("a","aa","")