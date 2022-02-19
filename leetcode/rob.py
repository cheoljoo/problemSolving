from collections import defaultdict
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

# House Robber : rob

class Solution:
    def __init__(self):
        self.mem = {}
        
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return max(self.dp(0),self.dp(1))
    
    def dp(self,start) -> int :
        if start >= len(self.nums):
            return 0
        if start in self.mem:
            return self.mem[start]
        r1 = self.nums[start] + self.dp(start+2)
        r2 = self.nums[start] + self.dp(start+3)
        self.mem[start] = max(r1,r2)
        return self.mem[start]

def run(s,expect):
    A = Solution()
    r = A.rob(s)

    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='rob.py',
        description=
        'rob'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('rob problem:')

    s = [1,2,3,1]
    run(s,4)
    s = [2,7,9,3,1]
    run(s,12)
    s = [1,70,9,3,100,3]
    run(s,170)

    

