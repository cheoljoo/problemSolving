from collections import defaultdict
import numpy as np

import sys
import argparse

B0 = 0
B1 = 1
MatchNumber = 998244353


class PermuMatch :
    """
    GCD and Permutatin Match

    url : https://codeup.kr/problem.php?id=2127
    a , b, n ,m 
    Bn = a*Bn-1 + b*Bn-2
    gcd(Bn,Bm)
    Match Number : 998244353

    Attributes
    ----------
    n : int n>2     < 10^18
    m : int m>2     < 10^18
    a : int coprime  < 10^18
    b : int coprime  < 10^18
    debug : int debug mode

    Methods
    -------
    __init__()
        input
    getB()
        compute Bn , Bm
    gcd()
        compute GCD
    """
    
    def __init__(self, debug=0):
        """
        input
        """
        np.seterr(all='ignore')  # RuntimeWarning: overflow encountered in long_scalars
        self.debug = debug
        self.a , self.b , self.n , self.m = map(int, input().split())
        if self.n > self.m :
            self.big = self.n
        else :
            self.big = self.m
        self.B = np.empty(self.big+1, dtype=int)
        self.B[0]=0
        self.B[1]=1
        if self.debug :
            print("a b n m : ",self.a , self.b , self.n , self.m)
        super().__init__()

    def getB(self):
        """
        Bn = a*Bn-1 + b*Bn-2
        """
        for i in range(2,self.big+1):
            self.B[i] = self.a*self.B[i-1] + self.b*self.B[i-2]
            self.B[i] %= MatchNumber
        if self.debug :
            print("Bn Bm: ",self.B[self.n] , self.B[self.m])

    def gcd(self):
        """
        GCD
        
        GCD : 유클리드 호제법 
        """
        Bn = self.B[self.n]
        Bm = self.B[self.m]
        
        return np.gcd(Bn,Bm)


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
    
    n = int( input() )
    
    ret = []
    for i in range(n):
        per = PermuMatch(dbg)
        per.getB()
        ret.append(per.gcd())
    
    for r in ret:
        print(r)


