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



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        totalSum = l * (l+1) // 2
        inputSum = 0
        for v in nums:
            inputSum += v
        return totalSum - inputSum
    
    
def run(x,expect):
    A = Solution()
    r = A.missingNumber(x)

    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , x )   

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='missingNumber.py',
        description=
        'missingNumber'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('missingNumber problem:')

    x = [3,0,1]
    run(x,2)
    x = [0,1]
    run(x,2)
    x = [9,6,4,2,3,5,7,0,1]
    run(x,8)
    

