# from collections import defaultdict
import enum
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

# shortestPathLength3.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode
# try cache , change the node status into bit mask type

timeFlag = 0
debugFlag = 0
class Solution:
    def __init__(self):
        self.startNodeList = []
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # initialize : self.node[MAX]=0 , self.edge[fromNode*MAX+toNode]=0
        if len(graph) == 1 :
            return 0
            
        self.MAX = len(graph)
        tmpEdgeCountt = self.MAX
        self.endMask = (1 << self.MAX) - 1
        for f in range(len(graph)):
            minNodeCount = len(graph[f])
            if tmpEdgeCountt > minNodeCount :
                tmpEdgeCountt = minNodeCount
                self.startNodeList.clear()
                self.startNodeList.append((f,1<<f))
            elif tmpEdgeCountt == minNodeCount :
                self.startNodeList.append((f,1<<f))
        
        # calculate 
        a = self.bfs(graph)
        return a
    
    def bfs(self,graph: List[List[int]]) -> int :
        edgeCount = 0
        queue = self.startNodeList
        if debugFlag : 
            print(len(queue),queue)
        visited = {}
        endMask = (1<<len(graph)) - 1
        path = []
        while True:
            nextQ = []
            if debugFlag : 
                print(len(queue))
            for (node,mask) in queue :
                if mask == endMask :
                    return edgeCount
                for n in graph[node]:
                    mask2 = mask | (1<<n)
                    if debugFlag :
                        mask2m = []
                        for i in range(len(graph)):
                            if mask2 & (1<<i):
                                mask2m.append(1)
                            else :
                                mask2m.append(0)
                    if not (n,mask2) in visited :
                        nextQ.append((n,mask2))
                        visited[(n,mask2)] = []
                    else :
                        visited[(n,mask2)].append(n)
            edgeCount += 1
            queue = nextQ

        return 0
                    

                
class Solution2:
    def __init__(self):
        self.path = []
        self.startNodeList = []
        self.dp = {}
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # initialize : self.node[MAX]=0 , self.edge[fromNode*MAX+toNode]=0
        if len(graph) == 1 :
            return 0
            
        self.MAX = len(graph)
        tmpEdgeCountt = self.MAX
        self.endMask = (1 << self.MAX) - 1
        for f in range(len(graph)):
            minNodeCount = len(graph[f])
            if tmpEdgeCountt > minNodeCount :
                tmpEdgeCountt = minNodeCount
                self.startNodeList.clear()
                self.startNodeList.append((f,1<<f))
            elif tmpEdgeCountt == minNodeCount :
                self.startNodeList.append((f,1<<f))
        
        # calculate 
        a = self.bfs_path(graph)
        return a
    
    def bfs_path(self,graph: List[List[int]]) -> int :
        edgeCount = 0
        queue = self.startNodeList
        # print(len(queue),queue)
        visited = {}
        endMask = (1<<len(graph)) - 1
        path = []
        while True:
            nextQ = []
            # print(len(queue))
            for (node,mask) in queue :
                if mask == endMask :
                    print(visited[(node,mask)])
                    return edgeCount
                for n in graph[node]:
                    mask2 = mask | 1<<n
                    mask2m = []
                    for i in range(len(graph)):
                        if mask2 & (1<<i):
                            mask2m.append(1)
                        else :
                            mask2m.append(0)
                    if not (n,mask2) in visited :
                        nextQ.append((n,mask2))
                        visited[(n,mask2)] = []
                        if mask2 == endMask :
                            print(len(queue),mask2,mask2m)
                    else :
                        visited[(n,mask2)].append(n)
            edgeCount += 1
            queue = nextQ

        return 0                   
        
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.shortestPathLength(s)
    print(" len :", len(s) , end="") 
    print(" , total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , ":" , end="")  
    if len(s) < 30: print(s , end="")  
    print()
    
    # A = Solution2()
    # r = A.shortestPathLength(s)

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='shortestPathLength.py',
        description=
        'shortestPathLength'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args() 
    debug = args.debug
    if not debug:
        debug = 0

    print('shortestPathLength problem :')

    s = [[1,2,3],[0],[0],[0]]
    run(s,4)
    s = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    run(s,4)
    s = [[]]
    run(s,0)
    s = [[1],[0]]
    run(s,1)
    s = [[1],[0,2,4],[1,3],[2],[1,5],[4]]
    run(s,6)
    s = [[1],[0,2,6],[1,3],[2],[5],[4,6],[1,5,7],[6]]
    run(s,9)
    s = [[1,2,3,4],[0,2],[0,1],[0,5],[0,6],[3],[4]]
    run(s,7)
    s = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],
         [0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]
    run(s,11)
    s = [[2],[3],[3,4,5,6,7,8,9,10,11,0],[2,4,5,6,7,8,9,10,11,1],[2,3,5,6,7,8,9,10,11],[2,3,4,6,7,8,9,10,11],[2,3,4,5,7,8,9,10,11],[2,3,4,5,6,8,9,10,11],
         [2,3,4,5,6,7,9,10,11],[2,3,4,5,6,7,8,10,11],[2,3,4,5,6,7,8,9,11],[2,3,4,5,6,7,8,9,10]]
    run(s,11)
    s = [[1,4],[0,3,10],[3],[1,2,6,7],[0,5],[4],[3],[3],[10],[10],[1,9,8]]
    run(s,15)

    