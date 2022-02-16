from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

class Solution:
    def __init__(self):
        self.memo = {}
    def strangePrinter(self, s: str) -> int:
        s = "".join(ch for i, ch in enumerate(s) if i == 0 or s[i-1] != ch)
        
        return self.dp(0, len(s)-1, s)
    
    def dp(self, start, end, s):
        # print count for [start, end], end exclusive
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        if start == end:
            return 1
        # 1st and others
        # from 2nd , remove it ( before + after  count) if it is same with start
        ans = 1 + self.dp(start + 1, end, s) 
        
        for i in range(start + 1, end+1):
            # skip the element when it's same as the start
            if s[start] == s[i]:
                if i == end:
                    ans = min(ans,self.dp(start, i-1, s))
                else :
                    ans = min(ans, self.dp(start, i-1, s) + self.dp(i + 1, end, s))
        self.memo[(start, end)] = ans
        return ans

def run(s,expect):
    ismatch = Solution()
    r = ismatch.strangePrinter(s)
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

    s = "aaabbbaaa"
    run(s,2)
    # s = "aba"
    # run(s,2)