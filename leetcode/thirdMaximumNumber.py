from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = None
        second = None
        third = None
        
        for i in nums :
            if first == i or second == i or third == i :
                continue
            if first == None :
                first = i
            elif first < i :
                third = second
                second = first
                first = i
            elif second == None :
                second = i
            elif second < i:
                third = second
                second = i
            elif third == None :
                third = i
            elif third < i:
                third = i
        
        if third == None:
            return first
        else :
            return third

def run(s,expect):
    a = Solution()
    r = a.thirdMax(s)
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

    s = [2,2,3,1]
    run(s,1)
    # s = "aba"
    # run(s,2)