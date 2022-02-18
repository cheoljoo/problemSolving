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

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Last executed input:
# 2126753390
# 1702766719

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while True:
            mid = (start+end)//2
            if isBadVersion(mid) == False :
                start = mid+1
            else :
                if start == end:
                    return start
                end = mid
            
        # for i in range(n):
        #     if isBadVersion(i+1):
        #         return i+1
        return n

def isBadVersion(n):
    if n >= 1702766719:
        return True
    else :
        return False

def run(s,expect):
    A = Solution()
    r = A.firstBadVersion(s)

    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='firstBadVersion.py',
        description=
        'firstBadVersion'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0


    run(2126753390,1702766719)

