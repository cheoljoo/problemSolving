from collections import defaultdict

import sys
import argparse



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
    
    l = int(input())
    r1,r2 = map(int , input().split() )
    b1,b2 = map(int , input().split() )
    y1,y2 = map(int , input().split() )
    
    h = (r1+r2)/2
    b1 = abs(h -b1)
    b2 = abs(h -b2)
    y1 = abs(h -y1)
    y2 = abs(h -y2)
    l = l/2 + abs(l/2 - h)
    if dbg:
        print(h,b1,b2,y1,y2,l)
    
    if b1 != b2 :
        h = (b1+b2)/2
        y1 = abs(h -y1)
        y2 = abs(h -y2)
        l = l/2 + abs(l/2 - h)
        if dbg:
            print(h,y1,y2,l)   
            
    if y1 != y2 :
        h = (y1+y2)/2
        l = l/2 + abs(l/2 - h)
        if dbg:
            print(h,l)
                
    print(l)