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

# maximumSubsequenceCount.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        size1 = []
        size2 = []
        count = 0
        text = list(text)
        if pattern[0] != pattern[1]:
            for ch in reversed(text):
                if ch == pattern[1] :
                    count += 1
                elif ch == pattern[0] :
                    size1.append(count)
                    size2.append(count+1)
            size1.append(count)
            return max(sum(size1),sum(size2))
        else :
            sum1 = 0
            count = 0
            for ch in reversed(text):
                if ch == pattern[1] :
                    count += 1
                    sum1 += count
            return sum1
            

           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.maximumSubsequenceCount(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maximumSubsequenceCount.py',
        description=
        'maximumSubsequenceCount'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maximumSubsequenceCount problem :')

    run("rrr","rr",6)
    run("abdcdbc","ac",4)
    run("aabb","ab",6)
    run("abbcccccaaaa","ac",10)