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
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        eachArt = []
        digDict = {}
        for (a,b) in dig:
            digDict[(a,b)] = 1
        for ai in range(len(artifacts)):
            eachArtDict = []
            (rs , cs,re,ce) = artifacts[ai]
            # print(rs , cs,re,ce)
            for ri in range(rs,re+1):
                for ci in range(cs,ce+1): 

                    eachArtDict.append([ri,ci])
            eachArt.append(eachArtDict)
        # print("artifacts:",artifacts)
        # print("eachArt:",eachArt)
        count = 0
        for eai in range(len(eachArt)):
            notInFlag = 0
            # print(eai,eachArt[eai])
            for p in eachArt[eai]:
                # print(p,dig)
                (a,b) = p
                if not((a,b) in digDict):
                    notInFlag = 1
                    break
            if notInFlag == 0:
                count += 1
        return count
            


def run(n,s,k,expect):
    ismatch = Solution()
    r = ismatch.digArtifacts(n,s,k)
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


    #run(2,[[0,0,0,0],[0,1,1,1]],[[0,0],[0,1],[1,1]],2)
    run(5,[[3,1,4,1],[1,1,2,2],[1,0,2,0],[4,3,4,4],[0,3,1,4],[2,3,3,4]],[[0,0],[2,1],[2,0],[2,3],[4,3],[2,4],[4,1],[0,2],[4,0],[3,1],[1,2],[1,3],[3,2]],1)



# 5203. Count Artifacts That Can Be Extracted
# User Accepted:916
# User Tried:1095
# Total Accepted:916
# Total Submissions:1221
# Difficulty:Medium
# There is an n x n 0-indexed grid with some artifacts buried in it. You are given the integer n and a 0-indexed 2D integer array artifacts describing the positions of the rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith artifact is buried in the subgrid where:

# (r1i, c1i) is the coordinate of the top-left cell of the ith artifact and
# (r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
# You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

# Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will excavate the cell (ri, ci), return the number of artifacts that you can extract.

# The test cases are generated such that:

# No two artifacts overlap.
# Each artifact only covers at most 4 cells.
# The entries of dig are unique.
 

# Example 1:


# Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
# Output: 1
# Explanation: 
# The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid.
# There is 1 artifact that can be extracted, namely the red artifact.
# The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it.
# Thus, we return 1.
# Example 2:


# Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
# Output: 2
# Explanation: Both the red and blue artifacts have all parts uncovered (labeled with a 'D') and can be extracted, so we return 2. 