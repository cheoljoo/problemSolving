from collections import defaultdict
from re import A
#import numpy as np

import sys
import argparse
import math
import random
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import bisect
import time

# minimumDeviation5.py in https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def __init__(self):
        self.maxOddValue = 0
    def minimumDeviation(self, nums: List[int]) -> int:
        # start_sort = time.time()
        nums.sort()
        
        self.minDeviation = nums[-1] - nums[0]
        self.getMaxOddValue(nums)
        # print("sort time :", time.time() - start_sort , "-> ", end="")
        self.do2(nums)
        self.do3(nums)
        self.do4(nums)
        return self.minDeviation
    
    def getMaxOddValue(self,nums) -> None:
        # find largest odd number
        # 1. find all(N:partial) and divide (logN) -> NlogN  : no change nums : great
        # 2. divide(logN) and insert(logN) from the end (N:partial) -> 2NlogN : change nums 
        for a in reversed(nums):
            if a % 2 == 0:
                o = a
                while a % 2 == 0:
                    a = a // 2
                if self.maxOddValue < a:
                    self.maxOddValue = a
            else :
                if self.maxOddValue < a:
                    self.maxOddValue = a
                break  

    def remove_all_by_value(self,nums,value) -> int: # return : remove count
        count = 0
        while value in nums :
            nums.remove(value)
            count += 1
        return count
            
    def do2(self,nums):
        # start = time.time()
        # fold all even number until below maxOddNumber if deviation will reduce
        
        # while True:
        #     a = nums[-1]
        #     if (self.maxOddValue < a) and (a % 2 == 0):
        #         o = a
        #         a = a // 2
        #         if abs(self.maxOddValue - a) < abs(self.maxOddValue - o):
        #             # count = self.remove_all_by_value(nums, o)
        #             # for _ in range(count):
        #             #     bisect.insort(nums,a)
        #             i = -1  
        #             while (abs(i) <= len(nums)) and (nums[i] == o):
        #                 nums[i] = a
        #                 i -= 1
        #             nums.sort()
        #             # update and sort is faster than update-insert each elements 
        #             # length(10000) 1.0s -> 0.2
        #         else:
        #             break  
        #     else :
        #         break
        
        for i in reversed(range(len(nums))):
            o = nums[i]
            a = o // 2
            if (self.maxOddValue < o) and (o % 2 == 0):
                while abs(self.maxOddValue - a) < abs(self.maxOddValue - o):
                    nums[i] = a
                    o = a
                    a = o // 2
            else :
                break    
        nums.sort()
        
        if self.minDeviation > nums[-1]-nums[0]:
            self.minDeviation = nums[-1]-nums[0] 
        # print("do2 time :", time.time() - start , "-> ", end="")    
                  
    def do3(self,nums):
        # start = time.time()
        # all double until below maxOddNumber
        while (nums[0] < self.maxOddValue) and (nums[0]%2 == 1):
            a = nums[0]
            o = a
            a = a*2
            if abs(self.maxOddValue - a) < abs(self.maxOddValue - o):
                count = self.remove_all_by_value(nums, o)
                for _ in range(count):
                    bisect.insort(nums,a) 
            else :
                break
        if self.minDeviation > nums[-1]-nums[0]:
            self.minDeviation = nums[-1]-nums[0] 
        # print("do3 time :", time.time() - start , "-> ", end="") 

    def do4(self,nums) -> None :
        # start = time.time()
        isChanged = True
        while isChanged == True:
            isChanged = False
            if len(nums) <= 1:
                break
            if nums[0] % 2 == 1 :   # remove first element and add first element *2
                # a = nums[0]
                # count = self.remove_all_by_value(nums, a)
                # # a = nums.pop(oddIndex)
                # for _ in range(count):
                #     bisect.insort(nums,a*2)
                # deviation = nums[-1] - nums[0]
                # if self.minDeviation > deviation:
                #     self.minDeviation = deviation
                #     isChanged = True
                # else :
                #     # nums.remove(a*2)
                #     for _ in range(count):
                #         nums.remove(a*2)
                #         bisect.insort(nums,a)
                min = nums[0]
                for i in range(1,len(nums)):
                    if min != nums[i]:
                        min = nums[i]
                        break
                max = nums[-1]
                if max < nums[0]*2 : 
                    max = nums[0]*2
                if self.minDeviation > max - min :
                    self.minDeviation = max - min
                    i = 0
                    min = nums[0]
                    while (i < len(nums)) and (nums[i] == min):
                        nums[i] = min*2
                        i += 1
                    nums.sort()
                    
            if nums[-1] % 2 == 0:
                # a = nums[-1]
                # count = self.remove_all_by_value(nums, a)
                # # a = nums.pop(evenIndex)
                # for _ in range(count):
                #     bisect.insort(nums,a//2)
                # deviation = nums[-1] - nums[0]
                # if self.minDeviation > deviation:
                #     self.minDeviation = deviation
                #     isChanged = True
                # else :
                #     for _ in range(count):
                #         nums.remove(a//2)
                #         bisect.insort(nums,a)
                max = nums[-1]
                for i in reversed(range(len(nums)-1)):
                    if max != nums[i]:
                        max = nums[i]
                        break
                min = nums[0]
                if min > nums[-1]//2 : 
                    min = nums[-1]//2
                if self.minDeviation > max - min :
                    self.minDeviation = max - min
                    max = nums[-1]
                    for i in reversed(range(len(nums))):
                        if nums[i] == max:
                            nums[i] = max//2
                        else:
                            break
                    nums.sort()
        # print("do4-1 time :", time.time() - start , "-> ", end="") 
        # update and sort is faster than remove-insert each elements 
        # length(10000) 0.5s -> 0.0
        
        
        # t = nums.copy()        
        # # print("t:",t)
        # while (t[-1]%2 == 0) and (t[-1] > self.maxOddValue) :
        #     a = t[-1]
        #     count = self.remove_all_by_value(t, a)
        #     # a = nums.pop(evenIndex)
        #     for _ in range(count):
        #         bisect.insort(t,a//2)
        #     deviation = t[-1] - t[0]
        #     if self.minDeviation > deviation:
        #         self.minDeviation = deviation
        
        # start = time.time()        
        min = nums[0]
        max = nums[-1]
        for i in reversed(range(len(nums))):
            if (nums[i]%2 == 0) and (nums[i] > self.maxOddValue) :
                if i > 0:
                    max = nums[i-1]
                    if min > nums[i]//2 : 
                        min = nums[i]//2
                    if self.minDeviation > max - min:
                        self.minDeviation = max - min
                else :
                    print("T.error : i == 0 :",nums[0], nums[i], nums[len(nums)-1], self.maxOddValue)
            else :
                break
        # print("do4-2 time :", time.time() - start , "-> ", end="")
         
        # start = time.time()
        # b = nums.copy()
        # # print("b:",b)
        # while (b[0]%2 == 1) and (b[0] < self.maxOddValue) :
        #     a = b[0]
        #     count = self.remove_all_by_value(b, a)
        #     # a = nums.pop(evenIndex)
        #     for _ in range(count):
        #         bisect.insort(b,a*2)
        #     deviation = b[-1] - b[0]
        #     if self.minDeviation > deviation:
        #         self.minDeviation = deviation  
        min = nums[0]
        max = nums[-1]
        for i in range(len(nums)):
            if (nums[i]%2 == 1) and (nums[i] < self.maxOddValue) :
                if i < len(nums)-1:
                    min = nums[i+1]
                    if max < nums[i]*2 : 
                        max = nums[i]*2
                    if self.minDeviation > max - min:
                        self.minDeviation = max - min
                else :
                    print("B.error : i == len()-1 :",nums[0],nums[i], nums[len(nums)-1], self.maxOddValue)
            else :
                break
        # print("do4-3 time :", time.time() - start , "-> ", end="") 
        
 
 
def run(s,expect):
    start = time.time()
    a = Solution()
    o = s.copy()
    r = a.minimumDeviation(s)
    print("  total_time :", time.time() - start , "-> ", end="") 
    print("len(%d) "%len(s),end="")
    if r == expect:
        print("SUCCESS >> ",end="")
    else :
        print("ERROR (", expect,") >> ",sep="",end="")
    print(r , ":",end="")
    if  len(s) < 100:
        print(s,o,end="")
    print()
    # sort time : 0.0 -> do2 time : 0.2184154987335205 -> do3 time : 0.0 -> do4-1 time : 0.0 -> do4-2 time : 0.0 -> do4-3 time : 0.0 ->   total_time : 0.22439837455749512 -> len(10000)
    # sort time : 0.0 -> do2 time : 0.6432626247406006 -> do3 time : 0.0 -> do4-1 time : 0.0 -> do4-2 time : 0.001994609832763672 -> do4-3 time : 0.0 ->   total_time : 0.6572427749633789 -> len(20000)
    # sort time : 0.0009975433349609375 -> do2 time : 21.690882444381714 -> do3 time : 0.0 -> do4-1 time : 0.0009968280792236328 -> do4-2 time : 0.006982088088989258 -> do4-3 time : 0.0 ->   total_time : 21.740752696990967 -> len(100000)
    

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/minimize-deviation-in-array/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='minimumDeviation.py',
        description=
        'minimumDeviation'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minimumDeviation problem:')
    
    s = [1,2,3,4]
    run(s,1)
    s = [4,1,5,20,3]
    run(s,3)
    s = [2,10,8]
    run(s,3)
    s = [2,8,6,1,6]
    run(s,1)
    s = [2,2]
    run(s,0)
    s = [16,16]
    run(s,0)
    s = [16]
    run(s,0)
    s = [139502287,127662367,182874278,195316256,158258043,128106398,165570519,161630895,197087073,177018029,142241150,189463437,114131106,180827841,140563651,140631914,127439843,117651449,108277946,148148621,198133057,173477124,180664549,119749615,192791912,171503536,146780066,146619923,180198468,132326257,129079222,142091904,115753487,178875891,171861205,165113533,105888611,148201456,114722931,111227228,139403775,192371264,112237013,173895760,188650252,109366482,174511822,108640913,191279346,127663274,180400034,179515445,109423556,191502543,108986309,163189619,168756945,177284541,114642866,136718954,146122849,186435019,108451832,162317887,137725843,138164718,170588551,159632836,139405555,105243015,187461591,156505003,163176045,107100346,124266013,198186644,160653221,157330716,188843428,130131460,136191103,120065496,143836292,194312999,108470642,166356073,192320235,101600108,170925551,197600861,149364536,158492279,166594704,141871659,197119385,187931161,141314732,124536617,102505057,142054441,142144983,139492998,114061225,172915905,186326112,101258267,176016355,117310304,134565576,175774728,115461652,173657901,150872767,127024993,164739980,199913646,140093586,140579776,115345543,115718199,111611931,189004451,117768984,160145942,103569746,150336410,166224862,129187299,147130259,158224131,167485119,115017904,104014213,149432483,102127258,199320902,193569603,157552714,113431868,165365010,162721361,169993800,130956004,123456024,157811076,167771287,103114996,183508477,171322947,103516387,118407455,111055030,161774593,106983428,187953441,186774576,106113788,124972645,140254982,102498490,186169756,112171085,181140323,127509228,139727086,170141845,102263907,125782453,198344152,132630801,135853494,171044990,143562844,128452102,166392273,154488151,125841090,155342972,118665099,183467485,105245785,173770396,182229265,102072773,137044502,148387216,139608067,141567001,150810789,114476348,163267954,164259991,165425337,152560087,193558089,180008386,154925409,153149280,144881521,161927809,103701602,124355592,199332316,164457368,184521526,176380601,132487910,136872491,124394249,178518694,129959078,168807287,165621480,142432287,186679088,142687756,149852668,137400257,130710611,177159816,143972099,179566227,139405172,125527818,138882615,192825874,115915326,176351775,149859250,196724440,188496780,102484169,138858670,135845950,187121403,165486776,143305183,167154441,171152787,178418731,155915678,138488715,176113588,133032247,135266151,150545120,193146386,100587965,105628049,127805067,100092626,119758139,174858873,145984705,192910027,181173340,138042671,122308978,160770301,130394674,166492711,161910843,119184450,109853721,170848534,121342141,100838796,198131866,156427959,176020777,184930698,117558856,113507815,153587163,123588933,120472984,198163856,107901250,182464664,128964739,138765154,197553755,190480953,169538709,105129765,143353678,199607036,144583353,199403460,195738467,124778611,186233414,168628878,101977678,160897452,195801072,186941874,177230274,179583881,133909934,175430770,158050009,141158921,159321118,192978346,153948939,147725900,128959020,152949311,173602535,195643978,120013972,142084051,136108423,121580658,145565683,156257215,199766954,187813699,171156531,162645972,100216855,139697220,182202999,147699018,110023818,176058211,185321487,176811279,100190707,135798617,116045000,140572589,172900728,116145251,140651548,165834418,116121994,186652919,103162165,164716217,117471904,155970321,113282879,105493962,103599601,188489301,155340595,136108503,127347508,194267446]
    run(s,98683701)
    s = [399,908,648,357,693,502,331,649,596,698]
    run(s,315)
    s = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
    run(s,17)
    s = []
    # for i in range(2,200002,2) : 
    for i in range(2,200002,2) : 
        s.append(i)
    run(s,315)