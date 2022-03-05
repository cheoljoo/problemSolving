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

# shortestPathLength.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
class Solution:
    def __init__(self):
        self.MAX = 12  # node range(12)
        self.node = []
        self.edge = []
        self.path = []
        self.startNodeList = []
    def shortestPathLength(self, graph: List[List[int]]) -> int:   
        # initialize : self.node[MAX]=0 , self.edge[fromNode*MAX+toNode]=0
        self.MAX = len(graph)
        self.minEdgeCount = self.MAX
        self.INFINITE = self.MAX * self.MAX + 1
        self.minPathCount = self.INFINITE
        for f in range(len(graph)):
            minNodeCount = len(graph[f])
            if self.minEdgeCount > minNodeCount :
                self.minEdgeCount = minNodeCount
                self.startNodeList.clear()
                self.startNodeList.append(f)
            elif self.minEdgeCount == minNodeCount :
                self.startNodeList.append(f)
            self.node.append(0)
            for t in range(self.MAX):
                edge = f*self.MAX + t
                self.edge.append(0)
        
        # calculate 
        if len(graph) == 1 :
            return 0
        min = self.INFINITE
        for startNode in self.startNodeList : 
            self.node[startNode] = 1
            self.path.append(startNode)
            for i in graph[startNode] :
                a = self.dfs(graph,startNode,i,1,0)
                if min > a :
                    min = a
            self.node[startNode] = 0  # pop  clear : self.edge , self.node
        return min
    
    def dfs(self,graph: List[List[int]], f:int , t:int , nodeCount:int , edgeCount:int) -> int :
        edgeCount += 1
        if self.minPathCount < edgeCount:
            return self.INFINITE 
        
        isVisitedNode = (self.node[t] == 1)
        edge = f*self.MAX + t
        isVisitedEdge = (self.edge[edge] == 1)
        self.path.append(t)
        
        if isVisitedEdge == True :
            self.path.pop()
            return self.INFINITE
        
        if isVisitedNode == False :
            nodeCount += 1
        
        
        if nodeCount == len(graph) :
            if debugFlag : print("edgeCount:",edgeCount,"path:", self.path)
            if self.minPathCount > edgeCount :
                self.minPathCount = edgeCount
            self.path.pop()
            return edgeCount
        
        mi = self.INFINITE
        self.edge[edge] = 1 
        self.node[t] = 1
        # a=[]
        # b=[]
        # a.append(mi)
        for i in graph[t] :
            a = self.dfs(graph,t,i,nodeCount,edgeCount)
            if mi > a :
                mi = a
            # tmp = self.dfs(graph,t,i,nodeCount,edgeCount)
            # a.append(tmp)
            # b.append(i)
            # if tmp != self.INFINITE :
            #     pass
            # mi = min(a)
        
        self.path.pop()        
        if isVisitedNode == False :
            self.node[t] = 0
        if isVisitedEdge == False :
            self.edge[edge] = 0
        return mi
                
                   
        
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
    s = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]
    run(s,0)
    
    