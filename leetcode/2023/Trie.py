from collections import defaultdict
from collections import Counter
from collections import deque
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
from bisect import bisect_left , bisect_right

timeFlag = 0
debugFlag = 0
import math

    
class Trie:
    
    def __init__(self):
        self.mem = {}

    def insert(self, word: str) -> None:
        self.mem[word] = 0

    def search(self, word: str) -> bool:
        if word in self.mem:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for s in self.mem.keys():
            if s.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)