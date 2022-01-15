from collections import defaultdict
# import numpy as np

import sys
import argparse

class Dice:
    """Dice object
    2 4 1 3 5 6
    1 is top (basic)
         2[0]
    4[1] 1[2] 3[3]
         5[4]
         6[5]

    go east
         2[0]
    6[1] 4[2] 1[3]
         5[4]
         3[5]
    a[1<-5] , a[2<-1] , a[3<-2] , a[5<-3] = a[5] , a[1] ,... 
    
    go west
    a[5<-1] , a[1<-2] , a[2<-3] , a[3<-5] = a[5]
    
    go north from basic 
         1[0]
    4[1] 5[2] 3[3]
         6[4]
         2[5]
    a[0<-2] , a[2<-4] , a[4<-5] , a[5<-0]
    
    go south from basic
    a[0<-2] , a[2<-4] , a[4<-5] , a[5<-0]
             
    """
    
    def __init__(self, debug=0):
        """initialization

        Args:
            debug (int, optional): debugging is on if not zero. Defaults to 0.
        """
        self.dice = [2,4,1,3,5,6]
        self.debug = debug
        self.direction = 0  # east
        self.MAX_DIRECTION = 4
        
        if self.debug :
            print("dice:",self.dice)
            
    def east(self):
        self.dice[1] , self.dice[2] , self.dice[3] , self.dice[5] = self.dice[5] , self.dice[1] , self.dice[2] , self.dice[3]
    def west(self):
        self.dice[5] , self.dice[1] , self.dice[2] , self.dice[3] = self.dice[1] , self.dice[2] , self.dice[3] , self.dice[5]
    def north(self):
        self.dice[0] , self.dice[2] , self.dice[4] , self.dice[5] = self.dice[2] , self.dice[4] , self.dice[5] , self.dice[0]
    def south(self):
        self.dice[2] , self.dice[4] , self.dice[5] , self.dice[0] = self.dice[0] , self.dice[2] , self.dice[4] , self.dice[5]
    
    def setClockwise(self,clockwise):
        """set clockwise. next dice will go this direction

        Args:
            clockwise (int): according to count , it will changed with this sequence (clockwise)
                0 : same direction
                1 : clockwise
                -1 : anti-clockwise
        """
        self.direction += clockwise
        self.direction = self.direction % self.MAX_DIRECTION
    
    def go(self,x,y,N,M):    
        """go with self.direction  then return new x,y

        Args:
            x (int): current position (row)
            y (int): current postion (column)
            N (int): board row size
            M (int): board column size

        Returns:
            x,y : int , int  new position
        """
        if self.direction == 0 : # east
            if M == 1 :
                pass
            else :
                if y+1 > M :
                    self.direction = 2
                    self.west()
                    y -= 1
                else :
                    self.east()
                    y += 1
        elif self.direction == 1 : # south
            if N == 1 :
                pass
            else :
                if x+1 > N :
                    self.direction = 3
                    self.north()
                    x -= 1
                else :
                    self.south()
                    x += 1
        elif self.direction == 2 : # west
            if M == 1 :
                pass
            else :
                if y == 1 :
                    self.direction = 0
                    self.east()
                    y += 1
                else :
                    self.west()
                    y -= 1
        else :   #direction == 3 : north
            if N == 1 :
                pass
            else :
                if x == 1 :
                    self.direction = 1
                    self.south()
                    x += 1
                else :
                    self.north()
                    x -= 1

        return x,y
        
        
    def getBottomValue(self):
        """get bottom value of dice

        Returns:
            int : bottom value of dice
        """
        return self.dice[5]
    
class RollingDice2 :
    """
    A class to get the sum rolling dice

    url : https://www.acmicpc.net/problem/2328
    - memory이슈까지 고민하여 문제 풀 예정
        - 주사위 동작할때 변하는 모습 미리 fix : 맨 아래값 고정 , 다음을 위한 변환된 주사위 모양 저장
        - 판에서 현 위치에서와 같은 연결되된 구간의 갯수 구하는 것
    - unittest를 적용해보자. 기본 값을 가졌을때 이미 알고 있는 값들이 있으니 unit test구현 가능할 것으로 보임.

    Attributes
    ----------
    N : row size  (1 ... 20)
    M : column size (1 ... 20)
    k : move count  (1 ... 1000)
    x : x position
    y : y position
    board[a,b] : numpy 2 dimensional array
    debug : int debug mode

    Methods
    -------
    fill()
        get the count of elements to meet the rule.
    count_fill()
        print the elements in debug mode
    """
    
    def __init__(self, debug=0):
        """
        input M,N,k and board information

        :param debug: debug mode
        :return:
        """
        self.debug = debug
        self.N , self.M , self.k = map(int , input().split())
        self.x = 1  # start x (column)
        self.y = 1  # start y (row)
        self.board = [0 for i in range((self.M)*(self.N))]
        self.boardCount = [0 for i in range((self.M)*(self.N))]  # Count with same value as neighborhoods
        if self.debug :
            print("M(C) , N(R) , k : ",self.M , self.N , self.k)
            print("x,y : ",self.x,self.y)
        for r in range(1 , self.N+1) :
            ii = input().split()
            for c in range(1 , self.M+1) :
                self.board[(r-1)*self.M +(c-1)] = int(ii[c-1])
        if self.debug :
            print("board : ",self.board)
        
        self.dice = Dice(self.debug)
        super().__init__()

    def getBoardValue(self,x,y):
        """N(R)*M(C)) 으로 이루어지므로 , 1,1 -> 0,0 (실제 메모리)으로 mapping이 되어야한다.

        Args:
            x (int): 1 ... self.N row
            y (int): 1 ... self.M column

        Returns: int value of board
            if range is out of board , return 0
        """
        if (x < 1) or (x > self.N) :
            return 0
        if (y < 1) or (y > self.M) :
            return 0
        
        return self.board[(x-1)*self.M + y-1]

    def getBoardCountValue(self,x,y):
        """N(R)*M(C)) 으로 이루어지므로 , 1,1 -> 0,0 (실제 메모리)으로 mapping이 되어야한다.

        Args:
            x (int): 1 ... self.N row
            y (int): 1 ... self.M column

        Returns: int value of board
            if range is out of board , return 0
        """
        if (x < 1) or (x > self.N) :
            # print("ERROR :getBoardCountValue : ",x,y)
            return -1
        if (y < 1) or (y > self.M) :
            # print("ERROR :getBoardCountValue : ",x,y)
            return -1
        
        return self.boardCount[(x-1)*self.M + y-1]
    
    def setBoardCountValue(self,x,y,num):
        """N(R)*M(C)) 으로 이루어지므로 , 1,1 -> 0,0 (실제 메모리)으로 mapping이 되어야한다.

        Args:
            x (int): 1 ... self.N row
            y (int): 1 ... self.M column
            num (int) : set value
        """
        if (x < 1) or (x > self.N) :
            print("ERROR :setBoardValue : ",x,y,num)
            return
        if (y < 1) or (y > self.M) :
            print("ERROR :setBoardValue : ",x,y,num)
            return
        
        self.boardCount[(x-1)*self.M + y-1] = num
        
    def printBoard(self):
        """print Board and BoardCount
        """
        print()
        print("=Print Board")
        print("==board")
        print("NM ",end="")
        for c in range(1 , self.M+1) :
            print(" ",c,end="")
        print()
        for r in range(1 , self.N+1) :
            print(r," ",end="")
            for c in range(1 , self.M+1) :
                print(" ",self.board[(r-1)*self.M +(c-1)],end="")
            print()
        
        print()
        print("==boardCount")
        print("NM ",end="")
        for c in range(1 , self.M+1) :
            print(" ",c,end="")
        print()
        for r in range(1 , self.N+1) :
            print(r," ",end="")
            for c in range(1 , self.M+1) :
                print(" ",self.boardCount[(r-1)*self.M +(c-1)],end="")
            print()    
            

        
    def getBoardCountSameNumber(self):
        """get boardCount to set the count of number with same value
        
        result is boardCount.
        """
        if self.debug :
            print("-getBoardCountSameNumber")
        for r in range(1 , self.N+1) :
            for c in range(1 , self.M+1) :
                self.getCountSameNumber(r,c)
        
    def getCountSameNumber(self,x,y):
        """count with the same number of (x,y)

        Args:
            x (int): 1 ... self.N row
            y (int): 1 ... self.M column
        """
        if self.getBoardCountValue(x,y) != 0:
            return
        checkBoard = [0 for i in range((self.M)*(self.N))]
        checkBoard[(x-1)*self.N+y-1]=1
        checkedBoardArray=[]
        self.globalCountOfSameValue = 1
        v = self.getBoardValue(x,y)
        
        if self.debug :
            print("--getCountSameNumber",x,y,v)
        self.goSameNumber(x-1,y,v,checkBoard,checkedBoardArray)
        self.goSameNumber(x+1,y,v,checkBoard,checkedBoardArray)
        self.goSameNumber(x,y-1,v,checkBoard,checkedBoardArray)
        self.goSameNumber(x,y+1,v,checkBoard,checkedBoardArray)
        checkedBoardArray.append([x,y])
        for xi,yi in checkedBoardArray :
            self.setBoardCountValue(xi,yi,self.globalCountOfSameValue)

    def goSameNumber(self,x,y,v,checkBoard,checkedBoardArray):
        if self.getBoardCountValue(x,y) != 0:
            return
        if checkBoard[(x-1)*self.N+y-1] != 0:
            return
        thisV = self.getBoardValue(x,y)
        if thisV != v:
            return
        else :
            if self.debug :
                print("goSameNumber",self.globalCountOfSameValue,x,y,v,self.getBoardValue(x,y))
                print("  checkboard:",checkBoard)
            self.globalCountOfSameValue += 1
            checkBoard[(x-1)*self.N+y-1]=1
            self.goSameNumber(x-1,y,v,checkBoard,checkedBoardArray)
            self.goSameNumber(x+1,y,v,checkBoard,checkedBoardArray)
            self.goSameNumber(x,y-1,v,checkBoard,checkedBoardArray)
            self.goSameNumber(x,y+1,v,checkBoard,checkedBoardArray)
            checkedBoardArray.append([x,y])
            
    def rollingDice(self):
        # self.printBoard()
        self.getBoardCountSameNumber() # boardCount is the result
        self.result = 0
        # self.printBoard()
        
        x , y = 1 , 1
        for k in range(1 , self.k+1):
            x,y = self.dice.go(x,y, self.N , self.M )
            bottom = self.dice.getBottomValue()
            boardValue = self.getBoardValue(x,y)
            if bottom > boardValue :
                self.dice.setClockwise(1)
            elif bottom < boardValue :
                self.dice.setClockwise(-1)
            self.result += (boardValue * self.getBoardCountValue(x,y) )
        
        # print("result:",self.result)
        print(self.result)
            
               
if (__name__ == "__main__"):
    dbg = 0
    parser = argparse.ArgumentParser(
        prog='AreaColorPaper.py',
        description=
        'size of filled with color paper in the board'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    dbg = args.debug
    if not dbg:
        dbg = 0
    
    if dbg :
            print("dbg:",dbg)
    # n = int( input() )
    # inx=[]
    # iny=[]
    # for i in range(n):
    #     x,y = map(int, input().split())
    #     if debug :
    #         print(i,":",x,y)
    #     inx.append(x)
    #     iny.append(y)
        

    rd = RollingDice2(dbg)
    rd.rollingDice()
    # print(rd.getBoardValue(1,2))
    # rd.printBoard()
    # rd.getBoardCountSameNumber()
    # rd.printBoard()

    # dc = Dice(dbg)
    # print(dc.getBottomValue())
    # dc.east()
    # print(dc.getBottomValue())
    

