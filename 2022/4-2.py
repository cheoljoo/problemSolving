#from collections import defaultdict
import numpy as np

import sys
import argparse

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
        # self.board = [0 for i in range(BOARD_X*BOARD_Y)]
        # self.B = np.empty(self.big+1, dtype=int)
        #self.B = [0 for i in range(self.big+1)]
        #self.B[0]=0
        #self.B[1]=1
        if self.debug :
            print("a b n m : ",self.a , self.b , self.n , self.m)
        super().__init__()

    def getB(self):
        """
        Bn = a*Bn-1 + b*Bn-2
        """
        prev1 = 1
        prev2 = 0
        for i in range(2,self.big+1):
            cur = self.a*prev1 + self.b*prev2
            if i == self.n :
                self.nValue = cur
            if i == self.m :
                self.mValue = cur
            prev2 = prev1
            prev1 = cur
            #self.B[i] %= MatchNumber
        if self.debug :
            print("Bn Bm: ",self.nValue , self.mValue)

    def gcd(self):
        """
        GCD
        
        GCD : 유클리드 호제법 
        """
        return np.gcd(self.nValue,self.mValue) % MatchNumber


if (__name__ == "__main__"):
    n = int( input() )
    
    ret = []
    for i in range(n):
        per = PermuMatch()
        per.getB()
        ret.append(per.gcd())
        del per
    
    for r in ret:
        print(r)

