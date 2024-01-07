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
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        idx = 0
        isPositive = True
        r = []
        for i in range(numRows):
            r.append("")
        for i in range(len(s)):
            if i == 0:
                r[idx] += s[i]
                idx += 1
            else :
                r[idx] += s[i]
                if idx == numRows-1 :
                    idx -= 1
                    isPositive = False
                elif idx == 0 :
                    idx += 1
                    isPositive = True
                else :
                    if isPositive :
                        idx += 1
                    else :
                        idx -= 1
        return "".join(r)
    
def run(s,n,expect):
    A = Solution()
    r = A.convert(s,n)

    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s , n)   

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='zigzagConversion.py',
        description=
        'zigzagConversion'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('zigzagConversion problem:')

    s = "PAYPALISHIRING"
    numRows = 3
    run(s,numRows,"PAHNAPLSIIGYIR")
    s = "PAYPALISHIRING"
    numRows = 4
    run(s,numRows,"PINALSIGYAHRPI")
    s = "A"
    numRows = 1
    run(s,numRows,"A")
    

