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

# maximumBobPoints.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def __init__(self):
        self.mem = {}  # {(scoring_section,remaining_arrow_count)} = mask
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        (mask,score) = self.dp(numArrows,0,len(aliceArrows)-1,0,aliceArrows)
        # print("mask:",mask)
        r = []
        zeroTarget = numArrows
        for i in range(1,len(aliceArrows)):
            if mask & 1<<i :
                zeroTarget -= aliceArrows[i]+1
                r.append(aliceArrows[i]+1)
            else :
                r.append(0)
        r = [zeroTarget] + r
        return r
    def dp(self,numArrows: int, mask , scoring_section  , score ,aliceArrows: List[int]) -> (int,int):
        # print("dp:",numArrows  , "mask=",end="")
        # for i in range(len(aliceArrows)):
        #     if mask & 1<<i :
        #         print("1 ",end="")
        #     else :
        #         print("0 ",end="")
        # print(" ", scoring_section,aliceArrows)
        if numArrows <= 0 :
            return (mask,score)
        if scoring_section <= 0:
            return (mask,score)
        if (scoring_section,numArrows) in self.mem:
            return self.mem[(scoring_section,numArrows)]
        
        score1 = 0
        if numArrows- (aliceArrows[scoring_section]+1) >= 0:
            mask1,score1 = self.dp(numArrows- (aliceArrows[scoring_section]+1) , mask , scoring_section-1 , score , aliceArrows[:-1])
            mask1 |= 1<<scoring_section
            score1 += scoring_section
        else :
            mask1 = mask
        mask2,score2 = self.dp(numArrows , mask , scoring_section-1 , score , aliceArrows[:-1])
        
        # score1 = 0
        # for i in range(len(aliceArrows)):
        #     if mask1 & 1<<i :
        #         score1 += i
        # score2 = 0
        # for i in range(len(aliceArrows)):
        #     if mask2 & 1<<i :
        #         score2 += i
        if score1 >= score2 :
            self.mem[(scoring_section,numArrows)] = (mask1,score1)
        else :
            self.mem[(scoring_section,numArrows)] = (mask2,score2)
        # print("ret dp:",numArrows  , "mask=",end="")
        # for i in range(12):
        #     if self.mem[(scoring_section,numArrows)][0] & 1<<i :
        #         print("1 ",end="")
        #     else :
        #         print("0 ",end="")
        # print("score:",score,score1,score2, "section:",scoring_section,aliceArrows)
        # print("mem:",self.mem)
        return self.mem[(scoring_section,numArrows)]

           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.maximumBobPoints(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maximumBobPoints.py',
        description=
        'maximumBobPoints'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maximumBobPoints problem :')

    run(3,[0,0,1,0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,0,1,1,1,0])
    run(9,[1,1,0,1,0,0,2,1,0,1,2,0],[0,0,0,0,1,1,0,0,1,2,3,1])