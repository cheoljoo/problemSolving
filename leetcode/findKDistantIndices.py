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
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indexKeys = []
        r = []
        for i in range(len(nums)) :
            if nums[i] == key:
                indexKeys.append(i)
        print(indexKeys)
        for i in range(len(nums)):
            findFlag = False
            for kv in indexKeys:
                print(kv , i , abs(kv-i))
                if abs(kv - i) <= k :
                    findFlag == True
                    r.append(i)
                    break
        return r
    


def run(s,key,k,expect):
    ismatch = Solution()
    r = ismatch.findKDistantIndices(s,key,k)
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


    run([3,4,9,1,3,9,5],9,1,[1,2,3,4,5,6])

# 6031. Find All K-Distant Indices in an Array
# User Accepted:8907
# User Tried:9481
# Total Accepted:9049
# Total Submissions:13924
# Difficulty:Easy
# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

# Return a list of all k-distant indices sorted in increasing order.

 

# Example 1:

# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 
# Example 2:

# Input: nums = [2,2,2,2,2], key = 2, k = 2
# Output: [0,1,2,3,4]
# Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index. 
# Hence, we return [0,1,2,3,4].
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# key is an integer from the array nums.
# 1 <= k <= nums.length