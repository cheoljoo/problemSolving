from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # we should add empty lists to the
        # if len(nums) == 0 : return 0
        p = nums[0]
        index = 1
        count = 1
        for _ in range(1,len(nums)) :
            if p == nums[index] :
                del nums[index]
                continue
            else :
                p = nums[index]
                count += 1
                index += 1
        
        return count

def run(s,expect):
    a = Solution()
    r = a.removeDuplicates(s)
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

    s = [1,1,2]
    run(s,2)
    s = [0,0,1,1,1,2,2,3,3,4]
    run(s,5)