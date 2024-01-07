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

# twoCitySchedCost.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            diff.append([abs(costs[i][0]-costs[i][1]),costs[i][0],costs[i][1]])
        diff.sort(key=lambda x: x[0])
        ret = 0 
        N = len(costs)//2
        countA = 0
        countB = 0
        for v in reversed(diff):
            if countA == N :
                ret += v[2]
                continue
            elif countB == N :
                ret += v[1]
                continue
            else :
                if v[1] > v[2]  :
                    ret += v[2]
                    countB += 1
                else :
                    ret += v[1]
                    countA += 1
        return ret

           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.twoCitySchedCost(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='twoCitySchedCost.py',
        description=
        'twoCitySchedCost'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('twoCitySchedCost problem :')

    run([[10,20],[30,200],[400,50],[30,20]], 110)
    run([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]],1859)
    run([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]],3086)
    