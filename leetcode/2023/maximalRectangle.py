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

# maximalRectangle.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # make matrix with 0 or 1 , 1's count until the end of 1' row , 1's count until the end of 1's column
        rCount = len(matrix)
        cCount = len(matrix[0])
        m = []
        ans = 0
        for i in range(rCount+1):
            m.append([[0,0,0,0] for _ in range(cCount+1)])
        for r in reversed(range(rCount)):
            for c in reversed(range(cCount)):
                if matrix[r][c] == '1':
                    m[r][c][0] = 1
                    m[r][c][1] = m[r+1][c][1] + 1 # 1's count until the end of 1's row
                    m[r][c][2] = m[r][c+1][2] + 1 # 1's count until the end of 1's column
        for r in range(rCount):
            for c in range(cCount):
                subMaxRec = 0
                subMinXSize = math.inf
                subMaxYSize = m[r][c][1]
                for YSize in range(subMaxYSize):
                    if r == 2 :
                        r= 2
                    if subMinXSize > m[r+YSize][c][2]:
                        subMinXSize = m[r+YSize][c][2]
                    if subMaxRec < (YSize+1)*subMinXSize:
                        subMaxRec = (YSize+1)*subMinXSize
                m[r][c][3] = subMaxRec
                if ans < subMaxRec:
                    ans = subMaxRec
        return ans

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.maximalRectangle(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maximalRectangle.py',
        description=
        'maximalRectangle'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maximalRectangle problem :')

    run([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],6)
    run([["0"]],0)
    run([["1"]],1)