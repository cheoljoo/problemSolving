from collections import defaultdict
import enum
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

import time

# getSkyline2.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 1
debugFlag = 0
class Solution:
    def __init__(self):
        self.startIdx = 0
        self.startSortIndex = 0
        self.endSortIndex = 0
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start = time.time()
        endSort = sorted(buildings,key=lambda x: x[1]*(2**32)+x[0])
        buildings.sort(key=lambda x: x[0]*(2**32)+x[1])
        startSort = buildings
        if timeFlag : print(" sort(%d):"%len(buildings), time.time() - start , "-> ", end="")
        
        if debugFlag : print("startSort:",buildings)
        if debugFlag : print("endSort:",endSort)
        # p = 11
        # a = min(enumerate(buildings), key=lambda x: abs(x[1][0]-11) if x[1][0] < p else math.inf)
        # print(a)
        
        # combine x1,x2 with up(x1)/down(x2) info
        start = time.time()
        size_1 = len(startSort)
        size_2 = len(endSort)
        res = []
        i, j = 0, 0
        while i < size_1 and j < size_2:
            if buildings[i][0] < endSort[j][1]:
                res.append([buildings[i][0],1,buildings[i][2]])
                i += 1
            else:
                res.append([endSort[j][1],0,endSort[j][2]])
                j += 1
        if i == size_1:
            for ii in range(j,len(endSort)):
                res.append([endSort[ii][1],0,endSort[ii][2]])
        if j == size_2:
            for ii in range(j,len(buildings)):
                res.append([buildings[ii][0],1,buildings[ii][2]])
        if debugFlag : print("res:",res)  # list[x,up:1/down:0]
        if timeFlag : print(" combine(%d):"%len(buildings), time.time() - start , "-> ", end="")
        
        start = time.time()
        r = []
        for (x,isUp,h) in res:
            if isUp == 1:  # up
                # l1 : [x1,x2,height]
                # enumerate() -> (index,[x1,x2,height])
                # minIdx = self.minIndexLessThanX(endSort,x)
                if debugFlag : print("UP x :",x,"idx :",end="")
                hmax = 0
                count = 0
                for i in range(self.startSortIndex,len(startSort)):
                    if startSort[i][1] <= x :
                        self.startSortIndex = i
                        break         
                for i in range(self.startSortIndex,len(startSort)):
                    if startSort[i][0] > x :
                        break
                    if startSort[i][0] <= x and x < startSort[i][1]: 
                        if hmax < startSort[i][2]: 
                            hmax = startSort[i][2]
                            count = 1
                        elif hmax == startSort[i][2]: 
                            count += 1
                        if debugFlag :print(" ->%d(%d..%d)H%d"%(i,startSort[i][0],startSort[i][1],startSort[i][2]), end="")
                if debugFlag : print(" hmax :",hmax , end="")
                if debugFlag : print(" #%d"%count , end="")
                if hmax == h : # and count == 1:
                    if debugFlag : print(" HIGH " , end="")
                    # if len(r)>0 :
                    #     if r[-1][0] != x : 
                    #         if r[-1][1] != hmax:
                    #             r.append([x,hmax])
                    #     elif r[-1][0] == x :
                    #         if r[-1][1] < hmax:
                    #             r[-1][1] = hmax
                    # else :
                    #     r.append([x,hmax])
                    r.append([x,hmax])
                    if debugFlag : print("          ",r,end="")
                if debugFlag : print()
        if timeFlag : print(" up(%d):"%len(res), time.time() - start , "-> ", end="")
        start = time.time()        
        for (x,isUp,h) in res:
            # else :   # isUp == 0: down
            if isUp != 1:  # up
                # l1 : [x1,x2,height]
                # enumerate() -> (index,[x1,x2,height])
                # minIdx = self.minIndexLessThanX(endSort,x)
                if debugFlag : print("dn x :",x,"idx :",end="")
                hmax = 0
                hmax2nd = 0
                count = 0
                for i in range(self.endSortIndex,len(endSort)):
                    if endSort[i][1] > x : # x is endPosition
                        self.endSortIndex = i
                        break
                                        
                for i in range(self.endSortIndex,len(endSort)):
                    if endSort[i][0] < x and x < endSort[i][1]: 
                        if hmax < endSort[i][2]:
                            hmax2nd = hmax 
                            hmax = endSort[i][2]
                            count = 1
                        elif hmax == endSort[i][2]:
                            count += 1
                        else :
                            if hmax2nd < endSort[i][2]:
                                hmax2nd = endSort[i][2]
                        if debugFlag :print(" ->%d(%d..%d)H%d"%(i,endSort[i][0],endSort[i][1],endSort[i][2]), end="")
                if debugFlag : print(" hmax :",hmax , end="")
                if debugFlag : print(" #%d"%count , end="")
                if debugFlag : print(" hmax2nd :",hmax2nd , end="")
                # if hmax == h and count == 1:
                if debugFlag : print(" HIGH " , end="")
                    # if len(r)>0 :
                    #     if r[-1][0] != x : 
                    #         if r[-1][1] != hmax2nd:
                    #             r.append([x,hmax2nd])
                    #     elif r[-1][0] == x :
                    #         if r[-1][1] < hmax2nd:
                    #             r[-1][1] = hmax2nd
                    # else :
                    #     r.append([x,hmax2nd])
                r.append([x,hmax])
                if debugFlag : print("          ",r,end="")
                if debugFlag : print()
        if timeFlag : print(" res(%d):"%len(res), time.time() - start , "-> ", end="")
        
        start = time.time()
        flag = True
        while flag:
            hmax = 0
            flag = False
            if len(r) > 1 :
                i = 0        
                while i < len(r):
                    x = r[i][0]
                    h = r[i][1]
                    if i == len(r)-1 : 
                        x1 = -1
                    else : 
                        x1 = r[i+1][0]
                    if i == len(r)-1 : 
                        h1 = -1
                    else :
                        h1 = r[i+1][1]
                        
                    if h == h1:
                        r.pop(i+1)
                        flag = True
                    else :
                        if x == x1:
                            hmax = max(h,h1,hmax)
                            if h != hmax:
                                r.pop(i)
                                flag = True
                        else : # x != x1:
                            hmax = 0
                    i += 1
                if debugFlag : print("r",r)
        if timeFlag : print(" pop(%d):"%len(res), time.time() - start , "-> ", end="")

        return r
    def minIndexLessThanX(self,sortList,xx):
        # enumerate() -> (index,[x1,x2,height])
        # return min(enumerate(sortList), key=lambda x: abs(x[1][1]-xx) if x[1][1] < xx else math.inf)
        
        # elapsed time : res(10000): 6.227318525314331
        for i in range(len(sortList)):
            if sortList[i][1] > xx :
                return i
        
        # elapsed time : res(10000): 7.8440186977386475 
        # i = self.startIdx
        # while i < len(sortList):
        #     if sortList[i][1] > xx :
        #         self.startIdx = i 
        #         return i
        #     else :
        #         i += 1
        
        return len(sortList)-1
        
            
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.getSkyline(s)
    print(" len :", len(s) , end="") 
    print(" , total_time :", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , ":" , end="")  
    if len(s) < 30: print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='getSkyline.py',
        description=
        'getSkyline'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('getSkyline problem :')

    s = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8],[22,24,8],[24,26,8],[26,28,6]]
    run(s,[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [26, 6], [28, 0]])
    s = [[2,5,3],[0,2,3]]
    run(s,[[0,3],[5,0]])
    s = [[1,2,1],[1,2,2],[1,2,3]]
    run(s,[[1,3],[2,0]])
    s = [[1,5,3], [1,5,3], [1,5,3]]
    run(s,[[1,3],[5,0]])
    s = [[1, 10001, 10000], [2, 10001, 9999], [3, 10001, 9998], [4, 10001, 9997], [5, 10001, 9996]]
    run(s,[[1, 10000], [10001, 0]])
    s = []
    p = 3000
    for i in range(1,p+1):
        s.append([i,p+1,p-i+1])
    run(s,[[1, p], [p+1, 0]])
    
    