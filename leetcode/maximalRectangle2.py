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

# maximalRectangle.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # make matrix with 0 or 1 , 1's count until the end of 1' row , 1's count until the end of 1's column
        rCount = len(matrix)
        cCount = len(matrix[0])
        m = []
        ans = 0
        for i in range(rCount+1):
            m.append([0 for _ in range(cCount+1)])
        for r in range(rCount):
            for c in range(cCount):
                if matrix[r][c] == '1':
                    m[r][c] = m[r-1][c] + 1 # heights from row
                else :
                    m[r][c] = 0
        for r in range(rCount):
            ans = max(ans,self.largestRectangleHistogram(m[r]))
        return ans
    def largestRectangleHistogram(self,heights):
        stack=[]
        right=[0]*len(heights)
        left=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while len(stack)>0 and stack[-1][0]>=heights[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1][1]
            else:
                right[i]=len(heights)
            stack.append([heights[i],i])
        stack=[]
        for i in range(len(heights)):
            while(len(stack)>0 and stack[-1][0]>=heights[i]):
                stack.pop()
            if stack:
                left[i]=stack[-1][1]
            else:
                left[i]=0-1
            stack.append([heights[i],i])
        mx=0
        for i in range(len(heights)):
            mx=max(mx,heights[i]*(right[i]-left[i]-1))
        return mx
        
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.maximalRectangle(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maximalRectangle.py',
        description=
        'maximalRectangle'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maximalRectangle problem :')

    run([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],6)
    run([["0"]],0)
    run([["1"]],1)