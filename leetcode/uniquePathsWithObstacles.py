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

# uniquePathsWithObstacles.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def __init__(self):
        self.count = 0
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DFS를 갈때 return 값으로 1 이면 , 이 값을 해당 (i,j)에 1로 set
        # 갈때 1이면 끝까지 갈수 있다고 판단하면됨.
        # 0이면 Down/Right로 간다. 그래서 , (len-1,len-1)에 도달하면 1 return
        self.ans = 0
        v = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]  # visited (how many path from here to target)
        self.u = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]  # unreached
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]:
            return 0
        self.dfs(0,0,obstacleGrid,v)
        print(self.count)
        return self.ans
    def dfs(self,r,c,o,v):
        self.count += 1
        t1 = 0
        t2 = 0
        if r == len(o)-1 and c == len(o[0])-1 and o[r][c] == 0:
            self.ans += 1
            v[r][c] = 1
            return 1
        if c+1 < len(o[0]) and o[r][c+1] == 0:
            flag1 = 1
            if v[r][c+1] != 0 or self.u[r][c+1] == 1:
                self.ans += v[r][c+1]
                v[r][c] += v[r][c+1]
                t1 = v[r][c+1]
            else:
                t1=self.dfs(r,c+1,o,v)
                v[r][c] += t1
        if r+1 < len(o) and o[r+1][c] == 0:
            flag2 = 1
            if v[r+1][c] != 0 or self.u[r+1][c] == 1:
                self.ans += v[r+1][c]
                v[r][c] += v[r+1][c]
                t2 = v[r+1][c]
            else:
                t2 = self.dfs(r+1,c,o,v)
                v[r][c] += t2
        if t1+t2 == 0:
            self.u[r][c] = 1
        return t1+t2

           
def run(s,expect):
    print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.uniquePathsWithObstacles(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s ,A.count, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='uniquePathsWithObstacles.py',
        description=
        'uniquePathsWithObstacles'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('uniquePathsWithObstacles problem :')

run([[0,0,0],[0,1,0],[0,0,0]],2)
run([[0,1],[0,0]],1)
run([[0]],1)
run([[1]],0)
run([[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0]],6)
run([[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,1,0,0]],10)
run([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]],4)