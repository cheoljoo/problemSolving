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

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        if n == 1:
            return 0
        q = [(1,0)]  # (len , val)  we do not need the exact array
        for i in range(2,n+1):
            # print("i:",i,"n:",n,"k:",k,"q:",q)
            nq = []
            while q:
                (l,v) = q.pop(0)
                for p in range(l+1):
                    nq.append((i,v+p))
            q = nq
        # print("n:",n,"k:",k,"q:",q)
        cnt = 0
        for l,v in q:
            if v == k:
                cnt += 1
        return cnt
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.kInversePairs(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='kInversePairs.py',
        description=
        'kInversePairs'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('kInversePairs problem :')


    run(10,15,110010)
    run(15,15,19664205)
    run(30,15,688272989)
    run(50,15,932975515)
    run(70,15,404529997)
    run(100,15,687491764)
    
# $  python3 kInversePairs.py
# kInversePairs problem :
#  total_time1 :  26.13805365562439 -> SUCCESS -> 110010 10



# 1 0 1 [1] 
# 2 0 1 [1,2](0) oldVal=0  oldLen=2
# 2 1 1 [2,1](1) oldVal=1  oldLen=2
# 3일때 
# [3,1,2](oldLen + oldVal=0) [1,3,2](oldLen-1 + oldVal) [1,2,3] (oldLen-2 + oldVal)
# [3,2,1](oldLen + oldVal=1) [2,3,1] [2,1,3]
# 3 0 1 [1,2,3]
# 3 1 2 [2,1,3] [1,3,2]
# 3 2 2 [3,2,1] [3,1,2]
# 4 1 3
# 4 2 5

# q 갯수 증가
# 1 -> 1 
# 2 -> 2 * 1
# 0 1
# 3 ->  3* 2
# 0 1 2
# 1 2 3
# 4 -> 4 * 3 * 2 

# q Val 구조
# 4일대 위처럼 24개로 4 * 6
# 0 1 2 3
# 1 2 3 4
# 2 3 4 5
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6

# 5* 4 * (3*2)
# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7

# ...



# n일때 아래 내용을 n * n-1 * (n-2*...*1)
# (n-2*...*1)까지 할 필요가 없고  k 까지만 하면 된다.
# 0 1 2 ... n-1
# 1 2 3 ... n
# ...
# n-2 ...   2n-3

# 1 2 3 ... n
# ...
# n-2 ...   2n-3
# n-1 ...   2n-2

# k <= 1000
# 위의 것을 max 1000번만 더하면 된다.
# 처음 start하는 값이 k이면 그게 끝.

# # this is timeout
# i: 2 n: 3 k: 10 q: [(1, 0)]
# i: 3 n: 3 k: 10 q: [(2, 0), (2, 1)]
# n: 3 k: 10 q: [(3, 0), (3, 1), (3, 2), (3, 1), (3, 2), (3, 3)]
# i: 2 n: 3 k: 1 q: [(1, 0)]
# i: 3 n: 3 k: 1 q: [(2, 0), (2, 1)]
# n: 3 k: 1 q: [(3, 0), (3, 1), (3, 2), (3, 1), (3, 2), (3, 3)]
# i: 2 n: 3 k: 2 q: [(1, 0)]
# i: 3 n: 3 k: 2 q: [(2, 0), (2, 1)]
# n: 3 k: 2 q: [(3, 0), (3, 1), (3, 2), (3, 1), (3, 2), (3, 3)]
# i: 2 n: 4 k: 1 q: [(1, 0)]
# i: 3 n: 4 k: 1 q: [(2, 0), (2, 1)]
# i: 4 n: 4 k: 1 q: [(3, 0), (3, 1), (3, 2), (3, 1), (3, 2), (3, 3)]
# n: 4 k: 1 q: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 1), (4, 2), (4, 3), (4, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 3), (4, 4), (4, 5), (4, 6)]
# i: 2 n: 4 k: 2 q: [(1, 0)]
# i: 3 n: 4 k: 2 q: [(2, 0), (2, 1)]
# i: 4 n: 4 k: 2 q: [(3, 0), (3, 1), (3, 2), (3, 1), (3, 2), (3, 3)]
# n: 4 k: 2 q: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 1), (4, 2), (4, 3), (4, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 3), (4, 4), (4, 5), (4, 6)]


# 7
# 15
# 1
# 0
# 1
# 1
# 1
# 2
# 3
# 10
# 3
# 0
# 3
# 1
# 3
# 2
# 4
# 1
# 4
# 2