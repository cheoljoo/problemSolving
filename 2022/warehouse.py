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

# warehouse.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def warehouse(self, n: int) -> List[int]:
        r = []
        for i in range(n+1):
            count = 0
            while i:
                i &= i - 1
                count += 1
            r.append(count)
        return r

           
def run(s,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.warehouse(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='warehouse.py',
        description=
        'warehouse'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('warehouse problem :')

    run(8,[3,3])