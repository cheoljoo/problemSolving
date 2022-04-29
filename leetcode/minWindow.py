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
        self.minCount = [math.inf,0,0]
        self.loc = {}
        
        for i in range(len(s)):
            v = s[i]
            if v in self.loc:
                self.loc[v].append(i)
            else :
                self.loc[v] = [i]
        self.targets = {}
        for i in range(len(t)):
            v = t[i]
            if v in self.targets:
                self.targets[v][0] += 1
            else :
                if v in self.loc:
                    self.targets[v] = [1,self.loc[v]]
                else:
                    return ""
        # self.loc['A'] = [1,2]  # 전체를 set하면 그것만 변경
        # self.loc['B'][0] = -1  # 내부의 한개만 변경하면 같이 변경됨.
        self.t = []
        for i,target in enumerate(self.targets.keys()):
            self.t.append([self.targets[target][0] , len(self.targets[target][1]), self.targets[target][1]])
            if self.targets[target][0] > len(self.targets[target][1]):
                return ""
        # print(self.t)
        self.loop(0,len(self.targets),0,0)
        return s[self.minCount[1]:self.minCount[2]+1]
    def loop(self,r,mx,f,t):
        if r == mx:
            if self.minCount[0] > t - f:
                self.minCount[0] = t - f
                self.minCount[1] = f
                self.minCount[2] = t
            return
        if t - f > self.minCount[0]:
            return
        for i in range(self.t[r][1]-self.t[r][0]+1):
            size = self.t[r][0]
            start = self.t[r][2][i]
            end = self.t[r][2][i+size-1]
            if r != 0:  # check f,t
                if start > f :
                    start = f
                if end < t :
                    end = t
            self.loop(r+1,mx,start,end)


           
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

    run("a","b","")
    run("ADOBECAODABEABDANCBAC","ABCCDAA","ABDANCBAC")
    run("ADOBECODEBANC","ABC","BANC")
    run("a","a","a")
    run("a","aa","")