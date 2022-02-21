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

# majorityElement.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def __init__(self):
        self.m = {}
    def majorityElement(self, nums: List[int]) -> int:
        for c in nums:
            if c in self.m:
                self.m[c] += 1
                if self.m[c] > len(nums)//2:
                    return c
            else :
                self.m[c] = 1
            
        for c in self.m:
            if self.m[c] > len(nums)//2:
                return c
            
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.majorityElement(s)
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
        prog='majorityElement.py',
        description=
        'majorityElement'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('majorityElement problem :')

    s = [3,2,3]
    run(s,3)
    s = [2,2,1,1,1,2,2]
    run(s,2)
    s = [1,1,2,2,2]
    run(s,2)
    s = [1,1,2,2,3,3,3,3,3]
    run(s,3)
    s = [1,1,3,3,3,3,3,2,2]
    run(s,3)
    s = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4]
    run(s,4)
    s = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    run(s,3)
    s = [1,2,3,1,2,3,1,2,3,2,2,2,2]
    run(s,2)

    
    
