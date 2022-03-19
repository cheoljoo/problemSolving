from collections import defaultdict
import enum
from re import A
#import numpy as np

import sys
import argparse
import math
import random
from tkinter import N
# https:##www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import time

# countBits.py : https:##github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class FreqStack:
    
    def __init__(self):
        self.stack = []
        self.stack.append([])
        self.stackDictToFindFast = []             # to find whether it is in or not  : dictionary is faster than list for find. 
        self.stackDictToFindFast.append({})
        self.topLevel = 0

    def push(self, val: int) -> None:
        for i in range(0,self.topLevel+2):
            if len(self.stack) <= i+2:
                self.stack.append([])
                self.stackDictToFindFast.append({})
            if not val in self.stackDictToFindFast[i]:
                self.stack[i].append(val)
                self.stackDictToFindFast[i][val] = 0
                if self.topLevel < i :
                    self.topLevel = i
                break

    def pop(self) -> int:
        p = self.stack[self.topLevel].pop()
        self.stackDictToFindFast[self.topLevel].pop(p,None)
        if len(self.stack[self.topLevel]) == 0:
            self.topLevel -= 1
        return p
           
def run():
    freqStack = FreqStack()
    freqStack.push(5) ## The stack is [5]
    freqStack.push(7) ## The stack is [5,7]
    freqStack.push(5) ## The stack is [5,7,5]
    freqStack.push(7) ## The stack is [5,7,5,7]
    freqStack.push(4) ## The stack is [5,7,5,7,4]
    freqStack.push(5) ## The stack is [5,7,5,7,4,5]
    freqStack.pop()   ## return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop()   ## return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop()   ## return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop()   ## return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='countBits.py',
        description=
        'countBits'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('countBits problem :')

    run()