from collections import defaultdict
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

# toyAlly.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def toyAlly(self, N,pair):
        # self.startQ = {}
        self.node = {}
        self.isVisit = {}
        flag = 1
        for (a,b) in pair:
            if a in self.node:
                self.node[a].append(b)
            else :
                self.node[a] = [b]
            if b not in self.node:
                self.node[b] = []
            self.isVisit[a] = -1
            self.isVisit[b] = -1
            # self.startQ[a] = 0
            # self.startQ[b] = 0
        
        flag  = True
        while flag :
            start = -1
            for a in self.isVisit.keys():
                if self.isVisit[a] == -1:
                    start = a
                    self.isVisit[start] = 1
                    break
            if start == -1 :
                break
            if self.go([start],1) == False:
                print("NO")
                return "NO"
        print("YES")
        return "YES"

    def go(self,startQ,side):
        Q = startQ
        while len(Q) :
            newQ = []
            for n in Q:
                for a in self.node[n]:
                    if self.isVisit[a] == -1:
                        newQ.append(a)
                        self.isVisit[a] = (side+1)%2
                    else :
                        if self.isVisit[a] != (side+1)%2:
                            return False
            Q = newQ
            side = (side+1)%2



def run(s,s2,expect):
    start = time.time()
    A = Solution()
    r = A.toyAlly(s,s2)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r,s ,s2, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='toyAlly.py',
        description=
        'toyAlly'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('toyAlly problem :')

    run(3,[[1,2],[2,3],[3,1]],"NO")
    run(4,[[1,2],[2,3],[3,4],[4,1]],"YES")
    run(6,[[1,2],[2,3],[1,4],[1,5],[6,2],[4,6]],"YES")
    run(9,[[1,2],[2,3],[1,4],[1,5],[6,2],[4,6],[7,8],[8,9],[9,7]],"NO")


