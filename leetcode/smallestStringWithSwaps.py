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

# smallestStringWithSwaps.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        self.ans = s
        sortedList = s.copy()
        sortedList.sort()
        pairsList = []
        checkDuplicatePairs = set()
        for p in pairs:
            if p[0] < p[1]:
                a = p[0]
                b = p[1]
            else :
                a = p[1]
                b = p[0]
            if (a,b) not in checkDuplicatePairs:
                    checkDuplicatePairs.add((a,b))
                    pairsList.append([a,b])
            
        self.ansScore = self.answerScore(s,sortedList)
        for i in range(len(pairsList)):
            p = pairsList[i]
            if ord(s[p[0]]) > ord(s[p[1]]):
                t = s.copy()
                t[p[0]] , t[p[1]] = t[p[1]] , t[p[0]]            
                self.go(t,pairsList,sortedList)
        return "".join(self.ans)
    def go(self,s, pairsList: List[List[int]],sortedList):
        for p in pairsList:
            if ord(s[p[0]]) > ord(s[p[1]]):
                t = s.copy()
                t[p[0]] , t[p[1]] = t[p[1]] , t[p[0]]            
                self.go(t,pairsList,sortedList)
        ansScore = self.answerScore(s,sortedList)
        if self.ansScore > ansScore:
            self.ansScore = ansScore
            self.ans = s
        return 
    def answerScore(self,s,sortedList):
        sum = 0
        for i in range(len(sortedList)):
            sum += abs(ord(s[i])-ord(sortedList[i]))*(10**(len(sortedList)-1-i))
        return sum           
def run(s,p,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.smallestStringWithSwaps(s,p)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='smallestStringWithSwaps.py',
        description=
        'smallestStringWithSwaps'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('smallestStringWithSwaps problem :')

    run("udyyek",[[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]],"deykuy")
    run("qdwyt",[[2,3],[3,2],[0,1],[4,0],[3,2]],"dqwyt")
    run("dcab",[[0,3],[1,2]],"bacd")
    run("dcab",[[0,3],[1,2],[0,2]],"abcd")
    run("cba",[[0,1],[1,2]],"abc")