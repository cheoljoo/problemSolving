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

# tvModel.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode
# N*3N*logN
class Solution:
    def tvModel(self, n: int,s :List[List[int]]) -> int:
        count = 0
        while s:
            self.getMaxAndRemove(s)
            count += 1
        return count
    def getMaxAndRemove(self,s):
        p = set()
        indexS = {}
        for i in range(len(s)):
            start,end = s[i]
            p.add(start)
            p.add(end)
            if start not in indexS:
                indexS[start] = []
            indexS[start].append(i)
            if end not in indexS:
                indexS[end] = []
            indexS[end].append(i)
        p = list(p)
        p.sort()
        # print(indexS)
        c = [0 for _ in range(len(p))]  # count
        mx = 0
        mxi = 0
        for start,end in s:
            si = bisect_left(p,start)
            ei = bisect_left(p,end)
            # print(start,end,si,ei)
            for i in range(si,ei+1):
                c[i] += 1
                if mx < c[i]:
                    mx = c[i]
                    mxi = i
        # print(s)
        # print(p)
        # print(c)
        # print(mx,mxi)
        # print(p[mxi])
        if mx == len(s):
            # print(mx , "==" ,len(s))
            s.clear()
            return
        for i in reversed(range(len(s))):
            if s[i][0] <= p[mxi] and p[mxi] <= s[i][1]:
                s.pop(i)
        return

           
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.tvModel(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='tvModel.py',
        description=
        'tvModel'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('tvModel problem :')

    run(4,[[10,15],[15,100],[-10,20],[-15,10]],2)
    run(5,[[10,15],[15,100],[-10,20],[-15,10],[-10,5]],2)
    run(6,[[10,15],[15,100],[-10,20],[-15,10],[-10,5],[-15,-11]],3)
    run(4,[[1,50],[2,50],[3,50],[4,50],[5,50]],1)
