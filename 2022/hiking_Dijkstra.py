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

timeFlag = 0
debugFlag = 0
import math

# hiking.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def hiking(self, target: List[int] , o : List[List[int]]) -> int:
        if len(o) <= 1 :
            return o[0][0]**2
        m = [[0 for _ in range(len(o[0])+2)] for _ in range(len(o)+2)]
        for i in range(len(o)):
            for j in range(len(o[0])):
                m[i+1][j+1] = o[i][j]
        edges= {}
        row = len(m)
        col = len(m[0])
        for i in range(len(m)):
            for j in range(len(m[0])):
                node = i*len(m) + j
                if j != len(m[0])-1:   # 맨오른쪽 줄
                    if m[i][j] < m[i][j+1]:   # 정상 >= , 우리는 목적지에서 거꾸로가는 것으로 할것이기에 반대로 계산 
                        # node -> node+1
                        edges[(node,node+1)] = abs(m[i][j] - m[i][j+1])
                        edges[(node+1,node)] = (m[i][j] - m[i][j+1])**2
                    else :
                        edges[(node,node+1)] = (m[i][j] - m[i][j+1])**2
                        edges[(node+1,node)] = abs(m[i][j] - m[i][j+1])
                if i != len(m)-1:   # 끝줄
                    if m[i][j] < m[i+1][j]:   # 정상 >=
                        # node -> node + len(m[0])
                        edges[(node,node+row)] = abs(m[i][j] - m[i+1][j])
                        edges[(node+row,node)] = (m[i][j] - m[i+1][j])**2
                    else :
                        edges[(node,node+row)] = (m[i][j] - m[i+1][j])**2
                        edges[(node+row,node)] = abs(m[i][j] - m[i+1][j])
        r = self.dijkstra(row,col,edges,target[0]*col+target[1])
        mn = min(min(r[:col]),min(r[row*col-col:row*col]))
        for i in range(row):
            mn = min(mn,r[i*col])
            mn = min(mn,r[i*col+col-1])
        return mn
    def dijkstra(self,row : int , col : int , graph:Dict[List[int],int],startNode:int) -> Dict[List[int],int]: # n : nodecount , graph[(x,y)] = (w,x1,y1) , from : (x,y)
        result = [math.inf for _ in range(row*col)]
        q = [(0,startNode)]
        while q:
            nextQ = []
            while q:
                w,node = q.pop(0)
                if result[node] != math.inf:
                    continue
                result[node] = w
                # north : node - col , south : node + col , east : node - 1 , west : node + 1
                if node-col >= 0 and result[node-col] == math.inf:
                    heapq.heappush(nextQ,(w+graph[(node,node-col)],node-col))
                if node+col < row*col and result[node+col] == math.inf:
                    heapq.heappush(nextQ,(w+graph[(node,node+col)],node+col))
                if node%col != 0 and result[node-1] == math.inf:
                    heapq.heappush(nextQ,(w+graph[(node,node-1)],node-1))
                if node%col != col-1 and result[node+1] == math.inf:
                    heapq.heappush(nextQ,(w+graph[(node,node+1)],node+1))
            q = nextQ
        # while q:
        #     w,node = q.pop(0)
        #     if result[node] != math.inf:
        #         continue
        #     result[node] = w
        #     # north : node - col , south : node + col , east : node - 1 , west : node + 1
        #     if node-col >= 0 :
        #         heapq.heappush(q,(w+graph[(node,node-col)],node-col))
        #     if node+col < row*col:
        #         heapq.heappush(q,(w+graph[(node,node+col)],node+col))
        #     if node%col != 0:
        #         heapq.heappush(q,(w+graph[(node,node-1)],node-1))
        #     if node%col != col-1:
        #         heapq.heappush(q,(w+graph[(node,node+1)],node+1))
        return result 

           
def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.hiking(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='hiking.py',
        description=
        'hiking'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('hiking problem :')

    run([2,2],
[[1,2,4],
 [1,3,5],
 [2,3,6]],3)

    run([3,3],
[[1,2,4,3,2],
 [1,3,5,4,4],
 [2,3,6,5,1],
 [3,1,4,1,3],
 [2,3,3,5,3]],8)

    run([10,10],
[[1,1,19,20,21,1,40,40,41,1],
[2,1,18,1,22,1,39,1,42,1],
[3,1,17,1,23,1,38,1,43,1],
[4,1,16,1,24,1,37,1,44,1],
[5,1,15,1,25,1,36,1,45,1],
[6,1,14,1,26,1,35,1,46,1],
[7,1,13,1,27,1,34,1,47,1],
[8,1,12,1,28,1,33,1,48,1],
[9,1,11,1,29,1,32,1,49,1],
[10,10,10,1,30,30,31,1,50,50]],50)
