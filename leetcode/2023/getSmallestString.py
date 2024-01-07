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

# getSmallestString.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z = self.getNum('z')
        zNum = 0
        while True:
            countOfZ = (k - n) // z
            zNum += countOfZ
            remainN = n - countOfZ
            remainK = k - countOfZ * z
            if remainK - remainN >= z :
                k = remainK
                n = remainN
            else :
                break
        if remainN == remainK :
            return  'a'*(remainN) + 'z'*zNum
        else :
            i = remainK - (remainN-1)
            return  'a'*(remainN-1) + chr(i + ord('a')-1) + 'z'*zNum
        return ''
            
    def getNum(self,ch) -> int :
        return ord(ch) - ord('a') + 1
           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.getSmallestString(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='getSmallestString.py',
        description=
        'getSmallestString'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('getSmallestString problem :')

    run(3,27,'aay')
    run(5,73,'aaszz')
    run(50,80,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafz')
    run(1,26,'z')
    run(1,2,'b')
    run(2,52,'zz')
    run(3,3,"aaa")
    run(90,200,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaakzzzz")
    run(90,1121,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaagzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    
