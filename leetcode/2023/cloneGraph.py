from collections import defaultdict
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

# cloneGraph.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 1
debugFlag = 0

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = []


class Solution:
    def __init__(self):
        self.mem = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node,0)
    
    def dfs(self,node:'Node',depth:int) -> 'Node':
        if not node:
            return node
        if node in self.mem:
            return node

        # print(depth,node.val,end="")
        depth += 1
        newNode = Node(node.val)
        self.mem[node] = newNode
        
        # print(" [",end="")
        # for n in node.neighbors:
        #     print(" : ",n.val,end="")
        # print("]")
        
        for n in node.neighbors:
            r = self.dfs(n,depth)
            if n in self.mem:
                tmpNewNode = self.mem[node]
                tmpNewN = self.mem[n]
                tmpNewNode.neighbors.append(tmpNewN)
            else :
                newN = Node(n.val)
                newNode.neighbors.append(newN)
                self.mem[n] = newN               
        return newNode
        
        
            
def run(s,expect):
    i = 1
    for n in s:
        node = Node(i)
        for nei in n:
            neinode = Node(nei)
            node.neighbors.append(neinode)
    start = time.time()
    A = Solution()
    r = A.cloneGraph(s)
    print(" , total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , ": " , end="")  
    print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='cloneGraph.py',
        description=
        'cloneGraph'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('cloneGraph problem :')

    s = [[2,4],[1,3],[2,4],[1,3]]
    run(s,[[2,4],[1,3],[2,4],[1,3]])
    s = [[]]
    run(s,[[]])
    s = []
    run(s,[])

    
    