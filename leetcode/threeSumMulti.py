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

# threeSumMulti.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        self.count = 0
        self.arrCountDict = {}
        arrList = []
        self.arrSet = set()
        self.mem = set()
        for v in arr:
            if v in self.arrCountDict :
                self.arrCountDict[v] += 1
            else :
                self.arrCountDict[v] = 1
                arrList.append(v)
                self.arrSet.add(v)
        arrList.sort()
        i = 0
        while True:
            if i >= len(arrList) or arrList[i] > target//3+1:
                break
            for j in range(i,len(arrList)):
                self.go(arrList , i , j, target)
                # self.go(arrList , i , j+1, target)
            i += 1
        return self.count % (10**9+7)

    def go(self,arrList,i,j,target):  # i is index of first argument , j is index of second argument
        if (i,j) in self.mem:
            return
        if j >= len(arrList):
            return 
        third = target - arrList[i] - arrList[j]
        if third not in self.arrSet:
            return
        vi = arrList[i]
        vj = arrList[j]
        if i == j :
            if third == vj :  # three element have the same number
                if self.arrCountDict[third] >= 3 :
                    self.count += self.arrCountDict[third]*(self.arrCountDict[third]-1)*(self.arrCountDict[third]-2) // 6   # nC3
                    self.mem.add((i,j))
                    return
                else :
                    return
            elif third > vj :
                if self.arrCountDict[vi] >= 2 :
                    n = self.arrCountDict[vi]*(self.arrCountDict[vi]-1) // 2   # nC2
                    n *=  self.arrCountDict[third]
                    self.count += n
                    self.mem.add((i,j))
                else :
                    return
            else :
                return
        else :
            if third == vj :  # three element have the same number
                if self.arrCountDict[third] >= 2 :
                    n = self.arrCountDict[third]*(self.arrCountDict[third]-1) // 2   # nC2
                    n *=  self.arrCountDict[vi]
                    self.count += n
                    self.mem.add((i,j))
                    return
                else :
                    return
            elif third > vj :
                self.count += self.arrCountDict[third]*self.arrCountDict[vi]*self.arrCountDict[vj]
                self.mem.add((i,j))
            else :
                return
            




           
def run(s,s1,expect):
    start = time.time()
    A = Solution()
    r = A.threeSumMulti(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s ,s1, end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='threeSumMulti.py',
        description=
        'threeSumMulti'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('threeSumMulti problem :')


    run([2,1,3,2,3,1],6,8)
    run([2,1,3,2,1],6,4)
    run([3,3,3,3,3],9,10)
    run([2,1,3],6,1)
    run([0,2,0],2,1)
    run([1,1,2,2,3,3,4,4,5,5],8,20)
    run([1,1,2,2,2,2],5,12)