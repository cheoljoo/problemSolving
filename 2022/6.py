from collections import defaultdict

import sys
import argparse
import re


if (__name__ == "__main__"):
    dbg = 0
    parser = argparse.ArgumentParser(
        prog='PermuMatch.py',
        description=
        'GCD and Permutatin Match'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    dbg = args.debug
    if not dbg:
        dbg = 0
    
    s= input()
    pattern = '(\d+|\+|\-)'
    result = re.findall(pattern,s)
    #print(result)
    
    flag=0
    sum =0
    for i in result:
        if i == '+':
            if dbg :
                print('++')
        elif i == '-':
            if dbg :
                print('--')
            flag = 1
        else :
            if dbg :
                print(i)
            if flag == 0:
                sum += int(i)
            else:
                sum -= int(i)
    
    print(sum)
