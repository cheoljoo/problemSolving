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

# validateStackSequences.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        poppedIndex = 0
        stack = []
        for v in pushed:
            if len(stack) == 0:
                stack.append(v)
            elif v != popped[poppedIndex]:
                stack.append(v)
            else :  # v == popped[poppedIndex]:
                poppedIndex += 1
            while poppedIndex != len(popped) and len(stack) > 0:
                if stack[-1] == popped[poppedIndex] :
                    stack.pop()
                    poppedIndex += 1
                else :
                    break
        if len(stack) == 0 and poppedIndex == len(popped):
            return True
        else :
            return False
                

           
def run(s1,s2,expect):
    start = time.time()
    A = Solution()
    r = A.validateStackSequences(s1,s2)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r,s1,s2 , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='validateStackSequences.py',
        description=
        'validateStackSequences'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('validateStackSequences problem :')

    run([1,0],[1,0],True)
    run([0],[0],True)
    run([1,2,3,4,5],[4,5,3,2,1],True)
    run([1,2,3,4,5],[4,3,5,1,2],False)