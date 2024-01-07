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

# search.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find max location or min location in logN
        self.len = len(nums)
        self.nums = nums
        start = 0
        end = len(nums)-1
        if start == end:
            minIndex = 0
        else :
            minIndex = 0
            while nums[start] >= nums[end]:
                mid = (start+end)//2
                if start+1 == end:
                    if nums[start] > nums[end]:
                        minIndex = end
                        break
                    else :
                        print("error")
                if nums[0] < nums[mid]: # right
                    start = mid
                else : # left
                    end = mid
        self.minIndex = minIndex
        
        start = 0
        end = len(nums)-1
        if start == end:
            if nums[start] == target:
                return 0
            else :
                return -1
        else :
            index = -1
            while True :
                mid = (start+end)//2
                if start+1 == end:
                    if self.newValue(start) == target:
                        return (start + self.minIndex) % self.len
                    elif self.newValue(end) == target:
                        return (end + self.minIndex) % self.len
                    else :
                        return -1
                midV = self.newValue(mid)
                if target ==  midV :
                    return (mid + self.minIndex) % self.len
                elif target < midV :
                    end = mid
                else :
                    start = mid
        return index
        
    def newValue(self,i:int)->int:
            return self.nums[(i + self.minIndex) % self.len]    
           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.search(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , s1 , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='search.py',
        description=
        'search'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('search problem :')

    run([0,1,2,4,5,6,7],2,2)
    run([0,1,2,4,5,6,7],5,4)
    run([0,1,2,4,5,6,7],7,6)
    run([0,1,2,4,5,6,7],3,-1)
    run([0,1,2,4,5,6,7],8,-1)
    run([4,5,6,7,0,1,2],0,4)
    run([3,3,4,5,6,7,0,3,3],0,6)
    run([4,5,6,7,0,1,2],3,-1)
    run([1],0,-1)
    run([3],3,0)
    run([1,2],0,-1)
    run([2,1],0,-1)