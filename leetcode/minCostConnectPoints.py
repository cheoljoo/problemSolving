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

# - algorithm : 
#   - input length 1000
#     - 1.15.3. Kruskal's Algorithm : find minimum spanning tree
#     - 1.15.4. Prim's Algorithm : find minimum spanning tree
#   - sort by distance
#   - put the same group if two vertices have edge.
#   - use all hash to find faster whether it is in or not.
#   - groupVertex[f] = v   f:vertext number , v : group number
#   - group[v] has hash {from:to} ,  v : group number
#   - if two vertices are in different groups , combine into one.  (delete group of [to])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        if l <= 1:
            return 0
        hq = []
        sum = 0
        for i in range(l):
            mn = math.inf
            loopFrom = -1
            loopTo = -1
            for loop in range(i+1,l):
                distance = abs(points[i][0] - points[loop][0]) + abs(points[i][1] - points[loop][1])
                heapq.heappush(hq,(distance,i,loop))
        
        # grouping for each vertex
        group = {}
        groupVertex = {}
        groupMax = 0
        edgeCount = 0
        dlist = []
        while hq:
            (distance , f,t) = heapq.heappop(hq)
            print(distance,f,t)
            dlist.append((distance , f,t))
            if f not in groupVertex and t not in groupVertex:
                group[groupMax] = {}
                group[groupMax][f] = t
                group[groupMax][t] = f
                groupVertex[f] = groupMax
                groupVertex[t] = groupMax
                groupMax += 1
                edgeCount += 1
                sum += distance
                if edgeCount == l - 1:
                    break
            elif f in groupVertex and t in groupVertex:
                if groupVertex[f] == groupVertex[t]:
                    continue
                else :
                    # all t copy in f
                    d = groupVertex[t]
                    for i in group[d].keys():
                        groupVertex[i] = groupVertex[f]
                        group[groupVertex[f]][i] = -1
                    group[d].clear()
                    edgeCount += 1
                    sum += distance
                    if edgeCount == l - 1:
                        break
            else :
                if f in groupVertex:
                    group[groupVertex[f]][t] = f
                    groupVertex[t] = groupVertex[f]
                elif t in groupVertex:
                    group[groupVertex[t]][f] = t
                    groupVertex[f] = groupVertex[t]
                edgeCount += 1
                sum += distance
                if edgeCount == l - 1:
                    break

            
        return sum

        
def run(s,expect):
    # print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.minCostConnectPoints(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minCostConnectPoints.py',
        description=
        'minCostConnectPoints'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minCostConnectPoints problem :')

    # run([[0,0],[2,2],[3,10],[5,2],[7,0]],20)
    # run([[3,12],[-2,5],[-4,1]],18)
    # run([[0,0],[1,1],[4,4],[5,5],[8,8],[9,9]],18)
    run([[-8,14],[16,-18],[-19,-13],[-18,19],[20,20],[13,-20],[-15,9],[-4,-8]],139)