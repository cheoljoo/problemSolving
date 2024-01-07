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

import sys
import argparse
import math
import random
import heapq

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = {}
        for f,t,w in edges:
            # print(f,t,w)
            if f not in graph:
                graph[f] = []
            graph[f].append([t,w])
        src1_result = self.dijkstra(n,graph,src1)
        src2_result = self.dijkstra(n,graph,src2)
        graph = {}
        for f,t,w in edges:
            #print(f,t,w)
            if t not in graph:
                graph[t] = []
            graph[t].append([f,w])
        dest_result = self.dijkstra(n,graph,dest)
        
        ans = math.inf
        for i in range(n):
            ans = min(ans,src1_result[i] + src2_result[i] + dest_result[i])
        if ans == math.inf:
            return -1
        return ans
    
    def dijkstra(self,n: int, graph: Dict[int,Tuple[int,int]], f: int): 
        result = [math.inf for _ in range(n)]
        result[f] = 0
        q = [(0,f)]   # (node,total weight)
        visited = set()
        while len(q):
            weight, start = heapq.heappop(q)

            if start in graph:
                
                for nxt,w in graph[start]:
                    if nxt in visited:
                        continue
                    if result[nxt] > (weight + w):
                        result[nxt] = weight + w
                        heapq.heappush(q,(result[nxt],nxt))
                        visited.add(nxt)
        return result

def run(n,s,src1,src2,dest,expect):
    ismatch = Solution()
    r = ismatch.minimumWeight(n,s,src1,src2,dest)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , len(s), s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='set_ax_b.py',
        description=
        'this set hates a b'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0


    run(6,[[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]],1,0,5,9)
    run(3,[[0,1,1],[2,1,1]],0,1,2,-1)
    run(6,[[0,2,2],[0,5,2],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,2],[3,0,1]],3,1,5,6)
    run(20
,[[14,2,24],[1,4,30],[13,10,14],[17,6,47],[2,8,1],[3,6,39],[6,2,8],[5,14,58],[7,9,34],[14,11,67],[18,11,46],[17,19,16],[9,16,32],[1,2,55],[3,14,46],[12,13,48],[18,4,34],[7,16,62],[16,7,28],[8,17,19],[8,15,1],[15,3,11],[19,4,22],[14,15,9],[8,13,42],[4,10,10],[11,12,9],[11,6,32],[16,1,14],[1,18,70],[15,0,28],[3,2,7],[14,17,62],[3,16,33],[3,7,1],[0,5,2],[17,7,42],[13,6,14],[4,9,22],[1,8,27],[0,6,20],[12,1,27],[7,2,54],[13,10,15],[13,16,51],[16,8,5],[7,17,49],[4,9,16],[16,19,65],[10,18,12],[0,19,30],[19,9,68],[0,2,10],[6,1,59],[12,14,60],[10,17,13],[11,9,2],[7,8,39],[8,16,59],[5,7,26],[18,5,61],[9,11,49],[0,16,24],[9,1,54],[16,17,33],[9,18,33],[19,4,14],[17,0,66],[6,16,63]]
,16
,4
,2,72)

