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

timeFlag = 0
debugFlag = 0
import math


# minWindow.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode
# make dictionary of index of s , t
# self.loc (s) , self.target (t) 
# 1. check length of charater in target
#   it chooses the length of characters
# 2. search all combination.
#
# BEST : sliding window
#  https://leetcode.com/problems/minimum-window-substring/solution/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        self.minCount = [math.inf,0,0]
        self.loc = {}
        self.ans = [0,0,0]
        
        for i in range(len(s)):
            v = s[i]
            if v in self.loc:
                self.loc[v].append(i)
            else :
                self.loc[v] = [i]
        self.targets = {}
        left = math.inf
        right = -1
        for i in range(len(t)):
            v = t[i]
            if v in self.targets:
                self.targets[v][0] += 1
                if len(self.loc[v]) < self.targets[v][0]:
                    return ""
                left = min(left,self.loc[v][self.targets[v][0]-1])
                right = max(right,self.loc[v][self.targets[v][0]-1])
            else :
                if v in self.loc:
                    self.targets[v] = [1,len(self.loc[v]),0,self.loc[v]]
                    left = min(left,self.loc[v][0])
                    right = max(right,self.loc[v][0])
                else:
                    return ""
        # print(left,right)
        self.ans[0] = right - left
        self.ans[1] = left
        self.ans[2] = right
        while True:
            leftChar = s[left]
            for i in range(left+1,right+1):
                if s[i] in self.targets:
                    break
            left = i
            self.targets[leftChar][2] += 1
            if self.targets[leftChar][0] + self.targets[leftChar][2] > self.targets[leftChar][1]:
                break
            right = max(right,self.targets[leftChar][3][self.targets[leftChar][0] + self.targets[leftChar][2]-1])
            if self.ans[0] > right - left:
                self.ans[0] = right - left
                self.ans[1] = left
                self.ans[2] = right
        return s[self.ans[1]:self.ans[2]+1]
           
def run(s,t,expect):
    print(len(s),"",end="")
    start = time.time()
    A = Solution()
    r = A.minWindow(s,t)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minWindow.py',
        description=
        'minWindow'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minWindow problem :')

    run("wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon","ozgzyywxvtublcl","")
    run("a","b","")
    run("ADOBECAODABEABDANCBAC","ABCCDAA","ABDANCBAC")
    run("ADOBECODEBANC","ABC","BANC")
    run("a","a","a")
    run("a","aa","")