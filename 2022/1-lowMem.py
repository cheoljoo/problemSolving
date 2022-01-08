from collections import defaultdict
import numpy as np

import sys
import argparse

#from memory_profiler import profile

class CountAntiSet :
    """
    A class used to get the count of elements

    url : https://codeup.kr/problem.php?id=2128&rid=0
        n, a, b이 주어진다. (1<=n<=10100)
        (1<=a,b<=103)
        집합 A의 임의의 원소 x를 선택했을 때
        ax+b가 집합 A에 존재하지 않도록 A의 원소를 빼버리자!
        하지만 a, b는 배려심이 많기 때문에 A의 크기를 최대로 하려고 한다.

    ax+b = n : hate a and b in set
    10 2 2  :  2x + 2 <= 10 
    x=1 =>  4 remove  1 2 3 5 6 7 8 9 10 (count 9)
                      ^
    x=2 =>  6 remove  1 2 3 5 7 8 9 10  (count 8)
                        ^
    x=3 =>  8 remove  1 2 3 5 7 9 10 (count 7)
                          ^
    x=4 =>  4 is not a element of set (count 7)
    x=5 =>  2*5+2 > 10    the end (count 7)

    Attributes
    ----------
    n : int max n
    a : int
    b : int
    debug : int debug mode

    Methods
    -------
    get_count()
        get the count of elements to meet the rule.
    print_set()
        print the elements in debug mode
    """

    #@profile
    def __init__(self, n , a , b, debug=0):
        """
        get the count of elements to meet the rule. (2)

        :param n: max number
        :param a: ax+b
        :param b: ax+b
        :param debug: debug mode
        :return:
        """
        self.debug = debug
        self.n = n
        self.a = a
        self.b = b
        self.x = np.zeros(n+1,dtype=np.int8)

        super().__init__()

        if self.debug :
            print(sys._getframe().f_code.co_name ,":",self.n , self.a , self.b,self.debug)

    #@profile
    def get_count(self):
        """
        get the count of elements to meet the rule. (2)
        """

        count = self.n
        for i in range(1 , self.n+1):
            nxt = self.a*i+self.b
            if self.x[i] != 1 :
                if self.debug :
                    print("x:",i , ", x[i]:",self.x[i])
                if nxt > self.n :
                    break
                else :
                    self.x[nxt] = 1
                    if self.debug :
                        self.print_set()
                    count -= 1

        if self.debug :
            print("result : ",end="")
        print(count)

    def print_set(self):
        """
        print the elements in debug mode (2)
        """

        if self.debug :
            print("set elements : ",end="")
            for i in range(1 , self.n+1):
                if self.x[i] == 0 :
                    print(i,end=" ")
            print()

if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='set_ax_b.py',
        description=
        'this set hates a b'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    sn ,sa , sb = input().split()
    n = int(sn)
    a = int(sa)
    b = int(sb)

    count_obj = CountAntiSet(n,a,b,debug)
    count_obj.get_count()

