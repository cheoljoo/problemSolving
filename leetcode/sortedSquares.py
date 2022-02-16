from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

# O(N)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i = 0
        for v in nums:
            if v >= 0:
                break
            i += 1
        
        lefti = i -1
        righti = i
        r = []
        for _ in range(len(nums)):
            if lefti < 0 :
                r.append(int(nums[righti]**2))
                righti += 1
            elif righti >= len(nums):
                r.append(int(nums[lefti]**2)) 
                lefti -= 1
            elif abs(nums[lefti]) > abs(nums[righti]):
                r.append(int(nums[righti]**2))
                righti += 1
            else :
                r.append(int(nums[lefti]**2)) 
                lefti -= 1
        return r

def run(s,expect):
    a = Solution()
    r = a.sortedSquares(s)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='set_ax_b.py',
        description=
        'this set hates a b'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    s = [-4,-1,0,3,10]
    run(s,[0,1,9,16,100])
    s = [-7,-3,2,3,11]
    run(s,[4,9,9,49,121])