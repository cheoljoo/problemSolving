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

# search-Duplicatable.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

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
                    if nums[start] == target:
                        return True
                    elif nums[end] == target:
                        return True
                    else :
                        return False
                if target == nums[mid]:
                    return True
                if nums[0] <= target and target < nums[mid]: # left
                    end = mid
                else : # right
                    start = mid
            return False
        
           
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

    run([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2,True)
    run([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1],2,True)
    run([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2,True)
    run([3,3,3,3,3,3,5,1,1,3,3,3,3],2,False)