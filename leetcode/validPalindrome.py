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

# validPalindrome.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        start = 0
        end = len(s)-1
        while True:
            if start >= end:
                return True
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                if start+1 == end:
                    return True
                if self.isPalindrom(s,start+1,end) or self.isPalindrom(s,start,end-1) :
                    return True
                else : 
                    return False 

    def isPalindrom(self,s:str,start:int,end:int) -> bool:
        while True:
            if start >= end:
                return True
            if s[start] == s[end]:
                start += 1
                end -= 1
            else :
                return False
        return False
           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.validPalindrome(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='validPalindrome.py',
        description=
        'validPalindrome'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('validPalindrome problem :')

    run("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",True)
    run("aba",True)
    run("a",True)
    run("abc",False)
    run("abca",True)
    run("acba",True)
    run("abcdba",True)
    run("acbbdca",True)
    run("acbcad",True)
    run("ad",True)
    run("add",True)
    run("adf",False)
    run("abffcda",False)