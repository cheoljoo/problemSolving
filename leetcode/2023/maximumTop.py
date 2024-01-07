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

import sys
import argparse
import math
import random

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0 :
            return nums[0]
        if len(nums) == 1:
            if k %2 == 1:
                return -1
            else :
                return nums[0]
        if k == 1 :
            return nums[1]
        if k <len(nums) :
            return max(max(nums[0:k-1]),nums[k])
        if k == len(nums):
            return max(nums[:-1])
        if k > len(nums) :
            return max(nums)
        return -1

            
    


def run(s,k,expect):
    ismatch = Solution()
    r = ismatch.maximumTop(s,k)
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


    run([99,95,68,24,18],69,99)

# 5227. Maximize the Topmost Element After K Moves
# User Accepted:2299
# User Tried:4956
# Total Accepted:2328
# Total Submissions:16888
# Difficulty:Medium
# You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

# In one move, you can perform either of the following:

# If the pile is not empty, remove the topmost element of the pile.
# If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
# You are also given an integer k, which denotes the total number of moves to be made.

# Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.

 

# Example 1:

# Input: nums = [5,2,2,4,0,6], k = 4
# Output: 5
# Explanation:
# One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
# - Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
# - Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
# - Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
# - Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
# Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
# Example 2:

# Input: nums = [2], k = 1
# Output: -1
# Explanation: 
# In the first move, our only option is to pop the topmost element of the pile.
# Since it is not possible to obtain a non-empty pile after one move, we return -1.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i], k <= 109