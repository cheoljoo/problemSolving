
#import numpy as np

import sys
import argparse
import math
import random


from collections import defaultdict
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. 
# You must implement a solution with a linear runtime complexity and use only constant extra space.
class Solution:
    def __init__(self):
        self.dp = defaultdict(int)
    def singleNumber(self, nums: list[int]) -> int:
        for v in nums:
            if self.dp[v] == 0:
                self.dp[v] = 1
            elif self.dp[v] == 1 :
                self.dp[v] += 1
        for v in self.dp :
            if self.dp[v] == 1:
                return v
        return 0
            

def run(s,expect):
    a = Solution()
    r = a.singleNumber(s)
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

    s = [2,2,1]
    run(s,1)
    s = [4,1,2,1,2]
    run(s,4)
    s = [-1]
    run(s,-1)