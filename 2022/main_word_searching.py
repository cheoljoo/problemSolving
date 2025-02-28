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

timeFlag = 0
debugFlag = 0
import math

# main_word_searching.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def main_word_searching(self, s) : 
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]][0] += 1   # count
                count[s[i]][1] += i   # sum of index
                count[s[i]][2].append(i+1)  # list of index
                count[s[i]][3] = i
            else :
                count[s[i]] = [1,i,[i+1],i]
        mxlist = []
        mx = -1
        mxsum = -1
        for k in count.keys():
            if mx < count[k][0]:
                mx = count[k][0]
                mxsum = count[k][1]
                mxlist.clear()
                mxlist.append(count[k][3])
            elif mx == count[k][0]:
                if mxsum < count[k][3]:
                    mxsum = count[k][3]
                    mxlist.clear()
                    mxlist.append(count[k][3])
                elif mxsum == count[k][3]:
                    mxlist.append(count[k][3])
        return [s[mxlist[0]],count[s[mxlist[0]]][2]]




           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.main_word_searching(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='main_word_searching.py',
        description=
        'main_word_searching'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('main_word_searching problem :')

    run(["banana", "lion", "tiger", "lion", "banana", "zoo", "school"],["banana",[1,5]])