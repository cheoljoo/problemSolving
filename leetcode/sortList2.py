from collections import defaultdict
import enum
from re import A
#import numpy as np

import sys
import argparse
import math
import random
from tkinter import N
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import time

# sortList2.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        return self.bSort(head)

    def sortedMerge(self,head1,head2):
        if not head1 :
            return head2
        if not head2 :
            return head1
        head = None
        if head1.val < head2.val:
            head = head1
        else :
            head = head2
        
        while head1 and head2 :
            if head1.val < head2.val:
                cur = head1
                head1 = head1.next
            else :
                cur = head2
                head2 = head2.next
                
            if not head1 :
                cur.next = head2
            elif not head2 :
                cur.next = head1
            else :
                if head1.val < head2.val :
                    cur.next = head1
                else :
                    cur.next = head2
        return head
                
        
    def bSort(self,head):
        if (not head) or (not head.next):
            return head
        if not head.next.next : # it is just two nodes
            if head.val > head.next.val:  
                t = head.next
                head.next = t.next
                t.next = head
                return t
            else :
                return head
        # more than 3 nodes
        mid = self.mid(head)
        return self.sortedMerge(self.bSort(head), self.bSort(mid))
        
    def mid(self,head):
        fast = head
        slow = head
        prev = slow
        while(fast and fast.next):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        return slow
        
        
        
            
def run(s,expect):
    pNode = None
    head = None
    for n in reversed(s):
        head = ListNode(n,pNode)
        pNode = head
    start = time.time()
    A = Solution()
    sortHead = A.sortList(head)
    print(" , total_time :", time.time() - start , "-> ", end="") 
    
    r = []
    while sortHead :
        r.append(sortHead.val)
        sortHead = sortHead.next
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print("len:%d"%len(s), r , ": " , end="")  
    if len(s) < 20 : print(s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='sortList.py',
        description=
        'sortList'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('sortList problem :')

    s = [4,2,1,3]
    run(s,[1,2,3,4])
    s = [-1,5,3,4,0]
    run(s,[-1,0,3,4,5])
    s = []
    run(s,[])
    s= [3,5,6,4,7,10,20,40,30,9,2,1,15]
    run(s,[1,2,3,4,5,6,7,9,10,15,20,30,40])
    

    
    