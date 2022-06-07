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
from bisect import bisect_left , bisect_right

timeFlag = 0
debugFlag = 0
import math

# kmelon.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def kmelon(self, n: int , s : List[List[int]]) -> int:
        # 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
        x , y = 0 , 0
        point = set()
        point.add((x,y))
        mxX , mxY = 0, 0
        mnX , mnY = 0, 0
        for i in range(len(s)):
            if s[i][0] == 1:
                x += s[i][1]
                mxX = max(x,mxX)
                mnX = min(x,mnX)
            elif s[i][0] == 2 :
                x -= s[i][1]
                mxX = max(x,mxX)
                mnX = min(x,mnX)
            elif s[i][0] == 3 : 
                y -= s[i][1]
                mxY = max(y,mxY)
                mnY = min(y,mnY)
            else :
                y += s[i][1]
                mxY = max(y,mxY)
                mnY = min(y,mnY)
            point.add((x,y))
        # 빈 꼭지점을 찾는다.
        p = [(mxX,mxY), (mxX,mnY), (mnX,mxY), (mnX,mnY)]
        for x1,y1 in p:
            if (x1,y1) not in point:
                break
        x1y = [y1]
        for x2,y2 in point:
            if x1 == x2:
                 x1y.append(y2)
        y1x = [x1]
        for x2,y2 in point:
            if y1 == y2:
                 y1x.append(x2)
        print("x1y",x1y)
        print("y1x",y1x)
        yL = max(abs(x1y[2]-x1y[0]),abs(x1y[1]-x1y[0]))
        yS = min(abs(x1y[2]-x1y[0]),abs(x1y[1]-x1y[0]))
        xL = max(abs(y1x[2]-y1x[0]),abs(y1x[1]-y1x[0]))
        xS = min(abs(y1x[2]-y1x[0]),abs(y1x[1]-y1x[0]))
        return n *(yL*xL - yS*xS)
        
           
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.kmelon(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='kmelon.py',
        description=
        'kmelon'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('kmelon problem :')

    run(7,[[2,160],[3, 30],[1, 60],[3, 20],[1, 100],[4, 50]],47600)
    run(17,[[1, 57],[3, 18],[1, 382],[4, 471],[2, 439],[3, 453]],3497631)
