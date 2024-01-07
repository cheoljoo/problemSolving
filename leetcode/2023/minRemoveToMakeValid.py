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

# minRemoveToMakeValid.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        r = []
        stack = []  # index of '('
        count = 0
        for ch in s:
            if ch == '(':
                r.append(ch)
                stack.append(count)
                count += 1
            elif ch == ')':
                if len(stack) > 0:
                    r.append(ch)
                    stack.pop()
                    count += 1
            else:
                r.append(ch)
                count += 1
            
        for _ in range(len(stack)):
            idx = stack.pop()
            r.pop(idx)
        return ''.join(r)

           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.minRemoveToMakeValid(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minRemoveToMakeValid.py',
        description=
        'minRemoveToMakeValid'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minRemoveToMakeValid problem :')

    run("lee(t(c)o)de)","lee(t(c)o)de")
    run("aaa)))bbb((ccc","aaabbbccc")
    run("a(b)(c(d)((tgf","a(b)c(d)tgf")

