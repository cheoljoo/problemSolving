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

class Solution:
    def printTable(self,t,ts):
        for i in range(len(t)):
            print(t[i])
            print(ts[i])
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
        # find the longest matched subsequence between word1 and word2
        # example "park" "spake"  common subsequence is "pak". so answer is 3
        l1,l2 = 0 ,0
        table = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]  # col : word1 , row : word2
        tableSet = [[set() for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]  # col : word1 , row : word2
        # tableSet[1][1].add("3")
        # print(tableSet)
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                    if len(tableSet[i-1][j-1]) == 0:
                        tableSet[i][j].add(word2[i-1])
                    else :
                        for p in tableSet[i-1][j-1]:
                            print(i,j,table[i][j],p)
                            tableSet[i][j].add(p + word2[i-1])
                else :
                    table[i][j] = max(table[i-1][j],table[i][j-1])
                    if table[i-1][j] == table[i][j-1]:
                        for p in tableSet[i-1][j]:
                            tableSet[i][j].add(p)
                        for p in tableSet[i][j-1]:
                            tableSet[i][j].add(p)
                    elif table[i-1][j] < table[i][j-1]:
                        tableSet[i][j] = tableSet[i][j-1]
                    else:
                        tableSet[i][j] = tableSet[i-1][j]
        self.printTable(table,tableSet)
        word1Sum = 0
        word2Sum = 0
        maxMatchedSum = 0
        for v in word1:
            word1Sum += ord(v)
        for v in word2:
            word2Sum += ord(v)
        for m in tableSet[len(word2)][len(word1)]:
            mMS = 0
            for v in m:
                mMS += ord(v)
            maxMatchedSum = max(maxMatchedSum,mMS)
        return word1Sum + word2Sum - 2* maxMatchedSum
        # return len(word1) + len(word2) - table[len(word2)][len(word1)]*2

    #   |     |     |   0 |   1 |   2 |   3 |   4 |   5 |   6 |
    #   |-----|-----|-----|-----|-----|-----|-----|-----|-----|
    #   |     | chʳ |     |  d  |  e  |  l  |  e  |  t  |  e  |
    #   |  0  |     |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
    #   |  1  |  l  |  0  |  0  |  0  |  1  |  1  |  1  |  1  |
    #                                   l     l     l     l
    #   |  2  |  e  |  0  |  0  |  1  |  1  |  2  |  2  |  2  |
    #                             e    l,e    le    le    le
    #   |  3  |  e  |  0  |  0  |  1  |  1  |  2  |  2  |  3  |
    #                             e    l,e  le,ee le,ee  lee
    #   |  4  |  t  |  0  |  0  |  1  |  1  |  2  |  3  |  3  |
    #                             e    l,e  le,ee let,eet lee,let,eet
    
          
def run(s,s1,expect):
    start = time.time()
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
    run("igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa",
"ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi",100)