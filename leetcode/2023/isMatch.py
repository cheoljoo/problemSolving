from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        fc = []   # forward character  / forward asterisk
        fa = []  # 1 is asterrisk , 0 is once
        fac = []  # asterrisk -> count   b*b -> 1
        prev = None
        for i in range(0,len(p)):
            if p[i] == '*' :
                continue
            if (i+1) == len(p) : # this is last character
                if (prev == p[i]) : #or (prev != None and p[i] == '.'):   #  b*b   b*.  => b*
                    continue
                else :
                    fc.append(p[i])
                    fa.append(0)
                    fac.append(0)
            else :
                if p[i+1] == '*':
                    fc.append(p[i])
                    fa.append(1)
                    fac.append(0)
                    prev = p[i]
                else :
                    if (prev == p[i])  : # or (prev != None and p[i] == '.'):  #  b*b   b*.  => b*
                        facc = fac.pop()
                        facc += 1
                        fac.append(facc)
                        continue
                    else :
                        fc.append(p[i])
                        fa.append(0)
                        fac.append(0)
                        prev = None

        bc = []  # backward character  / backward asterisk
        ba = []  # 1 is asterrisk , 0 is once
        bac = []  # asterrisk -> count   bb* -> 1
        prev = None
        asterrisk = False
        for i in reversed(range(0,len(p))):
            if p[i] == '*' :
                asterrisk = True
                continue
                
            if asterrisk == True : # this is last character
                prev = p[i]
                bc.insert(0,p[i])
                ba.insert(0,1)
                bac.insert(0,0)
                asterrisk = False
            else:
                if (prev == p[i]) : #or (prev != None and p[i] == '.'):   #  bb*   .b*  => b*
                    bac[0] += 1
                    continue
                else :
                    bc.insert(0,p[i])
                    ba.insert(0,0)
                    bac.insert(0,0)
                    asterrisk = None
                    prev = None
                        
        paCount = 0  # .* count (point_askrisk)
        for i in range(0,len(fc)):
            if (fc[i] == '.') and (fa[i] == 1):
                paCount += 1
    

        # ex. s = "aaabbb"  ,   p = "aa*b*c*b"
        # 1. right direction
        isTrue = True    
        idx = 0
        i = 0
        while i < len(s) :
            if idx == len(fc) :
                isTrue = False
                return False
            m = s[i]
            if fa[idx] == 1 :
                if (m != fc[idx]) and (fc[idx] != '.'):
                    if fac[idx] <= 0 :
                        idx += 1
                    else:
                        isTrue = False
                        return False
                    continue
                else :
                    fac[idx] -= 1
                    i += 1
                    continue
            else :
                if (m != fc[idx]) and (fc[idx] != '.'):
                    isTrue = False
                    return False
                else :
                    idx += 1                   
                    i += 1
                    continue

        # 2. left direction
        idx = len(bc)-1
        i = len(s)-1
        while i >= 0 :
            if idx < 0 :
                isTrue = False
                return False
            m = s[i]
            if ba[idx] == 1 :
                if (m != bc[idx]) and (bc[idx] != '.'):
                    if bac[idx] <= 0:
                        idx -= 1
                    else:
                        isTrue = False
                        return False
                    continue
                else :
                    bac[idx] -= 1
                    i -= 1
                    continue
            else :
                if (m != bc[idx]) and (bc[idx] != '.'):
                    isTrue = False
                    return False
                else :
                    idx -= 1
                    i -= 1
                    continue               
        
        tc = []   # forward character  / forward asterisk
        ta = []  # 1 is asterrisk , 0 is once
        for i in range(0,len(p)):
            if p[i] == '*' :
                continue
            if (i+1) == len(p) : # this is last character
                tc.append(p[i])
                ta.append(0)
            else :
                if p[i+1] == '*':
                    tc.append(p[i])
                    ta.append(1)
                else :
                    tc.append(p[i])
                    ta.append(0)
        idx = 0
        i = 0
        while idx < len(tc) :
            if ta[idx] == 0 :
                if i == len(s) :
                    isTrue = False
                    return False
                m = s[i]
                if (m != tc[idx]) and (tc[idx] != '.') :
                    i += 1
                    continue
                else :
                    i += 1
                    idx += 1
                    continue
            else :
                idx += 1
                                        
        # print(isTrue)
            
        return isTrue

def run(s,p,expect):
    ismatch = Solution()
    r = ismatch.isMatch(s,p)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s , p)   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='set_ax_b.py',
        description=
        'this set hates a b'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    # s = "atbtd"
    # p = "a.bc*d"        # False
    # run(s,p,False)
    # s = "aaabbb"
    # p = "aa*b*c*b"    # True
    # run(s,p,True)
    # s = "aaabbb"
    # p = ".a*.*c*b"    # True
    # run(s,p,True)
    # s = "aabbbbccc"
    # p = ".*b.*c"        # True
    # run(s,p,True)
    # s = "aabbbbcccd"
    # p = ".*c.*c."        # True
    # run(s,p,True)
    # s = "aabbbbccc"
    # p = "..*d.*c"        # False
    # run(s,p,False)
    # s = "abbccc"
    # p = ".*c.*b.*c"        # False
    # run(s,p,False)
    # s = "aa"
    # p = "a"         # False
    # run(s,p,False)
    # s = "a"
    # p = "a"          # True
    # run(s,p,True)
    # s = "a"
    # p = "aa"          # False
    # run(s,p,False)
    # s = "abcccccc"
    # p = "abb*bc*"   # False
    # run(s,p,False)
    # s = "abbcccccc"
    # p = "abb*bc*"   # True  : forward rule , backward rule
    # run(s,p,True)
    # s = "abc"
    # p = "ab*bc*"   # True : check with reverse order
    # run(s,p,True)
    # s = "aa"
    # p = "ab*"        # False
    # run(s,p,False)
    # s = "a"
    # p = "ab*"        # True
    # run(s,p,True)
    # s = "mississipppu"
    # p = "mis*is*ip*.u"    # True
    # run(s,p,True)
    # s = "mississippi"
    # p = "mis*is*ip*."        # True
    # run(s,p,True)
    # s = "acaabbaccbbacaabbbb"
    # p = "a*.*b*.*a*aa*a*"
    # run(s,p,False)
    # s = "acbbcbcbcbaaacaac"
    # p = "ac*.a*ac*.*ab*b*ac"
    # run(s,p,False)
    s = "bbcacbabbcbaaccabc"
    p = "b*a*a*.c*bb*b*.*.*"
    run(s,p,True)
