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
                    last = i

        if self.debug :
            print("result : ",end="")
        print(count,i,last)

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

    def analyzeNumber(self,inNum):
        """Analyze number
        
        함수 ()
          계속 나누어 떨어져서 딱 맞아떨어질때 몇 단계까지 가는지 조사
          몇단계까지가서 안 맞아떨어졌는지 조사
        """
        finalLevel=1
        perfect=0
        num = inNum
        if num < (self.a + self.b) :
            return finalLevel , False
        
        while num >= self.a + self.b:
            num -= self.b
            a = int(num/self.a)
            b = num % self.a
            if b != 0:
                return finalLevel , False
            else :
                if a < (self.a + self.b):
                    return finalLevel, True
                num = a
                finalLevel += 1
        
    def display(self,inNum):
        """[summary]
        함수2()
            딱맞아 떨어지면 odd 이면 안 찍음 , even이면 찍음
            딱맞아떨어지지 않으면 단계가 odd 이면 찍음.
        Args:
            inNum ([type]): [description]
        """
        level , perfect = self.analyzeNumber(inNum)
        if perfect == True :
            if level%2 == 0:
                return True
            else :
                return False
        else :
            if level%2 == 0:
                    return False
            else :
                return True           
    def displayCount(self):
        """[summary]
        """
        count = self.n
        for i in range(1 , self.n+1) :
            if self.display(i) == False:
                count -= 1
            else :
                last = i
            # if (self.a * i + self.b) > self.n :
            #     break
        print("count",count,i,last)
        
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

    # sn ,sa , sb = input().split()
    # n = int(sn)
    # a = int(sa)
    # b = int(sb)

    # 10293842 6 2 => 8823293
    n = 10293842
    a = 6
    b = 2
    debug = 0

    count_obj = CountAntiSet(n,a,b,debug)
    count_obj.get_count()
    
    print("4 : " , count_obj.analyzeNumber(4))
    print("6 : " , count_obj.analyzeNumber(6))
    print("21 : " , count_obj.analyzeNumber(21))
    print("39 : " , count_obj.analyzeNumber(39))
    print("36 : " , count_obj.analyzeNumber(36))
    print("63 : " , count_obj.analyzeNumber(63))
    print("66 : " , count_obj.analyzeNumber(66))
    print("147 : " , count_obj.analyzeNumber(147))
    print("84 : " , count_obj.analyzeNumber(84))
    print("72 : " , count_obj.analyzeNumber(72))
    print("201 : " , count_obj.analyzeNumber(201))
    print("282 : " , count_obj.analyzeNumber(282))
    print("228 : " , count_obj.analyzeNumber(228))
    print("246 : " , count_obj.analyzeNumber(246))
    print("240 : " , count_obj.analyzeNumber(240))
    print("241 : " , count_obj.analyzeNumber(241))
    
    count_obj.displayCount()
    

"""
        X 6  9 12 15 18 (1~5)   1 .. 3+3  1단계 만들어지는 수
        O  1단계 안 만들어지는 수
        
        O 21 30 39 48 57 (6 9 12 15 18 : 1 2 3 4 5 )  [3+3 ~ 3*]  2단계 만들어지는 수
        X 24 27 33 36 42 45 51 54 60 63  (7 8 10 11 13 14 16 17 19 20 )  2단계 안 만들어지는수
        O 1단계 안 만들어지는 수
        
        X 66 93 120 147 174 (21 30 39 48 57 : 6 9 12 15 18 : 1 2 3 4 5) 3단계 만들어지는 수 
        O 75 84 (24 27 : 7 8)  3단계 안 만들어지는 수
        X 69 72 (22 23 ) 2단계 안 만들어지는 수
        O 1단계 안 만들어지는 수
        
        O 201 282 (66 93: 21 30 :6 9 : 1 2) 4단계 만들어지는 수
        X 228 (75 : 24 : 7 )  4단계 안 만들어지는 수
        O 237 246 (78 81 : 25 26)  3단계 안 만들어지는 수
        X 240 (79 ) 2단계 안 만들어지는 수
        O 1단계 안 만들어지는 수

함수1 ()
  계속 나누어 떨어져서 딱 맞아떨어질때 몇 단계까지 가는지 조사
  몇단계까지가서 안 맞아떨어졌는지 조사

함수2()
    딱맞아 떨어지면 odd 이면 안 찍음 , even이면 찍음
    딱맞아떨어지지 않으면 단계가 odd 이면 찍음.

최적화 : 각기 몇개씩 건너뛰면서 처리하면 될지 알수 있음.  
"""