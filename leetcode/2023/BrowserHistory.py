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

class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pos+1]
        self.history.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        p = self.pos - steps
        if p < 0:
            p = 0
        self.pos = p
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        p = self.pos + steps
        if p >= len(self.history):
            p = len(self.history) -1
        self.pos = p
        return self.history[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)