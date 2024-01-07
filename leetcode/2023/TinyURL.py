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

# TinyURL.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Codec:
    def __init__(self):
        self.count = 1
        self.url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = longUrl.split('/')
        print(url)
        p = "http://tinyurl.com/" + str(self.count)
        self.url[p] = longUrl
        self.count += 1
        return p

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Codec()
    # r = A.TinyURL(s)
    tiny = A.encode(s); # returns the encoded tiny url.
    r = A.decode(tiny); # returns the original url after deconding it.
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='TinyURL.py',
        description=
        'TinyURL'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('TinyURL problem :')

    run("https://leetcode.com/problems/design-tinyurl","https://leetcode.com/problems/design-tinyurl")