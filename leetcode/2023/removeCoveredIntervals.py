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

# removeCoveredIntervals.py

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        s = sorted(intervals, key=lambda x: x[0]*10**6-x[1])
        for i in reversed(range(len(s))):
            targetList = s[i]
            for ii in range(i):
                ll = s[ii]
                if ll[1] >= targetList[1]:
                    count -= 1
                    break
        return count

def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.removeCoveredIntervals(s)
    print("  total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(%d) -> "%expect,end="")
    print(r , ":" , s , end="")
    p = sorted(s, key=lambda x: x[0]*10**6-x[1])   
    print(" sorted:",p)

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='removeCoveredIntervals.py',
        description=
        'removeCoveredIntervals'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('removeCoveredIntervals problem :')

    s = [[1,4],[3,6],[3,7],[2,8],[2,7]]
    run(s,2)
    s = [[1,4],[2,3]]
    run(s,1)
    s = [[3,10],[4,10],[5,11]]
    run(s,2)


    

