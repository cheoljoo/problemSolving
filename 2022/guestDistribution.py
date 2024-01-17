# 어느 행사장에 0번 부터 N-1번 까지의 행사 부스가 존재하는데 특정한 방식으로 행사장에 찾아온 손님들을 분배하려고 한다.
# 행사장에 손님이 도착하면 손님은 도착시간에 대기인원이 가장 적은 부스를 선택해 대기하게 된다.
# 만일 대기인원이 동일한 부스가 존재한다면 부스의 번호가 더 적은 부스에서 대기한다.
# 한 부스에서는 한명의 손님만이 이용할 수 있으며, 대기인원은 앞사람의 이용시간이 끝나고 난 뒤에 부스를 이용할 수 있다.
# 위와 같은 방식으로 손님을 맞이했을 때, 각 손님의 도착시간과 소요시간을 입력으로 받아 행사의 예상 종료시간을 출력하고 각 부스에서 맞이하게 될 손님의 수를 출력하시오.

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


