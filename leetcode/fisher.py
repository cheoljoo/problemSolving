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

# fisher.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def fisher(self, info:List[List[int]],N: int) -> int:
        self.mx = -math.inf
        self.mn = math.inf
        self.mem = {}
        if N == 1:
            return info[0][1]
        for i in range(N):
            if self.mx < info[i][1]:
                self.mx = info[i][1]
            if self.mn > info[i][1]:
                self.mn = info[i][1]
        # print(self.mx,self.mn,info)
        while True:
            if self.mx - self.mn <= 2:
                print(" <= 2:",self.mn,self.mx)
                ans = 0
                for i in reversed(range(self.mn , self.mx+1)):
                    if i in self.mem:
                        t = self.mem[i]
                    else:
                        t = self.go(i,info,N)
                    if t == 0:
                        return i
                    elif t > 0 :
                        ans = max(ans,i)
                return ans
            mid = (self.mx+self.mn)//2
            t = self.go(mid,info,N)
            if t == 0:
                return mid
            elif  t > 0 :
              self.mn = mid
            else :
                self.mx = mid  
            

    # def go(self,target,info,N) -> int:
    #     stack = []
    #     shortage = 0
    #     for i in range(N):
    #         node , h = info[i][0],info[i][1]
    #         s = h - target
    #         if not stack:
    #             stack.append((node,s))
    #             continue
    #         # s<0 이면 
    #         if s < 0:
    #             if stack[-1][1] == 1 or stack[-1][1] == 0:
    #                 stack.pop()
    #             if stack and stack[-1][1] <0:   
    #                 stack.append((node,s))
    #                 continue
    #             while stack and stack[-1][1] > 1:
    #                 diff = abs(node - stack[-1][0])
    #                 need = diff -s
    #                 if stack[-1][1] <= diff:
    #                     stack.pop()
    #                     stack.append((node,s))
    #                     continue
    #                 elif stack[-1][1] >= need:
    #                     stack[-1] = (stack[-1][0],stack[-1][1] - need)
    #                     if stack[-1][1] == 0 :
    #                         stack.pop()
    #                     break
    #                 else : 
    #                     s += stack[-1][1] - diff
    #                     stack.pop()
    #                     stack.append((node,s))
    #                     break
    #         elif s > 0:
    #             while stack and stack[-1][1] < 0:
    #                 diff = abs(node - stack[-1][0])
    #                 if s <= diff:
    #                     break
    #                 s -= diff
    #                 if s + stack[-1][1] > 0 :
    #                     s += stack[-1][1]
    #                     stack.pop()
    #                     continue
    #                 else:
    #                     stack[-1] = (stack[-1][0],stack[-1][1] + s)
    #                     if stack[-1][1] == 0 :
    #                         stack.pop()
    #                     s = 0
    #                     break
    #             if s > 0:
    #                 stack.append((node,s))
    #     if not stack:
    #         self.mem[target] = 0
    #         return 0
    #     elif stack[0][1] > 0:
    #         self.mem[target] = 1
    #         return 1
    #     else :
    #         self.mem[target] = -1
    #         return -1

    def go(self,target,info,N) -> int:
        spare = info[0][1] - target
        for i in range(1,N):
            node , h = info[i][0],info[i][1]
            tax = info[i][0] - info[i-1][0]  # positive
            if spare >= 0 : 
                if spare - tax < 0 : 
                    move = 0 
                else:
                    move = spare - tax
            else: # spare < 0:
                move = spare - tax
            spare = h - target + move

        if spare > 0:
            return 1
        elif spare < 0 :
            return -1
        else :
            return 0

           
def run(s,s1,expect):
    print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.fisher(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='fisher.py',
        description=
        'fisher'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('fisher problem :')

    run([[3,20]],1,20)
    run([[10,10],[20,0],[30,20]],3,5)
    run([[1,21],[2,0],[4,0]],3,6)
    run([[1,0],[2,0],[4,21]],3,6)
    run([[1,0],[2,21],[4,0]],3,6)
    run([[5,7],[15,100],[1200,20],[1201,41]],4,30)
    run([[5,7],[15,100],[1200,20]],3,20)
    run([[20,300],[40,400],[340,700],[360,600]],4,415)