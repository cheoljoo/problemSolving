from collections import defaultdict
from collections import Counter
from collections import deque
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
from bisect import bisect_left , bisect_right

timeFlag = 0
debugFlag = 0
import math

# removeDuplicates1209.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k :
            return s
        s = list(s)
        stack = [[s[0],1]]
        for i in range(1,len(s)):
            if s[i] == stack[-1][0]:
                stack[-1][1] += 1
            else :
                stack.append([s[i],1])
            
        i = 0
        while i < len(stack):
            ch = stack[i][0]
            cnt = stack[i][1]
            if cnt >= k:
                stack[i][1] %= k
                if stack[i][1] == 0:
                    stack.pop(i)
                    if i-1>=0 and i < len(stack) and stack[i-1][0] == stack[i][0]:
                        i = i-1
                else :
                    i += 1
            else :
                if i+1 < len(stack) and ch == stack[i+1][0]:
                    stack[i][1] += stack[i+1][1]
                    stack.pop(i+1)
                else :
                    i += 1

        # print(stack)
        ans = ""
        for ch,cnt in stack:
            ans += ch*cnt
        return ans
           
def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.removeDuplicates(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='removeDuplicates1209.py',
        description=
        'removeDuplicates'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('removeDuplicates problem :')

    run("abcd",2,"abcd")
    run("deeedbbcccbdaa", 3,"aa")
    run("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy" ,4, "ybth")
    run("pbbcggttciiippooaais",2,"ps")