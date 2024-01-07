from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

# O(N)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        index = 0
        while index < len(nums):
            v = nums[index]
            if index+1 == v or v == 0 :
                index += 1
                continue
            else :
                if nums[v-1] == v :
                    nums[index] = 0
                    index += 1
                    continue
                nums[index] , nums[v-1] = nums[v-1] , nums[index]
        r = []
        for (i,v) in enumerate(nums):
            if v == 0:
                r.append(i+1)
        return r

def run(s,expect):
    a = Solution()
    r = a.findDisappearedNumbers(s)
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

    s = [4,3,2,7,8,2,3,1]
    run(s,[5,6])
    s = [1,1]
    run(s,[2])