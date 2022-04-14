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

# coalTar.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def coalTar(self, nums: List[int]) -> int:
        # 0. 양쪽 안 쓰는 부분 날리기
        l = math.inf
        r = -1
        highest = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                l = i-1
                break
        if l == math.inf:
            return 0
        for i in reversed(range(1,len(nums))):
            if nums[i-1] < nums[i]:
                r = i
                break
        if r == -1:
            return 0
        nums = nums[l:r+1]

        # 마지막 max index 구하기  : mx2Index , mx2
        mx1Index = math.inf
        mx2Index = math.inf
        mx1 = -math.inf
        mx2 = -math.inf
        for i in range(len(nums)):
            if mx2 <= nums[i]:
                mx2Index = i
                mx2 = nums[i]
        # 첫번째 max index 구하기  : mx1Index , mx1
        for i in range(len(nums)):
            if mx2 == nums[i]:
                mx1Index = i
                mx1 = nums[i]
                break

        # 1. 첫번째 max 값의 왼쪽 부분
        lmx = nums[0]
        sum = 0
        for i in range(mx1Index):
            if lmx < nums[i]:
                lmx = nums[i]
            else :
                diff = lmx - nums[i]
                sum += diff

        # 2. 양 max값의 사이  (첫번째 max 값 ~  마지막 max값) 
        lmx = nums[mx1Index]
        for i in range(mx1Index,mx2Index):
            diff = lmx - nums[i]
            sum += diff

        # 3. 마지막 max값 오른쪽
        lmx = nums[-1]
        for i in reversed(range(mx2Index,len(nums))):
            if lmx < nums[i]:
                lmx = nums[i]
            else :
                diff = lmx - nums[i]
                sum += diff
            

        return sum 

        # split l .. highest , highest+1 .. r+1
         
           
def run(s,expect):
    print(s,end="")
    start = time.time()
    A = Solution()
    r = A.coalTar(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='coalTar.py',
        description=
        'coalTar'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('coalTar problem :')

    run([1,2,3,5,7,9,4,3,5,7,15,14,12,9,5,3,6,5,8,15,9,4,5,8,5,4,2],82)
