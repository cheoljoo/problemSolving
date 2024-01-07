from collections import defaultdict
from collections import Counter
import collections
import enum
from re import A
#import numpy as np

import sys
import argparse
import math
import random
from tkinter import N
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import time
import heapq

# minimumDeleteSum.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math


# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in xrange(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) - 1, -1, -1):
            for j in xrange(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]

    #   |     |     |   0 |   1 |   2 |   3 |   4 |   5 |   6 |
    #   |-----|-----|-----|-----|-----|-----|-----|-----|-----|
    #   |     | chʳ |     |  d  |  e  |  l  |  e  |  t  |  e  |
    #   |  0  |     |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
    #   |  1  |  l  |  0  |  0  |  0  |  1  |  1  |  1  |  1  |
    #                                  l     l     l     l
    #   |  2  |  e  |  0  |  0  |  1  |  1  |  2  |  2  |  2  |
    #                             e    l,e    le    le    le
    #   |  3  |  e  |  0  |  0  |  1  |  1  |  2  |  2  |  3  |
    #                             e    l,e  le,ee le,ee  lee
    #   |  4  |  t  |  0  |  0  |  1  |  1  |  2  |  3  |  3  |
    #                             e    l,e  le,ee let,eet lee,let,eet
    
          
def run(s,s1,expect):
    start = time.time()
    print(len(s),len(s1))
    A = Solution()
    r = A.minimumDeleteSum(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minimumDeleteSum.py',
        description=
        'minimumDeleteSum'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minimumDeleteSum problem :')

    run("delete","leet",403)
    run("igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa","ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi",100)