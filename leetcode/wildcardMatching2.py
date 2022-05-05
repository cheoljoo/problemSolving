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
        # check from the end : remove matched string from the end
        s = list(s)
        p = list(p)
        i = 0
        while i+1 < len(p):
            if p[i] == '*' and p[i+1] == '*':
                p.pop(i)
            else :
                i += 1
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
        s = s[:se+1]
        p = p[:pe+1]
        # check from the start : remove matched string from the start
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
        s = s[ss:]
        p = p[ps:]

        # if pattern has more than one asterrisk
        # if one of both directions is satisfied , it is True.
        # run("abcdabcd","*da*c*d",True)
        isInAs = False
        si ,pi = 0,0
        sizeTilAs = {}
        size = 1
        for i in reversed(range(len(p))):
            if p[i] == '*':
                size = 0
            sizeTilAs[i] = size
            size += 1
        while True:
            if p[pi] == '*' and pi == len(p)-1:
                return True
            if si >= len(s) and pi >= len(p):
                return True
            elif si >= len(s) and pi < len(p):
                break
            elif si < len(s) and pi >= len(p):
                break
            else :
                if p[pi] == '*':
                    isInAs = True
                    pi += 1
                elif p[pi] == s[si] or p[pi] == '?':
                    isMatch , jump = self.getMatched(s,p,si,pi,False,sizeTilAs)
                    if isMatch :
                        pi += jump
                        si += jump
                        isInAs = False
                    else :
                        if isInAs == True:
                            si += 1
                        else : 
                            break
                elif isInAs == True:
                    si += 1
                else :
                    break
        
        isInAs = False
        si ,pi = len(s)-1 , len(p)-1
        sizeTilAsReverse = {}
        size = 0
        for i in range(len(p)):
            if p[i] == '*':
                size = 0
            sizeTilAsReverse[i] = size
            size += 1
        while True:
            if p[pi] == '*' and pi == 0:
                return True
            if si < 0 and pi < 0:
                return True
            elif si < 0 and pi >= 0:
                break
            elif si >= 0 and pi < 0:
                break
            else:
                if p[pi] == '*':
                    isInAs = True
                    pi -= 1
                elif p[pi] == s[si] or p[pi] == '?':
                    isMatch , jump = self.getMatched(s,p,si,pi,True,sizeTilAsReverse)
                    if isMatch :
                        pi -= jump
                        si -= jump
                        isInAs = False
                    else :
                        if isInAs == True:
                            si -= 1
                        else : 
                            break
                elif isInAs == True:
                    si -= 1
                else :
                    break
        
        return False

    def getMatched(self,s,p,si,pi,isReverseOrder,sizeTillAs):
        isMatch = False
        count = 0
        if isReverseOrder == False :
            pl = range(sizeTillAs[pi])
        else :
            pl = range(0,-1*(sizeTillAs[pi]),-1)
        for i in pl:
            if i+si >= len(s) or i+si < 0:
                break
            if p[i+pi] == '*':
                isMatch = True
                break
            elif p[i+pi] == s[i+si] or p[i+pi] == '?':
                count += 1
                continue
            else :
                break
        if count == sizeTillAs[pi]:
            isMatch = True
        return (isMatch,count)


           
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

    run("ab","*ab*****",True)
    run("abcdabcd","*db*",False)

    run("aa","*",True)
    run("mississippi","m*si*",True)
    run("abce","abc*??",False)
    
    run("a","a*****",True)
    run("abcabczzzde","*abc???de*",True)
    run("","",True)
    run("","******",True)
    run("a","",False)
    run("aab","c*a*b",False)
    run("aa","a",False)
    run("cb","?a",False)
    run("aa","a?a",False)
    run("cb","??b",False)

    
    
    run("abcdabcd","*da*c*d",True)
    run("abcdabcd","*bc*bc*d",True)
    run("abcdabcd","a*bc**d",True)
    run("abcdabcd","*bcd",True)
    run("abcdabcd","a*bcd",True)
    # we can trace sequentially.

