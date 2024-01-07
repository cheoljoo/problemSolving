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
import bisect

timeFlag = 0
debugFlag = 0
import math

# maxSlidingWindow.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        lidx = 0
        if len(nums) == 1 or k == 1:
            return nums
        for i in range(len(nums)-k+1):
            if i == 0:
                mx = max(nums[:k])
            else :
                if mx == nums[i-1]:
                    if mx <= nums[i+k-1]:
                        mx = nums[i+k-1]
                    else :
                        mx = max(nums[i:i+k]) # it makes timeout when we do frequently.
                        # lidx = bisect.bisect_left(nums[i:i+k],mx)
                        # print("T" , i,lidx,mx)
                        #
                        # mx = -math.inf
                        # lidx = 0
                        # for x in range(i,i+k):
                        #     if mx < nums[x]:
                        #         mx = nums[x]
                        #         lidx = x
                else:
                    if mx < nums[i+k-1]:
                        mx = nums[i+k-1]
            ans.append(mx)
        return ans
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     ans = []
    #     if len(nums) == 1 or k == 1:
    #         return nums
    #     q = []
    #     for i in range(k):
    #         heapq.heappush(q,-1*nums[i])
    #     mx = -1*q[0]
    #     ans.append(mx)
    #     for i in range(1,len(nums)-k+1):
    #         if mx == nums[i-1]:
    #             heapq.heappop(q)  # 이것은 중간중간처리가 안되는 것으로 문제가 있음. avl tree로 관리를 해야 하나?
    #         heapq.heappush(q,-1*nums[i+k-1])
    #         mx = -1*q[0]
    #         ans.append(mx)
    #     return ans


           
def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.maxSlidingWindow(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print( end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maxSlidingWindow.py',
        description=
        'maxSlidingWindow'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maxSlidingWindow problem :')


    run([1,3,-1,-3,5,3,6,7] , 3 , [3,3,5,5,6,7])
    run([1] , 1 , [1])
    run([1,3,-1,-3,5,3,6,7,3,-1,-3,5,13,6,7,3,-1,-13,5,3,6,7,3,-1,-3,5,3,6,17,3,-1,-23,5,23,6,7,3,-1,-3,5,3,6,7,3,-1,-3,5,3,6,7,3,-1,-3,5,3,6,7,3,-1,-3,5,13,6,7] , 10 , [7,7,7,13,13,13,13,13,13,13,13,13,13,7,7,7,7,7,7,17,17,17,17,17,23,23,23,23,23,23,23,23,23,23,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,13,13,13])
    s = list(range(10000,-10000,-1))
    s += list(range(-10000,10000))
    run(s,10007,[])
    s = list(range(10,-10,-1))
    s += list(range(-10,10))
    run(s,7,[])
