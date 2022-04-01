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


# if sample is 1,1,1,1,1,1,1,1,1,1,1,1,1,1  
# we can not find the direction from mid position.
# so O(N) is the solution in the worst case.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        else :
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