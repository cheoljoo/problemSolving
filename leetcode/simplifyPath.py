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

# simplifyPath.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split('/')
        list = []
        for v in elements:
            if v == "..":
                if len(list) == 0:
                    pass
                else :
                    list.pop()
            elif v == ".":
                pass
            elif v == "":
                pass
            else:
                list.append(v)
        return '/' + '/'.join(list)
        
                
            

           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.simplifyPath(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='simplifyPath.py',
        description=
        'simplifyPath'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('simplifyPath problem :')

    run("/../","/")
    run("/home//foo/","/home/foo")