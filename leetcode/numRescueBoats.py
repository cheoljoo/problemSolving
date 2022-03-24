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

# numRescueBoats.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

# one moves maximum two people . it is NP problem if some people
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # peopleDict = {}
        # for p in people :
        #     if p in peopleDict:
        #         peopleDict[p] += 1
        #     else :
        #         peopleDict[p] = 1
        move = 0
        smallIndex = 0
        bigIndex = len(people)-1
        while smallIndex <= bigIndex:
            if people[smallIndex] + people[bigIndex] <= limit :
                smallIndex += 1
                bigIndex -= 1
                move += 1
            else :
                bigIndex -= 1
                move += 1
        return move
                

           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.numRescueBoats(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s ,s1, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='numRescueBoats.py',
        description=
        'numRescueBoats'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('numRescueBoats problem :')

    # run([1,2],3,1)
    run([3,2,2,1],3,3)
    run([3,5,3,4],5,4)