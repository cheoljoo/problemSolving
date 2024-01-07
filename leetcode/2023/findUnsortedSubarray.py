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

# findUnsortedSubarray.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        startIndex = -1
        lastIndex = -1
        mn = -math.inf
        firstDownFlag = False
        for i,v in enumerate(nums):
            if firstDownFlag == False :
                if mn > v :
                    mn = v
                    firstDownFlag = True
                else :
                    mn = v
            else :
                mn = min(mn,v)
        # 코드 추가 : mn의 위치부터가 시작
        if firstDownFlag == False:
            return 0
        else :
            for i,v in enumerate(nums):
                if mn < v :
                    startIndex = i
                    break
        mx = math.inf      
        firstDownFlag = False
        for i in reversed(range(len(nums))):
            if firstDownFlag == False :
                if mx < nums[i] :
                    mx = nums[i]
                    firstDownFlag = True
                else :
                    mx = nums[i]
            else : 
                mx = max(mx,nums[i])
        if firstDownFlag == False:
            return 0
        else :
            for i in reversed(range(len(nums))):
                if mx > nums[i] :
                    lastIndex = i
                    break
        print(" : " , mn , startIndex , mx , lastIndex)
        return lastIndex - startIndex +1 
            
            

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.findUnsortedSubarray(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='findUnsortedSubarray.py',
        description=
        'findUnsortedSubarray'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('findUnsortedSubarray problem :')

    run([2,6,4,8,10,9,15],5)
    run([2,4,6,3,8,14,9,13,15],7)
    run([1,2,5,4,7],2)
    run([1,2,3,4],0)
    run([1],0)