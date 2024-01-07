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

# longestIncreasingPath.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.rMax = len(matrix)
        self.cMax = len(matrix[0])
        self.visited = [[False for _ in range(self.cMax)] for _ in range(self.rMax)] 
        self.mem = [[0 for _ in range(self.cMax)] for _ in range(self.rMax)]
        long = 0
        for r in range(self.rMax):
            for c in range(self.cMax):
                res = self.dfs(r,c,matrix)
                self.mem[r][c] = max(self.mem[r][c] , res)
                long = max(long , self.mem[r][c])
        return long
    def dfs(self,r,c,matrix):
        if self.mem[r][c]:
            return self.mem[r][c]
        mx = 0
        self.visited[r][c] = True
        v = matrix[r][c]
        if r-1 >= 0 and not self.visited[r-1][c] and v < matrix[r-1][c]:          # north
            # if self.mem[r-1][c] : print(r-1,c,"not 0 =>", self.mem[r-1][c])
            self.mem[r-1][c] = self.dfs(r-1,c,matrix)
            mx = max(mx,self.mem[r-1][c])
        if c-1 >= 0 and not self.visited[r][c-1] and v < matrix[r][c-1]:          # west
            # if self.mem[r][c-1] : print(r,c-1,"not 0 =>", self.mem[r][c-1])
            self.mem[r][c-1] = self.dfs(r,c-1,matrix)
            mx = max(mx,self.mem[r][c-1])
        if r+1 < self.rMax and not self.visited[r+1][c] and v < matrix[r+1][c]:          # south
            # if self.mem[r+1][c] : print(r+1,c,"not 0 =>", self.mem[r+1][c])
            self.mem[r+1][c] = self.dfs(r+1,c,matrix)
            mx = max(mx,self.mem[r+1][c])
        if c+1 < self.cMax and not self.visited[r][c+1] and v < matrix[r][c+1]:          # east
            # if self.mem[r][c+1] : print(r,c+1,"not 0 =>", self.mem[r][c+1])
            self.mem[r][c+1] = self.dfs(r,c+1,matrix)
            mx = max(mx,self.mem[r][c+1])
        self.visited[r][c] = False
        return mx + 1
            
        
    
                

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.longestIncreasingPath(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='longestIncreasingPath.py',
        description=
        'longestIncreasingPath'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('longestIncreasingPath problem :')

    run([[9,9,4],[6,6,8],[2,1,1]],4)
    run([[3,4,5],[3,2,6],[2,2,1]],4)
    run([[1]],1)
    run([[1,2,3],[6,5,4],[7,8,9]],9)