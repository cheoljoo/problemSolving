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

# largestRectangleArea.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def nearestSmallestToLeft(self, data: List[int]):
        self.left = [-1 for _ in range(len(data))]
        old = -1
        s = []
        for i,h in enumerate(data):
            if old < h:
                s.append([h,i])
                self.left[i] = i
            elif old > h:
                if s :
                    li = i
                    # smaller than stack
                    while s[-1][0] > h:
                        lh , li = s.pop()
                        if not s :
                            break
                    # equal
                    if not s : 
                        self.left[i] = 0
                        s.append([h,0])
                    else :
                        if s[-1][0] == h:
                            self.left[i] = s[-1][1]
                        elif s[-1][0] > h :
                            print("error2")
                        else :
                            self.left[i] = li
                            s.append([h,li])
                else :
                    print("error1")
            else :
                self.left[i] = self.left[i-1]
            old = h
        
    def nearestSmallestToRight(self, data: List[int]):
        self.right = [len(data) for _ in range(len(data))]
        old = -1
        s = []
        for i in reversed(range(len(data))):
            h = data[i]
            if old < h:
                s.append([h,i])
                self.right[i] = i
            elif old > h:
                if s :
                    ri = i
                    # smaller than stack
                    while s[-1][0] > h:
                        rh , ri = s.pop()
                        if not s :
                            break
                    # equal
                    if not s : 
                        self.right[i] = len(data)-1
                        s.append([h,len(data)-1])
                    else :
                        if s[-1][0] == h:
                            self.right[i] = s[-1][1]
                        elif s[-1][0] > h :
                            print("error4")
                        else :
                            self.right[i] = ri
                            s.append([h,ri])
                else :
                    print("error3")
            else :
                self.right[i] = self.right[i+1]
            old = h

    def largestRectangleArea(self, heights: List[int]) -> int:
        self.nearestSmallestToLeft(heights)
        self.nearestSmallestToRight(heights)
        mx = 0
        for i,h in enumerate(heights):
            mx = max(mx,h*(self.right[i] - self.left[i]+1))
        return mx

           
def run(s,expect):
    print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.largestRectangleArea(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='largestRectangleArea.py',
        description=
        'largestRectangleArea'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('largestRectangleArea problem :')

    run([3,6,5,7,4,8,1,0],20)
    run([2,1,2],3)
    run([2,1,5,6,2,3],10)
    run([2,4],4)
    run([10,10,5,10,10,20,10,5,3],40)