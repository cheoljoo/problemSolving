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

timeFlag = 0
debugFlag = 0
import math

# plant_trees.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def plant_trees(self, total , A,B) : 
        self.mem = {}
        tree = 0
        # binary search
        start , end = 0,total
        mid = -1
        mx = 0
        while (start + end) // 2 != mid:
            mid = (start + end) // 2
            # find left or right
            t = self.getTreesAB(mid,A,total-mid,B)
            mx = max(mx,t)
            for i in range(1,end-start):  # end-start
                if mid-i >= 0 : 
                    left = self.getTreesAB(mid-i,A,total-mid+i,B)
                    mx = max(mx,left)
                    if t < left : # go left
                        end = mid - i  # i 
                        break
                if mid+i <= total : 
                    right = self.getTreesAB(mid+i,A,total-mid-i,B)
                    mx = max(mx,right)
                    if t < right : # go left
                        start = mid + i
                        break
        return mx



    def getTreesAB(self,ta,A,tb,B):
        if (ta,tb) in self.mem:
            return self.mem[(ta,tb)]
        sumA ,sumB = 0,0
        for v in A:
            sumA += ta // v
        for v in B:
            sumB += tb // v
        ans = min(sumA,sumB)
        self.mem[(ta,tb)] = ans
        return ans
            




           
def run(s,s1,s2,expect):
    print(s,end="")
    start = time.time()
    A = Solution()
    r = A.plant_trees(s,s1,s2)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='plant_trees.py',
        description=
        'plant_trees'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:   
        debug = 0

    print('plant_trees problem :')

    run(35,[4,6,5],[3,2],12)
    run(1,[1,1],[1,1,1],0)
    run(2,[1,1],[1,1,1],2)
    run(100000,[4,5,6,7,8,3,4],[1,4,5,6,8,2],0)
