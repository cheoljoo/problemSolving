from collections import defaultdict
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

# numberOfArithmeticSlices.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        if len(nums) < 3:
            return 0
        for start in range(len(nums)-2):
            diff = nums[start+1] - nums[start]
            for count in range(start+2,len(nums)):
                if (nums[count] - nums[count-1]) == diff : # success
                    result += 1
                else : 
                    break
        return result
        
            
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.numberOfArithmeticSlices(s)
    print(" , total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print("len:%d"%len(s), r , ": " , end="")  
    print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='numberOfArithmeticSlices.py',
        description=
        'numberOfArithmeticSlices'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('numberOfArithmeticSlices problem :')

    s = [1,2,3,4]
    run(s,3)
    s = [1]
    run(s,0)
    s = [1,3,4]
    run(s,0)
    s = [1,2,3]
    run(s,1)
    s = [2,1,2,3,4]
    run(s,3)
    
    


# Great Code : Time: O(n)  Space: O(n) for cache
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         @cache
#         def count(n):
#             if cnt < 3: return 0
#             return n - 2 + count(n - 1)
        
#         prev, cnt, ans = None, 2, 0
#         for i in range(1, len(nums)):
#             diff = nums[i-1] - nums[i]
#             if diff == prev:
#                 cnt += 1
#             else:
#                 ans += count(cnt)
#                 cnt = 2
                
#             prev = diff
            
#         return ans + count(cnt)