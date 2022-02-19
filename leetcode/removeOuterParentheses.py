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
    def removeOuterParentheses(self, s: str) -> str:
        lvl = 0
        r = ""
        for ch in s:
            if ch == '(' :
                if lvl == 0:
                    lvl += 1
                    continue
                else :
                    lvl += 1
            else : # ')'
                if lvl == 1 :
                    lvl -= 1
                    continue
                else :
                    lvl -= 1
            r += ch
        return r
    
def run(s,expect):
    A = Solution()
    r = A.removeOuterParentheses(s)

    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='removeOuterParentheses.py',
        description=
        'removeOuterParentheses'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('removeOuterParentheses problem:')

    s = "(()())(())"
    run(s,"()()()")
    s = "(()())(())(()(()))"
    run(s,"()()()()(())")
    s = "()()"
    run(s,"")
    

