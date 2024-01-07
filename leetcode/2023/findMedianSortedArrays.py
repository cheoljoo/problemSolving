from collections import defaultdict
#import numpy as np

import sys
import argparse
import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        #self.LIMIT = 4
        self.size = len(nums1) + len(nums2)
        self.isEvenCount = False
        if (self.size % 2) == 0:
            self.isEvenCount = True
        self.midSize = self.size // 2      # 0 ... midIndex    # 0 1 (2) 3 4   notEven 2 is mid
                                           # 0 ... midIndex # 0 1 (2) 3    Even 2 and 2-1 is mid

        self.nums1MidIndex = len(nums1) // 2    # MidIndex is prior count less than Mid
        self.nums2MidIndex = self.midSize - self.nums1MidIndex
        #if min(self.nums1MidIndex + 1 , self.nums2MidIndex + 1) <  self.LIMIT :
        self.halfMinSize = min(self.nums1MidIndex + 1 , self.nums2MidIndex + 1) // 2
        self.nums1OldIndex = -1
        self.nums1OOIndex = -1
        print("midSize:", self.midSize , " , nums1MidIndex:",self.nums1MidIndex , " , nums2MidIndex:",self.nums2MidIndex)
        while True:
            if (self.nums1MidIndex >= len(nums1)) or (self.nums1MidIndex < 0) :
                break;
            if (self.nums2MidIndex >= len(nums2)) or (self.nums2MidIndex < 0) :
                break;
            if nums1[self.nums1MidIndex] < nums2[self.nums2MidIndex] :
                print("< nums1MidIndex:",self.nums1MidIndex , ",OO:" , self.nums1OOIndex, ", nums2MidIndex:",self.nums2MidIndex , " , half:",self.halfMinSize)
                self.nums1MidIndex += self.halfMinSize
                self.nums2MidIndex -= self.halfMinSize
                if self.halfMinSize <= 1 :
                    #break
                    self.halfMinSize = 1
                else :
                    self.halfMinSize //= 2
                print("< nums1MidIndex:",self.nums1MidIndex , ",OO:" , self.nums1OOIndex, ", nums2MidIndex:",self.nums2MidIndex , " , half:",self.halfMinSize)
            else :
                print("> nums1MidIndex:",self.nums1MidIndex , ",OO:" , self.nums1OOIndex, ", nums2MidIndex:",self.nums2MidIndex , " , half:",self.halfMinSize)
                self.nums1MidIndex -= self.halfMinSize
                self.nums2MidIndex += self.halfMinSize
                if self.halfMinSize <= 1 :
                    #break
                    self.halfMinSize = 1
                else :
                    self.halfMinSize //= 2
                print("> nums1MidIndex:",self.nums1MidIndex , ",OO:" , self.nums1OOIndex, ", nums2MidIndex:",self.nums2MidIndex , " , half:",self.halfMinSize)
            if self.nums1OOIndex == self.nums1MidIndex :
                print("==")
                break
            else :
                self.nums1OOIndex = self.nums1OldIndex
                self.nums1OldIndex = self.nums1MidIndex
        print("nums1MidIndex:",self.nums1MidIndex , " , nums2MidIndex:",self.nums2MidIndex)
        if self.nums1MidIndex == -1:
            if self.isEvenCount == False : # odd
                return float(nums2[self.midSize])
            else : #even
                return (nums2[self.midSize-1] + nums2[self.midSize])/2
        elif self.nums2MidIndex == -1:
            if self.isEvenCount == False : # odd
                return float(nums1[self.midSize])
            else : #even
                return (nums1[self.midSize-1] + nums1[self.midSize])/2
        elif self.nums1MidIndex >= len(nums1):
            if self.isEvenCount == False : # odd
                return float(nums2[self.midSize])
            else : #even
                return (nums2[self.midSize-1] + nums2[self.midSize])/2


# OO is old and old (previous and previous) : if we have the same value in previous item , we should stop.
# 여기는 너무 끝의 처리가 너무 힘들다. 

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/median-of-two-sorted-arrays/

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

    nums1 = [1,2,3,8,19]
    nums2 = [14,15,16,17]
    merge = Solution()
    print(merge.findMedianSortedArrays(nums1,nums2))
