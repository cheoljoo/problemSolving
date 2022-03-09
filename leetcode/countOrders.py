from collections import defaultdict
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

# countOrders.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def countOrders(self, n: int) -> int:
        # 2n Pn , Dn
        # start P1 =>  P1, (2n-1) * P(n-1)
        # ...
        # start Pn , (2n-1)*P(n-1)
        # P(n) = n*(2n-1)*P(n-1)
        
        # P(1) = 1
        # P(2) = 2*3*P(1) = 6
        # P(3) = 3*5*P(2) = 90
        
        p = {}
        p[1] = 1
        for i in range(2,n+1):
            p[i] = (i * (2*i -1) * p[i-1]) % 1000000007
        
        return p[n] % 1000000007

            