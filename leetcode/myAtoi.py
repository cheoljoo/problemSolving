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

# myAtoi.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def myAtoi(self, s: str) -> int:
        plus = True
        i = 0
        while i < len(s):
            ch = s[i]
            n = ord(ch)
            if ch == ' ':
                pass
            elif ch == '-':
                plus = False
                i += 1
                break
            elif ch == '+':
                i += 1
                break
            elif ch == '.':
                return 0
            elif n < ord('0') or n > ord('9'):
                return 0
            elif ord('0') <= n and n <= ord('9'):
                break
            i += 1
        print(i,s,s[i:])
        ans = 0
        digit = 0
        while i < len(s):
            ch = s[i]
            n = ord(ch)
            if n < ord('0') or n > ord('9'):
                break
            elif ord('0') <= n and n <= ord('9'):
                d = n - ord('0')
                ans *= 10
                ans += d
            i += 1
        if plus == False:
            ans *= -1
        print(ans)
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 -1:
            return 2**31 -1
        else:
            return ans
                
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.myAtoi(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='myAtoi.py',
        description=
        'myAtoi'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('myAtoi problem :')

    run("   -42",-42)
    run("4193 with words",4193)
    run("+ 4",0)
    run(".4",0)
    run("a+4",0)
    run("- 5 w",0)