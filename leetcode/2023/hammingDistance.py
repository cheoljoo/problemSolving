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
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        
        # hamming weight ( number of 1 bits )
        if n < 0:
            n = abs(n)-1
        count = 0
        while n :
            n &= n - 1
            count += 1
        return count
    
def run(x,y,expect):
    A = Solution()
    r = A.hammingDistance(x,y)

    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , x , y)   

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='hammingDistance.py',
        description=
        'hammingDistance'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('hammingDistance problem:')

    x = 4
    y = 1
    run(x,y,2)
    x = 3
    y = 1
    run(x,y,1)
    

