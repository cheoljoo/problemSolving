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

# removeInvalidParentheses.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ss = []
        lFlag = 0
        for i in range(len(s)):
            if s[i] == '(':
                lFlag = 1
                ss.append(s[i])
            elif s[i] == ')':
                if lFlag:
                    ss.append(s[i])
            else :
                ss.append(s[i])

        rFlag = 0
        for i in reversed(range(len(ss))):
            if ss[i] == ')':
                rFlag = 1
                break
            elif ss[i] == '(':
                if rFlag == 0:
                    ss.pop(i)

        remove = [ 0 for _ in range(len(ss))]
        stack = []
        self.ans = []
        self.removeMinCount = math.inf
        self.checkValidParentheses(0,ss,remove,stack,0)
        return self.ans
        
    def checkValidParentheses(self, i, s , r,st,removeMinCount):
        if i == len(s):
            if not st:
                if self.removeMinCount == math.inf or self.removeMinCount == removeMinCount:
                    p = self.getAnswer(s,r)
                    # print("success:",removeMinCount,p)
                    self.removeMinCount = removeMinCount
                    if p not in self.ans:
                        self.ans.append(p)
            return
        if s[i] == '(' or s[i] == ')':
            stack1 = st.copy()
            stack2 = st.copy()

            r[i] = 0
            flag = 1
            if s[i] == '(':
                stack1.append(s[i])
            else :
                if stack1:
                    stack1.pop()
                else :
                    flag = 0
            if flag :
                # if self.removeMinCount > 
                self.checkValidParentheses(i+1,s,r,stack1,removeMinCount)
            
            r[i]=1
            self.checkValidParentheses(i+1,s,r,stack2,removeMinCount+1)
            
        else :
            self.checkValidParentheses(i+1,s,r,st,removeMinCount)
    def getAnswer(self,s,r):
        ans = ""
        for i in range(len(r)):
            if r[i] == 1:
                continue
            ans += s[i]
        return ans
                 
def run(s,expect):
    print(s,": ",end="")
    start = time.time()
    A = Solution()
    r = A.removeInvalidParentheses(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    fail = 0
    if len(r) !=  len(expect):
        fail = 1
    for v in r:
        if v not in expect:
            fail = 1
            break
    if fail == 0:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='removeInvalidParentheses.py',
        description=
        'removeInvalidParentheses'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('removeInvalidParentheses problem :')

    run("()())()",["(())()","()()()"])
    run("(a)())()",["(a())()","(a)()()"])
    run(")(",[""])
    run("a(a)((b",["a(a)b"])
    run("(((()())()",['(((())))', '((()()))', '((()))()', '(()())()'])
    run("a()())(b)",['a()()(b)', 'a(())(b)'])
    run("a(a)))((()()b",['a(a)(())b', 'a(a)()()b'])
    run("(a)())()",['(a)()()', '(a())()'])