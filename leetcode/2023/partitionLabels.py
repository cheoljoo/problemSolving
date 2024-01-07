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

# partitionLabels.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else :
                freq[c] = 1
        r = []
        p = 0
        stack = {}
        for (i,c) in enumerate(list(s)) :
            freq[c] -= 1
            if freq[c] == 0 :
                stack.pop(c,None)  # pop
                if len(stack.keys()) == 0:
                    r.append(i+1-p)
                    p = i+1
            else :
                stack[c] = 0  # push
        return r
        
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.partitionLabels(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='partitionLabels.py',
        description=
        'partitionLabels'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('partitionLabels problem :')

    run("ababcbacadefegdehijhklij",[9,7,8])
    run("eccbbbbdec",[10])