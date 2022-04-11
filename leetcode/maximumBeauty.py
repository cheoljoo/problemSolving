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
import heapq

# maximumBeauty.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

# 다시 짜자.
# 이미 target을 넘은 것을 구한다.
# target에 도달할수 있는 max를 구한다.
# 0개부터 ... target 도달 max 까지 쯕 넣어가면서

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        gardenNum = len(flowers)
        flowers.sort(reverse=True)
        self.complete = 0
        for v in flowers:
            if v >= target:
                self.complete += 1
        complete = 0
        nf = newFlowers
        for flower in flowers:
            if nf >= (target - flower):
                nf -= (target - flower)
                complete += 1
            else :
                break
        # nf를 다주어도 target만큼 안되는 요소들임.
        remain = flowers[complete:]
        heapq.heapify(remain)
        n = 0
        while remain and remain[0] != target  and  n < nf:
            heapq.heappush(remain,heapq.heappop(remain) +1)
            n += 1
        if remain:
            point1 = complete * full + remain[0] * partial
            # print(complete,remain[0],point1)
        else :
            point1 = complete * full
            # print(complete,point1)
        # point1 은 complete를 최대로 채웠을때 beauty값을 계산한 것... 그리고,  complete 수 및 min 값을 구한 것이다.  
        
        #point2는 complete를 최소한으로 채웠을때
        rflowers = sorted(flowers)
        nf = newFlowers
        for i in range(1,len(rflowers)):
            nf -= i*(rflowers[i] - rflowers[i-1])
            if nf < 0:
                break

        if nf < 0:
            mn = rflowers[i] + nf//i
        else :
            mn = rflowers[-1] + nf//len(rflowers)

        if mn >= target :  # garden마다 꽃을 다 채울수 있음. 
            point2 = (gardenNum) * full
            point3 = (gardenNum-1) * full + (target-1) * partial
        # heapq.heapify(flowers)
        # n = 0
        # while flowers[0] < target  and  n < newFlowers:
        #     heapq.heappush(flowers,heapq.heappop(flowers) +1)
        #     n += 1
        # complete =0
        # mn = math.inf
        # while flowers:
        #     n = heapq.heappop(flowers)
        #     if n >= target :
        #         complete +=1
        #     else :
        #         if mn > n:
        #             mn = n
        # if mn == math.inf:
        #     mn = 0
        else :  # garden마다 꽃을 다 채울수 없음.
            nf = newFlowers
            point2 = 0
            point3 = self.get(0,rflowers,nf, target, full, partial)
            for i in range(complete):
                if rflowers[len(rflowers)-1-i] >= target :
                    continue
                gap = target - rflowers[len(rflowers)-1-i]
                rflowers[len(rflowers)-1-i] = target
                nf -= gap
                if nf > 0 :
                    point3 = max(point3,self.get(i+1,rflowers,nf, target, full, partial))
            
        return max(point1,point2,point3)

    def get(self,lastComplete:int,rflowers: List[int], newFlowers: int, target: int, full: int, partial: int):
        nf = newFlowers
        count = 0
        for i in range(1,len(rflowers) - lastComplete):
            nf -= i*(rflowers[i] - rflowers[i-1])
            if nf < 0:
                count = i
                break

        if nf < 0:
            mn = rflowers[count] + nf//count
        else :
            mn = rflowers[len(rflowers) - lastComplete -1] + nf//(len(rflowers) - lastComplete)
        
        if mn >= target :  # garden마다 꽃을 다 채울수 있음. 
            # nf가 남았다는 것은 우리가 원하는 모두가 흩뿌려지는 것이 아닌 , 뭔가는 찾다는 것이고 이건 다른 경우에 계산이 되어진 것이다.
            return 0
        else :
            a = (lastComplete + self.complete)*full
            b = mn*partial
            return a + b
        
def run(s,s1,s2,s3,s4,expect):
    # print(s,end="")
    start = time.time()
    A = Solution()
    r = A.maximumBeauty(s,s1,s2,s3,s4)
    print(len(s) , " total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maximumBeauty.py',
        description=
        'maximumBeauty'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maximumBeauty problem :')

#     run([1,3,1,1], 7,6,12,1,14)
#     run([2,4,5,3],10,5,2,6,30)
#     run([19,17,6,9,19],24,10,17,4,104)
#     run([20,1,15,17,10,2,4,16,15,11],2,20,10,2,14)
#     run([1056,73246,24730,45592,2076,47062,51329,30904,77941,93853,99362,35655,37069,29547,75748,19177,15083,62416,38012,63192,22196,66038,70061,61813,17744,75195,91086,16455,62569,376,99843,75705,63131,64017,90656,79076,69391,39275,70667,87360,86690,42416,99339,7827,5112,93538,31350,75264,72815,97536,76295,8700,35630,99048,9193,71976,66667,41722,9016,83118,22486,93533,11894,22471,69541,34613,2290,50824,77760,89037,71688,91386,41314,63112,74778,97032,64333,11903,42272,46057,48163,72195,44974,14659,94983,29406,75337,83095,87638,13317,53059,87590,3989,80643,9239,94515,22388,87053,33189]
# ,4141897
# ,100000
# ,62283
# ,17678,1696054247)
#     run([8,2]
# ,24
# ,18
# ,6
# ,3,54)
#     run([5,19,1,1,6,10,18,12,20,10,11]
# ,6
# ,20
# ,3
# ,11,47) 
#     run([89287,5538,37141,72522,84502,44451,24432,2324,72779,57060,99178,6,29440,53664,76197,46742,17384,22072,33067,66274,19323,72943,12914,91475,96826,84847,28100,89590,34977,74052,4813,24563,97491,71687,8533,49262,2265,10553,63902,19647,27006,64548,89892,64046,72766,34623,17297,21417,70630,93469,83379,19483,93842,65968,28401,1889,24441,99401,37907,13794,3640,95432,36875,10200,95360,10829,96763,15900,8490,68972,52537,72458,95269]
# ,42
# ,4534
# ,32415
# ,11040,2734140)
    run([75827,28680,81903,52486,91395,73466,66984,13440,48757,55165,27686,2415,40618,54653,67084,86405,52528,37671,13695,33870,25493,85037,71795,20915,2166,44293,91381,59851,51309,95966,36665,35444,65473,64343,81177,74772,85450,68906,35751,75031,68610,84091,87426,78383,59245,22170,3767,1504,585,57933,50166,19281,80334,1019,35812,48926,43076,22510,13669,9240,9190,41086,61005,65352,34509,7558,94252,53745,44108,46721,772,90294,69197,94924,5699,48353,70394,11750,28125,33217,26686,59289,95048,9141,22531,87251,21173,17070,3880,74803]
,2615793
,92430
,61384
,4170,309396826)