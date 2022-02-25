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

# compareVersion.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = list(map(int,version1.split('.')))
        s2 = list(map(int,version2.split('.')))
        self.removeLastZeros(s1)
        self.removeLastZeros(s2)
        i = 0
        while (i < len(s1)) and (i < len(s2)):
            if s1[i] < s2[i] :
                return -1
            elif s1[i] > s2[i] :
                return 1
            i += 1
        if i == len(s1) and i == len(s2) :
            return 0
        elif i == len(s1) :
            return -1
        elif i == len(s2) :
            return 1
        return 0
                
    def removeLastZeros(self,s:List[int]) -> None :
        for (i,v) in enumerate(reversed(s)) :
            if v == 0 :
                s.pop()
            else :
                return
        return
        
        
            
def run(s1,s2,expect):
    start = time.time()
    A = Solution()
    r = A.compareVersion(s1,s2)
    print(" total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(s1,s2 , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='compareVersion.py',
        description=
        'compareVersion'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('compareVersion problem :')


    run("1.01","1.001",0)
    run("1.0","1.0.0",0)
    run("0.1","1.1",-1)
    run("1.1.1","1.1",1)
    

    
    