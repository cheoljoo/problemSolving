from collections import defaultdict
from re import A
#import numpy as np

import sys
import argparse
import math
import random
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import time

# maxScoreIndices.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = nums.copy()
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                zeros[i] = count
            else :
                zeros[i] = count
                
        ones = nums.copy()    
        count = 0
        for i in reversed(range(len(nums))):
            if nums[i] == 1:
                count += 1
                ones[i] = count
            else :
                ones[i] = count
        
        max = 0       
        maxCount = 1
        m = nums.copy()
        m.append(0)
        for i in range(len(m)):
            if i == 0:
                divisionScore = 0 + ones[0]
            elif i == len(nums):
                divisionScore = zeros[i-1] + 0
            else :
                divisionScore = zeros[i-1] + ones[i]
            if max < divisionScore :
                max = divisionScore
                maxCount = 1
            elif max == divisionScore :
                maxCount += 1
            m[i] = divisionScore
        r = []
        for i in range(len(m)):
            if max == m[i]:
                r.append(i)
        return r 

def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.maxScoreIndices(s)
    print("  total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , ":" , s , end="")  
    print()

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='maxScoreIndices.py',
        description=
        'maxScoreIndices'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maxScoreIndices problem :')

    s = [0,0,1,0]
    run(s,[2,4])
    s = [0,0,0]
    run(s,[3])
    s = [1,1]
    run(s,[0])


    

