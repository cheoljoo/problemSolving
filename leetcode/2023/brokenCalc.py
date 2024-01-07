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

# brokenCalc.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

# algorithm
# count SV -> target
# count +=1  SV-1 -> target
# count +=1  SV*2 -> target

# leaf
# SV-1 == target
# SV-1 < target -> ERROR
# SV*2 == target 
# SV*2 > tagrget ==> SV*2-target

# DP : mem{SV} = count

class Solution:
    # def __init__(self):
    #     self.mem = {}
    #     self.visited = {}

    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        if startValue > target :
            return startValue - target
        elif startValue == target :
            return 0
        if target % 2 == 1 :
            target += 1
            count += 1
        while True:
            if startValue == target//2 :
                return count + 1
            elif startValue > target//2:
                break
            # elif target % 2 == 1:
            #     break
            else :
                target //= 2
                count += 1
            if target % 2 == 1 :
                target += 1
                count += 1
        print("1:",startValue,target,count)
        if target % 2 == 1 :
            target += 1
            count += 1
        while True: 
            if startValue*2 == target:
                return count+1
            elif startValue*2 > target:
                break
            else :
                startValue *= 2
                count += 1
        print("2:", startValue,target,count)
        return count + startValue - target//2 + 1
        
        
        # if startValue == 0:
        #     return math.inf
        # if startValue == target :
        #     self.mem[target] = 0
        #     return 0
        # if startValue*2 == target :
        #     self.mem[target] = 1
        #     return 1
        # if startValue in self.mem:
        #     return self.mem[startValue]
        # if startValue >= target:
        #     self.mem[startValue] = startValue - target
        #     return startValue - target
        # if startValue in self.visited:
        #     return math.inf
        # else :
        #     self.visited[startValue] = 0
        
        # ret = min(1 + self.brokenCalc(startValue - 1, target) , 1 + self.brokenCalc(startValue*2,target))
        # if startValue in self.mem :
        #     if self.mem[startValue] < ret :
        #         self.mem[startValue] = ret
        # else :
        #     self.mem[startValue] = ret
        # return ret
                

           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.brokenCalc(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s ,s1, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='brokenCalc.py',
        description=
        'brokenCalc'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('brokenCalc problem :')

    run(2,3,2)
    run(5,8,2)
    run(3,10,3)
    run(100,100,0)
    run(100,1,99)
    run(1,1000000,28)
    run(1,1000,12)
    run(1,10000,20)
    run(1,100000,24)
# example
'''
2
3
5
8
3
10
100
100
100
1
1
1000000
'''
