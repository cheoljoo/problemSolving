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

# warehouse.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def warehouse(self, n: List[int]) -> List[int]:
        sm = sum(n)
        if sm % len(n) != 0:
            return -1
        t = sm // len(n)  # equality target
        # ans = math.inf
        # 2개의 heapq를 사용한다. 
        # 1개는 t 보다 작은 것들로 큰 순서로 sort (커야 한번에 더 많이 가져올수 있음)
        #    추가되어야 한 값을 아래의 큰 값들에서 찾아서, 제일 큰 차이값은 제일 큰 칸에서 뽑으면 문제가 없을듯 하긴함.
        # 1개는 t 보다 큰 값들로 작은 값에서부터 가져오게 하면 된다.  여기서 나누어 사용하는 것은 아무 제약이 없기 때문이다.
        lessQ = []
        greaterQ = []
        for v in n:
            if v < t:
                heapq.heappush(lessQ,-v)
            elif v > t:
                heapq.heappush(greaterQ,v)
        count = 0
        print("lessQ:",lessQ,"greaterQ:",greaterQ,"target:",t)
        while lessQ :
            a = heapq.heappop(lessQ) * -1
            move = a // 2
            if a + move >= t:
                move = t - a

            b = heapq.heappop(greaterQ)
            print("a,b:",a,b,"move:",move,"count:",count)
            if b > move:
                b -= move
                if b != t:
                    heapq.heappush(greaterQ,b)
            elif b < move:
                move -= b
            if a+move != t:
                heapq.heappush(lessQ,(a+move)*-1)
            count += 1
            print("lessQ:",lessQ,"greaterQ:",greaterQ,"move:",move,"count:",count)
            
        return count
                    
                    

            

           
def run(s,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.warehouse(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='warehouse.py',
        description=
        'warehouse'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('warehouse problem :')

    run([4,8,2,10],4)