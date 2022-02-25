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

timeFlag = 0
debugFlag = 0
class Solution:
    def __init__(self):
        # self.startIdx = 0
        self.startSortIndexUp = 0
        self.startSortIndexDown = 0
        self.prevDirection = 1  # 1:up
        self.prevMaxUp = 0
        self.prevQueueDown = []
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
        # my algorithm is that down lines are sorted of res[]
        # we want to choose second max number at down lines. 
        res.sort(key=lambda x: x[0]*(2**64)+((x[1]+1)//2)*(2**32)+x[2])
        if timeFlag : print(" res.sort(%d):"%len(res), time.time() - start , "-> ", end="")
        
        start = time.time()
        r = []
        for (x,isUp,h) in res:
            # if x == 95 :
            #     pass
            # if x == 97 : 
            #     pass
            # if x == 99 : 
            #     pass
            if isUp == 1:  # up
                if self.prevDirection == isUp :
                    if self.prevMaxUp < h :
                        self.prevMaxUp = h
                        r.append([x,h])
                    continue
 
                self.prevDirection = isUp
                # l1 : [x1,x2,height]
                # enumerate() -> (index,[x1,x2,height])
                # minIdx = self.minIndexLessThanX(endSort,x)
                if debugFlag : print("UP x :",x,"idx :",end="")
                hmax = 0
                count = 0
                p1count = 0
                p2count = 0
                for i in range(self.startSortIndexUp,len(startSort)):
                    if startSort[i][1] < x :
                        self.startSortIndexUp = i
                        p1count += 1
                    else :
                        break         
                for i in range(self.startSortIndexUp,len(startSort)):
                    if startSort[i][0] > x :
                        break
                    p2count += 1
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
                    self.prevMaxUp = hmax
                    if debugFlag : print("          ",r,end="")
                if debugFlag : print()
        # if timeFlag : print(" up(%d):"%len(res), time.time() - start , "-> ", end="")
        # start = time.time()        
        # for (x,isUp,h) in res:
            # else :   # isUp == 0: down
            if isUp != 1:  # down
                if self.prevDirection == isUp :
                    if self.prevQueueDown[-1] == h :
                        self.prevQueueDown.remove(h)
                        r.append([x,self.prevQueueDown[-1]])
                        self.prevMaxUp = self.prevQueueDown[-1]
                    elif self.prevQueueDown[-1] > h :
                        if h in self.prevQueueDown : self.prevQueueDown.remove(h)
                    # else :
                    #     print("*TT*ERROR",end="")
                    continue
                else :
                    self.prevQueueDown.clear()
                    self.prevQueueDown.append(0)
                self.prevDirection = isUp
                self.prevMaxUp = 0
                # l1 : [x1,x2,height]
                # enumerate() -> (index,[x1,x2,height])
                # minIdx = self.minIndexLessThanX(endSort,x)
                if debugFlag : print("dn x :",x,"idx :",end="")
                hmax = 0
                hmax2nd = 0
                count = 0
                p1count = 0
                p2count = 0
                for i in range(self.startSortIndexDown,len(startSort)):
                    if startSort[i][1] < x :
                        self.startSortIndexDown = i
                        p1count += 1
                    else :
                        break       
                for i in range(self.startSortIndexDown,len(startSort)):
                    if startSort[i][0] > x :
                        break
                    p2count += 1
                    if startSort[i][0] < x and x < startSort[i][1]: 
                        if hmax < startSort[i][2]:
                            hmax2nd = hmax 
                            hmax = startSort[i][2]
                            count = 1
                        elif hmax == startSort[i][2]:
                            count += 1
                        else :
                            if hmax2nd < startSort[i][2]:
                                hmax2nd = startSort[i][2]
                        self.prevQueueDown.append(startSort[i][2])
                        if debugFlag :print(" ->%d(%d..%d)H%d"%(i,startSort[i][0],startSort[i][1],startSort[i][2]), end="")
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
                r.append([x,hmax])   # max among the rests of itself
                self.prevMaxUp = hmax
                # self.prevQueueDown.remove(hmax)
                self.prevQueueDown.sort()
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

    s = [[1,38,219],[2,19,228],[2,64,106],[3,80,65],[3,84,8],[4,12,8],[4,25,14],[4,46,225],[4,67,187],[5,36,118],[5,48,211],[5,55,97],[6,42,92],[6,56,188],[7,37,42],[7,49,78],[7,84,163],[8,44,212],[9,42,125],[9,85,200],[9,100,74],[10,13,58],[11,30,179],[12,32,215],[12,33,161],[12,61,198],[13,38,48],[13,65,222],[14,22,1],[15,70,222],[16,19,196],[16,24,142],[16,25,176],[16,57,114],[18,45,1],[19,79,149],[20,33,53],[21,29,41],[23,77,43],[24,41,75],[24,94,20],[27,63,2],[31,69,58],[31,88,123],[31,88,146],[33,61,27],[35,62,190],[35,81,116],[37,97,81],[38,78,99],[39,51,125],[39,98,144],[40,95,4],[45,89,229],[47,49,10],[47,99,152],[48,67,69],[48,72,1],[49,73,204],[49,77,117],[50,61,174],[50,76,147],[52,64,4],[52,89,84],[54,70,201],[57,76,47],[58,61,215],[58,98,57],[61,95,190],[66,71,34],[66,99,53],[67,74,9],[68,97,175],[70,88,131],[74,77,155],[74,99,145],[76,88,26],[82,87,40],[83,84,132],[88,99,99]]
    run(s,[[1,219],[2,228],[19,225],[45,229],[89,190],[95,175],[97,152],[99,74],[100,0]])
    s = [[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]]
    run(s,[[1,3],[3,0]])
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
    p = 10000
    for i in range(1,p+1):
        s.append([i,p+1,p-i+1])
    run(s,[[1, p], [p+1, 0]])
    s = []
    p = 10000
    for i in range(1,p+1):
        s.append([1,i+1,1+i])
    run(s,[[1, p+1], [p+1, 0]])
    
    