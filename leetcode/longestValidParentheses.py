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

# longestValidParentheses.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sl = list(s)
        return self.go(sl)

    def go(self,s:List[str]) -> int:
        stack = [['s',0]]
        pStack = []
        # ")())(()"
        for i,v in enumerate(s):
            if v == '(':
                stack.append([v,0])
                pStack.append(v)
            elif v== ')':
                if stack[-1][0] == '(':
                    stack[-1][0] = 's'
                    stack[-1][1] += 2
                    pStack.pop()
                else :
                    if pStack:
                        pStack.pop()
                        sum = 0
                        while True:
                            if stack[-1][0] == '(':
                                stack[-1][0] = 's'
                                stack[-1][1] += sum+2
                                break
                            elif stack[-1][0] == 's':
                                sum += stack[-1][1]
                                stack.pop()
                            else :
                                break
                    else :
                        stack.append([v,0])
        mx = 0
        sum = 0
        while stack:
            v,count = stack.pop()
            if v == 's':
                sum += count
            else :
                mx = max(mx,sum)
                sum = 0

        return max(mx,sum)
    # def go(self,s:List[str]) -> int:
    #     # ")())(()"
    #     mx = 0
    #     subsum = 0
    #     while s:
    #         count , s,isAccumulate = self.count(s)
    #         if isAccumulate :
    #             subsum += count
    #         else :
    #             mx = max(mx,subsum)
    #             subsum = count
    #     mx = max(mx,subsum)
    #     return mx
    
    # def count(self,s:List[str]) :
    #     stack = []
    #     count = 0
    #     isAccumulate = True
    #     for i,v in enumerate(s):
    #         if stack:
    #             if v == '(':
    #                 stack.append(v)
    #             elif v== ')':
    #                 if stack :
    #                     stack.pop()
    #                     count += 2
    #                     if not stack:
    #                         if i+1 == len(s):
    #                             s = []
    #                         else :
    #                             s = s[i+1:]
    #                         return (count , s , isAccumulate)
    #                 else : 
    #                     print("error-1")
    #         else :  # stack is empty
    #             if v == '(':
    #                 stack.append(v)
    #             else:
    #                 isAccumulate = False
    #                 count = 0
    #     if stack:
    #         isAccumulate = False
    #     return (count,[], isAccumulate)

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.longestValidParentheses(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='longestValidParentheses.py',
        description=
        'longestValidParentheses'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('longestValidParentheses problem :')

    run("()(())",6)
    run("(()(((()",2)
    run(")()())()()(",4)
    run(")())(()",2)
    run("(()",2)
    run(")()())",4)
    run("",0)
    run("()(()",2)
    run("()",2)