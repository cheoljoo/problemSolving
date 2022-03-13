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

class Solution:
    def __init__(self):
        self.path = []
        self.visitedEdge = {}
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        self.nodes = {}
        # [[0,1,1],[2,1,1]]  : we change direction reversely. because we can start from dest
        for (n1,n2,w) in edges:
            if not n2 in self.nodes :
                self.nodes[n2] = []
            self.nodes[n2].append((n1,w))
        
        # DFS
        src1ok = False
        src2ok = False
        weight = 0
        (src1ok,src2ok,src1weight,src2weight,commonweight) = self.dfs(dest,src1,src2,isVisitSrc2)
        weight = src1weight+src2weight
        if src1ok == True and src2ok == True :
            return weight - commonweight
        if src1ok == True and src2ok == False :
            (src1ok,src2ok,src1weight,src2weight,commonweight) = self.dfs(dest,-1,src2)
            if src2ok == False :
                return -1
            return weight + src2weight
        elif src1ok == False and src2ok == True :
            (src1ok,src2ok,src1weight,src2weight,commonweight) = self.dfs(dest,src1,-1)
            if src1ok == False :
                return -1
            return weight + src1weight
        return -1
    def dfs(self,start,end1,end2,isVisitEnd2):
        """ 
        goto end1

        Args:
            start (_type_): _description_
            end1 (_type_): _description_
            end2 (_type_): _description_

        Returns:
            _type_: _description_
        """
        for (next,weight) in self.nodes[start]:
            if end1 == -1 and end2 == -1 :
                return (True,True,w,w,w)
            if start == end1: 
                (src1ok,src2ok,src1weight,src2weight,commonweight) = self.dfs(next,-1,src2,0)
        

def run(n,s,src1,src2,dest,expect):
    ismatch = Solution()
    r = ismatch.minimumWeight(n,s,src1,src2,dest)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

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

