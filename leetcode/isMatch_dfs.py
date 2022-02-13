from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.tc = []   # forward character  / forward asterisk
        self.ta = []  # 1 is asterrisk , 0 is once
        # self.p = p
        # self.slen = len(s)
        for i in range(0,len(p)):
            if p[i] == '*' :
                continue
            if (i+1) == len(p) : # this is last character
                self.tc.append(p[i])
                self.ta.append(0)
            else :
                if p[i+1] == '*':
                    self.tc.append(p[i])
                    self.ta.append(1)
                else :
                    self.tc.append(p[i])
                    self.ta.append(0)
        
        # DFS : if find true -> OK
        return self.go(s,0,0,0)

    # DFS : if find true -> OK
    def go(self,s : str,sIndex : int,patternIndex : int,loopLevel:int) -> bool:
        
        if (sIndex == len(s)) and (patternIndex == len(self.ta)):
            return True
        elif patternIndex == len(self.ta) :
            return False
        elif sIndex == len(s) :
            for i in range(patternIndex,len(self.ta)):
                if self.ta[i] == 0:
                    # tmp = "문자는 남고 pattern은 소진"
                    # self.returnDebug(tmp,False,s,sIndex,patternIndex,loopLevel)
                    return False
            # tmp = "뒤가 모두 *형식"
            # self.returnDebug(tmp,True ,s,sIndex,patternIndex,loopLevel)
            return True
        
        # self.debug(s,sIndex,patternIndex,loopLevel)
        if self.ta[patternIndex] == 1 :
            if self.tc[patternIndex] == '.':
                for i in reversed(range(len(s) - sIndex+1)):
                    rr = self.go(s,sIndex+i,patternIndex+1,loopLevel+1)
                    # tmp = "go_return:.*(" + str(i) + ")"
                    # self.returnDebug(tmp,rr,s,sIndex,patternIndex,loopLevel+1)
                    if True == rr:
                        return True
                # tmp = "go_return:.*"
                # self.returnDebug(tmp,False,s,sIndex,patternIndex,loopLevel)
                return False
            else :
                if self.tc[patternIndex] == s[sIndex] :
                    # tmp = "go_return:match*"
                    # r1 = self.go(s,sIndex+1,patternIndex,loopLevel+1)
                    # self.returnDebug(tmp,r1,s,sIndex,patternIndex,loopLevel+1)
                    # r2 = self.go(s,sIndex,patternIndex+1,loopLevel+1)
                    # self.returnDebug(tmp,r2,s,sIndex,patternIndex,loopLevel+1)
                    # r3 = self.go(s,sIndex+1,patternIndex+1,loopLevel+1)
                    # self.returnDebug(tmp,r3,s,sIndex,patternIndex,loopLevel+1)
                    # return  r1 or r2 or r3
                    return  self.go(s,sIndex+1,patternIndex,loopLevel+1) or self.go(s,sIndex,patternIndex+1,loopLevel+1) or self.go(s,sIndex+1,patternIndex+1,loopLevel+1)
                else :
                    # tmp = "go_return:miss*"
                    # rr = self.go(s,sIndex,patternIndex+1,loopLevel+1)
                    # self.returnDebug(tmp,rr,s,sIndex,patternIndex,loopLevel+1)
                    # return rr
                    return self.go(s,sIndex,patternIndex+1,loopLevel+1)
        else :
            if self.tc[patternIndex] == '.':
                # tmp = "go_return:match"
                rr = self.go(s,sIndex+1,patternIndex+1,loopLevel+1)
                # self.returnDebug(tmp,rr,s,sIndex,patternIndex,loopLevel+1)
                return rr
                # return self.go(s,sIndex+1,patternIndex+1,loopLevel+1)
            elif self.tc[patternIndex] == s[sIndex] :
                # tmp = "go_return:match"
                rr = self.go(s,sIndex+1,patternIndex+1,loopLevel+1)
                # self.returnDebug(tmp,rr,s,sIndex,patternIndex,loopLevel+1)
                return rr
                # return self.go(s,sIndex+1,patternIndex+1,loopLevel+1)
            else :
                # tmp = "go_return:miss"
                # self.returnDebug(tmp,False,s,sIndex,patternIndex,loopLevel+1)
                return False
        # print("return")
        return True
    
    def returnDebug(self,tmp:str , ret:bool,s : str,sIndex : int,patternIndex : int,loopLevel:int) :
        # return
        print("return:",ret,sep="",end=" ")
        print(tmp,sep="",end=" ")
        self.debug(s,sIndex,patternIndex,loopLevel)
        
    def debug(self,s : str,sIndex : int,patternIndex : int,loopLevel:int) :
        # return
        print("DL:",loopLevel, sep="", end=" ")
        print("sIndex:",sIndex, sep="", end=" ")
        print("sChar:",s[sIndex], sep="", end=" ")
        print("s:",s, sep="", end=" ")
        print("patternIndex:",patternIndex, sep="", end=" ")
        print("patternChar:",self.tc[patternIndex], sep="", end=" ")
        print("pattern*:",self.ta[patternIndex], sep="", end=" ")
        # print("pattern:",self.p, sep="", end=" ")
        print("macheds:",end="")
        for i in range(sIndex):
            print(s[i],sep="",end="")
        print(end=" ")
        print("machedp:",end="")
        for i in range(patternIndex):
            print(self.tc[i],sep="",end="")
            if self.ta[i] == 1:
                print('*',sep="",end="")
        print(end=" ")
        print()

        
        
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

    s = "aa"
    p = "a"         # False
    run(s,p,False)
    s = "a"
    p = "a"          # True
    run(s,p,True)
    s = "a"
    p = "aa"          # False
    run(s,p,False)
    
    s = "abcccccc"
    p = "abb*bc*"   # False
    run(s,p,False)
    s = "abbcccccc"
    p = "abb*bc*"   # True  : forward rule , backward rule
    run(s,p,True)
    s = "abc"
    p = "ab*bc*"   # True : check with reverse order
    run(s,p,True)    
    s = "aa"
    p = "ab*"        # False
    run(s,p,False)
    s = "a"
    p = "ab*"        # True
    run(s,p,True)
    s = "atbtd"
    p = "a.bc*d"        # False
    run(s,p,False)
    s = "aaabbb"
    p = "aa*b*c*b"    # True
    run(s,p,True)
    
    s = "aaabbb"
    p = ".a*.*c*b"    # True
    run(s,p,True)
    s = "aabbbbccc"
    p = ".*b.*c"        # True
    run(s,p,True)
    s = "aabbbbcccd"
    p = ".*c.*c."        # True
    run(s,p,True)
    s = "aabbbbccc"
    p = "..*d.*c"        # False
    run(s,p,False)
    s = "abbccc"
    p = ".*c.*b.*c"        # False
    run(s,p,False)

    s = "mississipppu"
    p = "mis*is*ip*.u"    # True
    run(s,p,True)
    s = "mississippi"
    p = "mis*is*ip*."        # True
    run(s,p,True)
    s = "acaabbaccbbacaabbbb"
    p = "a*.*b*.*a*aa*a*"
    run(s,p,False)
    s = "acbbcbcbcbaaacaac"
    p = "ac*.a*ac*.*ab*b*ac"
    run(s,p,False)
    s = "bbcacbabbcbaaccabc"
    p = "b*a*a*.c*bb*b*.*.*"
    run(s,p,True)

