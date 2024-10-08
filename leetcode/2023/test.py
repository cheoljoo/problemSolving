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

# House Robber : rob



a = [2,4,6]
b = [1,3,5,-1,-1,-1]

a = iter(a)
output = [next(a,0) if x == -1 else x for x in b]
print(output)
sorted_output = sorted([next(a,0) if x == -1 else x for x in b])
print(sorted_output)
# [1, 2, 3, 4, 5, 6]  : 왜 나는 [0, 0, 0, 1, 3, 5]  이런 값이 나올까?


import os
import contextlib

# os.remove('somefile.tmp') 

with contextlib.suppress(FileNotFoundError):
    print(1)
    os.remove('somefile.tmp')
    print(2)

# This is equivalent to:

try:
    print(3)
    os.remove('somefile.tmp')
    print(4)
except FileNotFoundError:
    print(5)
    pass   

import re
patternDate = '\d+\/\d+\/\d+'
patternTime = '\d+:\d+:\d+\.\d+'
if re.match(patternDate, '2022/10/01') :
    print("True1")
if re.match(patternTime, "10:10:03.210") :
    print("True2")