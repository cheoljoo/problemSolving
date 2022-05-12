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

# permuteUnique.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.check = set()
        nums.sort()
        self.go(0,nums)
        return self.ans
    def go(self,start,nums):
        if start == len(nums)-1 :
            if tuple(nums) not in self.check:
                self.check.add(tuple(nums))
                self.ans.append(nums)
            return
        self.go(start+1,nums)
        for i in range(start+1,len(nums)):
            if nums[start] != nums[i]:
                n = nums.copy()
                n[start],n[i] = n[i],n[start]
                self.go(start+1,n)
        

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.permuteUnique(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    flag = True
    if len(r) != len(expect):
        flag = False
    for lis in r:
        if lis not in expect:
            flag = False
    if flag:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='permuteUnique.py',
        description=
        'permuteUnique'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('permuteUnique problem :')


    run([1,1,2],[[1,1,2],
 [1,2,1],
 [2,1,1]])
    run([1,2,3],[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    run([-10],[[-10]])
    run([1,1],[[1,1]])