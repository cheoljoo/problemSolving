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

# burstBallon.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def burstBallon(self, nums: List[int]) -> int:
        forward = {}
        backward = {}
        mn = math.inf
        oldMn = mn
        for i in nums:
            forward[i] = min(mn,oldMn)
            mn = forward[i]
            oldMn = i
        print('forward:',forward)
        mn = math.inf
        oldMn = mn
        for i in reversed(nums):
            backward[i] = min(mn,oldMn)
            mn = backward[i]
            oldMn = i
        print('backward:',backward)
        count = 0
        for i in nums:
            if backward[i] < i and forward[i] < i:
                pass
            else :
                count += 1
        return count

        # split l .. highest , highest+1 .. r+1
         
           
def run(s,expect):
    print(s,end="")
    start = time.time()
    A = Solution()
    r = A.burstBallon(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='burstBallon.py',
        description=
        'burstBallon'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('burstBallon problem :')

    run([-16,27,65,-2,58,-92,-71,-68,-61,-33],6)
    run([9,-1,-5],3)
