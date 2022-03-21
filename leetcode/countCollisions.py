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

# countCollisions.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def countCollisions(self, directions: str) -> int:
        R = [len(directions)]
        S = [len(directions)]
        count = 0
        for i in range(len(directions)):
            # print("r:",R)
            # print("s:",S)
            if directions[i] == 'L':
                rp = R[-1]
                sp = S[-1]
                if min(rp,sp) < i:
                    if rp == min(rp,sp) :
                        S.append(R.pop())
                        count += 2
                    else :
                        count += 1
                    count += len(R)-1
                    R = [R[0]]                        
            if directions[i] == 'R':
                R.append(i)
            if directions[i] == 'S':
                count += len(R)-1
                R = [R[0]]   
                S.append(i)
        #     print("count:",count)
        # print("count:",count)
        return count

           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.countCollisions(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='countCollisions.py',
        description=
        'countCollisions'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('countCollisions problem :')

    run("RLRSLL",5)
    run("LLRR",0)