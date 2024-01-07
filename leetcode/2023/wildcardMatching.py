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

# wildcardMatching.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if s == "":
        #     for v in p:
        #         if v != '*':
        #             return False
        #     return True

        # check from the end
        se,pe = len(s)-1,len(p)-1
        while True:
            if se<0 or pe<0:
                break
            if s[se] == p[pe] or p[pe] == '?':
                se -= 1
                pe -= 1
            elif p[pe] == '*':
                break
            else :
                return False
        if pe < 0 and se >=0 :
            return False
        if se < 0 and pe < 0:
            return True
        if se <0 and pe >= 0:
            for i in range(pe+1):
                if p[i] != '*':
                    return False
            return True
        # check from the start
        ss,ps = 0,0
        while True:
            if ss >= len(s) and ps >= len(p):
                return True
            elif ss >= len(s):
                break  # return False
            elif ps >= len(p):
                break  # return False

            if s[ss] == p[ps] or p[ps] == '?':
                ss += 1
                ps += 1
            elif p[ps] == '*':
                break
            else :
                return False
        if ps >= len(p) and ss < len(s) :
            return False
        if ps >= len(p) and ss >= len(s):
            return True
        if ps < len(p) and ss >= len(s):
            for i in range(ps,len(p)):
                if p[i] != '*':
                    return False
            return True
        # print(ss,ps,se,pe,s,p)

        # if one of both directions is satisfied , it is True.
        # run("abcdabcd","*da*c*d",True)
        isInAs = False
        si ,pi = ss,ps
        while True:
            if si > se and pi > pe:
                return True
            if pi < len(p) and p[pi] == '*':
                if pi == pe:
                    return True
                isInAs = True
                pi += 1
                continue
            if si > se or pi > pe:
                break
            elif p[pi] == s[si] or p[pi] == '?':
                pi += 1
                si += 1
                isInAs = False
            elif isInAs == True:
                si += 1
            else :
                break
        
        isInAs = False
        si ,pi = se,pe
        while True:
            if si < ss and pi <ps:
                return True
            if pi >= 0 and p[pi] == '*':
                if pi == ps:
                    return True
                isInAs = True
                pi -= 1
                continue
            if si < ss or pi <ps:
                break
            elif p[pi] == s[si] or p[pi] == '?':
                pi -= 1
                si -= 1
                isInAs = False
            elif isInAs == True:
                si -= 1
            else :
                break
        
        return False




           
def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.isMatch(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s ,s1, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='wildcardMatching.py',
        description=
        'wildcardMatching'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('wildcardMatching problem :')

    run("abce","abc*??",False)
    run("ab","*ab",True)
    run("a","a*",True)
    run("abcabczzzde","*abc???de*",True)
    run("","",True)
    run("","******",True)
    run("a","",False)
    run("aab","c*a*b",False)
    run("aa","a",False)
    run("cb","?a",False)
    run("aa","a?a",False)
    run("cb","??b",False)

    run("aa","*",True)
    run("abcdabcd","*db*",False)
    run("abcdabcd","*da*c*d",True)
    run("abcdabcd","*bc*bc*d",True)
    run("abcdabcd","a*bc**d",True)
    run("abcdabcd","*bcd",True)
    run("abcdabcd","a*bcd",True)
    # we can trace sequentially.

