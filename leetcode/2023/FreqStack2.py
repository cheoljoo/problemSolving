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
        self.topLevel = 0

    def push(self, val: int) -> None:
        for i in range(0,self.topLevel+2):
            if len(self.stack) <= i+2:
                self.stack.append([])
            if not val in self.stack[i]:
                self.stack[i].append(val)
                if self.topLevel < i :
                    self.topLevel = i
                break

    def pop(self) -> int:
        p = self.stack[self.topLevel].pop()
        if len(self.stack[self.topLevel]) == 0:
            self.topLevel -= 1
        return p


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# list를 쌓을수 있는 max stack size만큼이 될 것이고 , 20000 으로 크지 않다.  이것은 frequence가 될 것이다. 
# 각 element는 dictionary로 구성하자...  
# dictionary에는 value:0 로 뒤에 추가 (위치는 필요없음)  맨 뒤에 추가
#    dictionary가 list 보다 같은 값이 있는지를 찾는데 빠르기 때문이다.
# 그림으로 보면  
# freqStack.push(5); ## The stack is [5]
#    stack[0] = {5}
# freqStack.push(7); ## The stack is [5,7]
#     stack[0] = {5,7}   7 is recent 
# freqStack.push(5); ## The stack is [5,7,5]
#     stack[1] = {5}
#     stack[0] = {5,7}
# freqStack.push(7); ## The stack is [5,7,5,7]
#     stack[1] = {5,7}
#     stack[0] = {5,7}
# freqStack.push(4); ## The stack is [5,7,5,7,4]
#     stack[1] = {5,7}
#     stack[0] = {5,7,4}
# freqStack.push(5); ## The stack is [5,7,5,7,4,5]
#     stack[2] = {5}     <- top stack level
#     stack[1] = {5,7}
#     stack[0] = {5,7,4}

# freqStack.pop();   ## return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
#     stack[2] = {}
#     stack[1] = {5,7}   <- top stack level
#     stack[0] = {5,7,4}
# freqStack.pop();   ## return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
#     stack[2] = {}
#     stack[1] = {5}   <- top stack level
#     stack[0] = {5,7,4}
# freqStack.pop();   ## return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   ## return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
           
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