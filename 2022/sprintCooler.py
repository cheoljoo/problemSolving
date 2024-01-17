# Problem
#  한 마을에 여러 농장이 존재하는데, 심한 가뭄이 들어 인공적으로 비가 내리게 할 수 있는 강수 기계를 사용해 이를 해결하고자 한다.

# 강수 기계는 농장의 위치에서만 작동 시킬 수 있으며 어떤 농장 A의 위치에서 강수 기계를 작동 시키면, A로부터 강수 범위 내에 존재하는 모든 농장에 동일한 양의 비를 내리게 할 수 있다.
# 각 농장 간의 거리는 X 좌표와 Y좌표의 차이 만큼으로 계산할 수 있다. ( i ~ j 농장 거리 : |X(i) - X(j)| + |Y(i) - Y(j)| )
# 만일 어떤 농장 A에서 필요 강우량을 모두 채웠다면, 해당 농장에는 강수 기계를 작동 시킬 수 없다.
# 단, 다른 농장에 강수 기계를 작동하였으나 농장 A이 강수 기계의 범위 안에 존재하는 경우에는 A농장에서도 비가 내리게 된다.
# 그렇다면 강수 기계를 작동 시킬 수 있는 횟수가 주어졌을 때, 필요 강우량을 만족 시킬 수 있는 최대 농장의 수를 구하라.

# Input
# 첫째 줄에는 농장의 개수 N(0<N<=10), 작동 횟수 K, 강수 기계의 범위 L, 강수 기계 작동 시 강우량 M 이 주어진다.
# 이어지는 N개의 줄에는 각 농장의 위치 좌표 Y, X와 필요 강수량 R이 주어진다.



# Output
# 최댓값 D를 출력하라. 

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
    def guestDistribution(self, roomMax: int,guest):
        q = []
        for i in range(roomMax):
            heapq.heappush(q,(0,i))
        guest.sort()
        for start,spend in guest:
            wait,room = heapq.heappop(q)
            heapq.heappush(q,(wait+spend-1,room))
            

           
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.guestDistribution(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='guestDistribution.py',
        description=
        'guestDistribution'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('guestDistribution problem :')

    run(2,[(1,2),(3,7),(4,4),(8,5)],(14,[3,1]))


