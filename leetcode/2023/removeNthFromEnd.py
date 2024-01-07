from collections import defaultdict
from re import A
#import numpy as np

import sys
import argparse
import math
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        c = head
        count = 0
        while c :
            c = c.next
            count += 1
        
        if (count == n) or (count == 1 and n == 1):
            head = head.next
            return head
        
        c = head
        for _ in range(count-n-1):
            c = c.next
        
        c.next = c.next.next
        return head

def linkedlist2list(rHead:ListNode) -> list:
    r = []
    c = rHead
    while c:
        r.append(c.val)
        c = c.next
    return r

def printHead(head):
    c = head
    while c:
        print(c.val , " " , end="")
        c = c.next
    print()

def run(s,n,expect):
    A = Solution()
    head = None
    prev = head
    for i in s:
        c = ListNode(i)
        if head == None :
            head = c
            prev = c
        else :
            prev.next = c
            prev = c
    printHead(head)
    rHead = A.removeNthFromEnd(head,n)
    printHead(rHead)
    r = linkedlist2list(rHead)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

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

    s = [1,2,3,4,5]
    run(s,2,[1,2,3,5])
    s = [1]
    run(s,1,[])
