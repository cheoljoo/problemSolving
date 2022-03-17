from collections import defaultdict
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

# pirateJewel.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def pirateJewel(self, s1,s2) -> int:
        sum = []
        for (i,v) in enumerate(s1):
            sum.append((v + s2[i],v,s2[i],i))
        sum.sort()
        count = 0
        ret = 0
        for (_,v1,v2,_) in reversed(sum):
            if count %2 == 0:
                ret += v1
            else :
                ret -= v2
            count += 1
        return ret
           
def run(s,s2,expect):
    start = time.time()
    A = Solution()
    r = A.pirateJewel(s,s2)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r,s ,s2, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='pirateJewel.py',
        description=
        'pirateJewel'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('pirateJewel problem :')

    run([10,100,2],[5,90,0],97)
    run([90,5,0],[100,10,2],80)
    run([10,100,50],[100,10,60],50)
    run([20,15,5,8],[10,20,8,9],5)
    run([0,0,0],[100,1000,10],-100)

