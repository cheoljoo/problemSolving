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
        self.MAX = 12  # node range(12)
        self.edge = []
        self.path = []
        self.startNodeList = []
        self.dp = {}
    def shortestPathLength(self, graph: List[List[int]]) -> int:   
        # initialize : self.node[MAX]=0 , self.edge[fromNode*MAX+toNode]=0
        self.MAX = len(graph)
        tmpEdgeCountt = self.MAX
        self.INFINITE = self.MAX * self.MAX + 1
        self.minPathCount = self.INFINITE
        self.endMask = (1 << self.MAX) - 1
        mask = 0
        for f in range(len(graph)):
            minNodeCount = len(graph[f])
            if tmpEdgeCountt > minNodeCount :
                tmpEdgeCountt = minNodeCount
                self.startNodeList.clear()
                self.startNodeList.append(f)
            elif tmpEdgeCountt == minNodeCount :
                self.startNodeList.append(f)
            for t in range(self.MAX):
                edge = f*self.MAX + t
                self.edge.append(0)
        
        # calculate 
        if len(graph) == 1 :
            return 0
        min = self.INFINITE
        for startNode in self.startNodeList : 
            mask = 1 << startNode
            for i in graph[startNode] :
                # self.dp.clear()
                self.path.append(startNode)
                a = self.dfs(graph,startNode,i,1,mask,0)
                self.dp[(i,mask)] = a
                self.path.pop()
                if min > a :
                    min = a
                if min == self.MAX-1 :
                    break
            # mask = mask ^ (1 << startNode)   # pop  clear : self.edge , self.node
        return min
    
    def dfs(self,graph: List[List[int]], f:int , t:int , nodeCount:int , mask:int , edgeCount:int) -> int :
        m = []
        for i in range(len(graph)):
            if mask & (1<<i):
                m.append(1)
            else :
                m.append(0)
        
        edgeCount += 1
        if self.minPathCount <= edgeCount:
            return self.INFINITE 
        
        ## critical point to reduce running time
        if self.minPathCount <= len(graph) - (nodeCount + 1) + edgeCount :
            return self.minPathCount
        
        isVisitedNode = (mask & (1<<t)) != 0
        edge = f*self.MAX + t
        isVisitedEdge = (self.edge[edge] == 1)
        self.path.append(t)
        
        if isVisitedEdge == True :
            self.path.pop()
            return self.INFINITE
        
        if isVisitedNode == False :
            nodeCount += 1
        
        if f==2 :
            pass
        if f == 2 and t == 3  :
            pass
                
        if nodeCount == len(graph) :
            if debugFlag : print("nodeCount:" , nodeCount , "edgeCount:",edgeCount,"path:", self.path)
            if self.minPathCount > edgeCount :
                self.minPathCount = edgeCount
            self.path.pop()
            return edgeCount
        
                
        if (t,mask) in self.dp :
            if self.dp[(t,mask)] <= edgeCount :
                self.path.pop()
                return self.dp[(t,mask)]
                
        mi = self.INFINITE
        self.edge[edge] = 1 
        mask |= (1<<t)
        a=[]
        b=[]
        a.append(mi)
        m1 = []
        for i in range(len(graph)):
            if mask & (1<<i):
                m1.append(1)
            else :
                m1.append(0)
        
        if self.minPathCount == 14 :
            pass
        
        for i in reversed(graph[t]) :
            # aa = self.dfs(graph,t,i,nodeCount,mask,edgeCount)
            # if (t,i,mask) in self.dp :
            #     if self.dp[(t,i,mask)] > aa :
            #         self.dp[(t,i,mask)] = aa
            # else :
            #     self.dp[(t,i,mask)] = aa
            # if mi > aa :
            #     mi = aa

            if nodeCount + 1 == len(graph) :
                pp = 0
                for ii in range(len(graph)) :
                    if not (mask & (1<<ii)) :
                        pp = ii
                        if ii in graph[t]:
                            tmp = self.dfs(graph,t,ii,nodeCount,mask,edgeCount)
                            if (ii,mask) in self.dp :
                                if self.dp[(ii,mask)] > tmp :
                                    self.dp[(ii,mask)] = tmp
                            else :
                                self.dp[(ii,mask)] = tmp
                            a.append(tmp)
                            b.append(i)
                            mi = min(a)
                            break
            
            tmp = self.dfs(graph,t,i,nodeCount,mask,edgeCount)
            if (i,mask) in self.dp :
                if self.dp[(i,mask)] > tmp :
                    self.dp[(i,mask)] = tmp
            else :
                self.dp[(i,mask)] = tmp
            a.append(tmp)
            b.append(i)
            mi = min(a)
        
        self.path.pop()        
        if isVisitedNode == False :
            mask = mask ^ (1 << t)
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

    