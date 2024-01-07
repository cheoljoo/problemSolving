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

timeFlag = 0
debugFlag = 0
import math

# isBipartite.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for i in range(len(graph)):
            if len(graph[i]) > 0:
                break
        q = [i]
        BLACK = 1
        WHITE = -1
        curColor = BLACK
        node = [0 for _ in range(len(graph))]
        while q:
            nextQ = []
            for v in q:
                if node[v] == 0:
                    node[v] = curColor
                elif node[v] != curColor:
                    return False
                for nn in graph[v]:
                    if node[nn] == 0:
                        nextQ.append(nn)
            q = nextQ
            if not q:
                flag = -1
                for i in range(len(graph)):
                    if len(graph[i]) > 0 and node[i] == 0:
                        flag = i
                        break
                if flag == -1:
                    return True
                else :
                    q = [flag]
            curColor *= -1
        return True



           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.isBipartite(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='isBipartite.py',
        description=
        'isBipartite'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('isBipartite problem :')

    run([[1,2,3],[0,2],[0,1,3],[0,2]],False)
    run([[1,3],[0,2],[1,3],[0,2]],True)
    run([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]],False)
    run([[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]],False)