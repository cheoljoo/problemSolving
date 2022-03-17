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

# scoreOfParentheses.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == '':
            return 0
        elif s == '()':
            return 1
        sum = 0
        subs = ''
        level = 0
        for ch in s:
            if ch == '(':
                if level > 0:
                    subs += ch
                level += 1
            else :
                level -= 1
                if level == 0:
                    if subs == '':
                        sum += 1
                    else :
                        sum += self.scoreOfParentheses(subs)*2
                    subs = ''
                else :
                    subs += ch
        return sum
            
           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.scoreOfParentheses(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='scoreOfParentheses.py',
        description=
        'scoreOfParentheses'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('scoreOfParentheses problem :')

    run("(())()",3)
    run("()",1)
    run("(())",2)
    run("()()",2)
    run("()(()())",5)
    run("((()))",4)
    run("()(()(()()))",11)