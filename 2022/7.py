from collections import defaultdict

import sys
import argparse
import re
import math

def isPrimeNumber(num):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if (num % i) == 0:
                if dbg :
                    print("isPrimeNumber:",num,i,False)
                return False
        
        if dbg :
            print("isPrimeNumber:",num,True)
        return True
    else:
        return False

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
    upsideFlag = 0
    for idx in range(len(s)):
        if s[idx] == '3':
            upsideFlag = 1
        elif s[idx] == '4':
            upsideFlag = 1
        elif s[idx] == '7':
            upsideFlag = 1    
        if dbg :
            print('s:',s[idx])
    # print("s:" , s)
    # print("upsideNum:" , upsideNum)
    
    upsideNum = 0   
    for idx in reversed(range(len(s))): 
        if s[idx] == '6':
            upsideNum = upsideNum*10 + 9
        elif s[idx] == '9':
            upsideNum = upsideNum*10 + 6
        else :
            upsideNum = upsideNum*10 + int(s[idx])
    
    if upsideFlag == 1 :
        print('no')
    else :
        if not isPrimeNumber(int(s)):
            print('no')
        elif not isPrimeNumber(upsideNum):
            print('no')
        else:
            print('yes')
            
            
