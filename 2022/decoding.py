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

# decoding.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

Encode_Table = [
    'X', 'v', 'Q', 'F', '7', '3', '5', 'g',
    'I', 'l', '6', '0', 'z', 'H', 'W', 'd',
    'B', 'e', 'p', 'f', 'J', 'b', 's', 'N',
    'T', 'u', 'r', 'S', 'K', '9', 'c', 'i',
    'k', 'x', 'C', 'w', 'U', 'n', 'j', 'Y',
    'L', '8', 'O', 'E', 'h', 'M', 'V', 't',
    'P', 'D', '4', 'G', 'R', 'y', 'a', 'm',
    '1', 'o', '2', 'A', 'Z', 'q', '+', '/']

class Solution:
    def decoding(self, s:str) -> int:
        ans = deque([])
        mat = {}
        for i in range(len(Encode_Table)):
            mat[Encode_Table[i]] = i
        s = list(s)
        sum = 0
        for i,v in enumerate(s):
            if v == '=':
                sum *= 64
            else :
                sum *=64
                sum += mat[v]
        while sum:
            print("[",chr(sum%256),"]")
            if sum%256:
                ans.appendleft(chr(sum%256))
            sum //= 256        
        return "".join(ans)


           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.decoding(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='decoding.py',
        description=
        'decoding'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('decoding problem :')

    run("BB==","A")
    run("BJI=","AB")
    run("BJlF","ABC")
    run("BJlFeX==","ABCD")