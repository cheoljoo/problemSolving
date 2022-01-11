from collections import defaultdict
import numpy as np

import sys
import argparse

BOARD_X = 100
BOARD_Y = 100
COLOR_PAPER_SIZE = 10

class AreaColorPaper :
    """
    A class used to get the count of elements

    url : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=712&sca=2060#n
    가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
    이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
    이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

    cross : 2차원 배열 100 x 100
    if x=0 , y=0 => cross[0~9][0~9] are filled  => for i in range(x,x+10) 
    finally check the filled count.

    Attributes
    ----------
    n : count of color paper
    a[] : x position
    b[] : y position
    debug : int debug mode

    Methods
    -------
    fill()
        get the count of elements to meet the rule.
    count_fill()
        print the elements in debug mode
    """
    
    def __init__(self, n , x , y, debug=0):
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
        self.x = x
        self.y = y
        self.board = np.zeros((BOARD_X,BOARD_Y),dtype=np.int8)
        if debug :
            print("x array : ",x)
            print("y array : ",y)
            print("board : ",self.board)
        super().__init__()

    def fill(self):
        """fill the board with input x,y array
        
        if x=0 , y=0 => cross[0~9][0~9] are filled  => for i in range(x,x+10) 
        """
        for i in range(self.n):
            for x in range(self.x[i],self.x[i]+COLOR_PAPER_SIZE):
                for y in range(self.y[i],self.y[i]+COLOR_PAPER_SIZE):
                    self.board[x,y] = 1
    
    def count_filled(self):
        """occupied paper size.
        returns: int count of filled
        """
        count = 0
        for x in range(BOARD_X):
            for y in range(BOARD_Y):
                if self.board[x,y] == 1:
                    count += 1
        
        return count


if (__name__ == "__main__"):
    debug = 0
    parser = argparse.ArgumentParser(
        prog='AreaColorPaper.py',
        description=
        'size of filled with color paper in the board'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 1
    
    n = int( input() )
    inx=[]
    iny=[]
    for i in range(n):
        x,y = map(int, input().split())
        if debug :
            print(i,":",x,y)
        inx.append(x)
        iny.append(y)
        

    acp = AreaColorPaper(n,inx,iny,debug)
    acp.fill()
    print(acp.count_filled())


