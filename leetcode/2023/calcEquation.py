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

# calcEquation.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        v = {}
        for i in equations:
            v[i[0]] = 0.0
            v[i[1]] = 0.0 

        p = [i for i in range(len(v))] # parents
        names = [i for i in v.keys()]
        pairs = {n:i for n,i in zip(names,p)}
        def find(x:int):
            if x != p[x]:
                x = find(p[x])
            return x
        def union(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                p[py] = px
        
        for i in equations:
            union(pairs[i[0]],pairs[i[1]])
        i = 1
        for i in range(len(p)):
            p[i] = find(p[i])
        group = defaultdict(list)
        for n,i in zip(names,p):
            group[i].append(n)
        calculated = {}
        for i in group.keys():
            calculated[group[i][0]] = 1.0  # calculated[variable] = 1.0
            v[group[i][0]] = 1.0
            flag = 1
            while flag:
                flag = 0
                for idx,e in enumerate(equations):
                    if e[0] in calculated and e[1] not in calculated:
                        calculated[e[1]] = calculated[e[0]]/values[idx]
                        v[e[1]] = calculated[e[1]]
                        flag = 1
                    elif e[0] not in calculated and e[1] in calculated:
                        calculated[e[0]] = calculated[e[1]]*values[idx]
                        v[e[0]] = calculated[e[0]]
                        flag = 1
        ans = []
        for a,b in queries:
            if a not in v or b not in v:
                ans.append(-1.0)
            else:
                if p[pairs[a]] == p[pairs[b]]:
                    ans.append(v[a]/v[b])
                else :
                    ans.append(-1.0)
        return ans

           
def run(s,s1,s2,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.calcEquation(s,s1,s2)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='calcEquation.py',
        description=
        'calcEquation'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('calcEquation problem :')

    run([["a","b"],["c","d"]],[1.0,1.0],[["a","c"],["b","d"],["b","a"],["d","c"]],[-1.00000,-1.00000,1.00000,1.00000])
    run([["a","b"],["e","f"],["b","e"]],[3.4,1.4,2.3],[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]],[0.29412,10.94800,1.00000,1.00000,-1.00000,-1.00000,0.71429])
    run([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],[6.0, 0.5, -1.0, 1.0, -1.0 ])
    run([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]],[3.75000,0.40000,5.00000,0.20000])
    run([["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]],[0.50000,2.00000,-1.00000,-1.00000])