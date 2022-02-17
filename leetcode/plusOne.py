from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # s = "".join(ch for i, ch in enumerate(s) if i == 0 or s[i-1] != ch)
        s = "".join(str(ch) for ch in digits)
        i = int(s)
        # print(i)
        i += 1
        # print(i)
        s2 = list(str(i))
        r = []
        for it in s2:
            r.append(int(it))
        # print(r)
        return r
    


def run(s,expect):
    ismatch = Solution()
    r = ismatch.plusOne(s)
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

    s = [1,2,3]
    run(s,[1,2,4])
    s = [4,3,2,1]
    run(s,[4,3,2,2])
    s = [9]
    run(s,[1,0])