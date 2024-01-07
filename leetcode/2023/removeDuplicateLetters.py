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

# removeDuplicateLetters.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = {}
        isVisit = {}
        for ch in s:
            if ch in count :
                count[ch] += 1
            else :
                count[ch] = 1
            isVisit[ch] = 0
        for ch in s :
            count[ch] -= 1
            if isVisit[ch] > 0 :
                continue
            if len(stack) == 0:
                stack.append(ch)
                isVisit[ch] += 1
            else :
                while(len(stack)>0 and stack[-1]>ch and count[stack[-1]]>0):
                    tch = stack.pop()
                    isVisit[tch] -= 1
                stack.append(ch)
                isVisit[ch] += 1
            
        return ''.join(stack)

           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.removeDuplicateLetters(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r,s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='removeDuplicateLetters.py',
        description=
        'removeDuplicateLetters'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('removeDuplicateLetters problem :')

    run("bcabc","abc")
    run("cbacdcbc","acdb")