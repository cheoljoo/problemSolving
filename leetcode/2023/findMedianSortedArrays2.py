from collections import defaultdict
#import numpy as np

import sys
import argparse
import math
import random

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        self.SEQUENTIAL_LIMIT = 2
        self.totalSize = len(nums1) + len(nums2)
        # 1,2,3   4,5,6   even : 3,4 의 중간값이므로 뒤의 4까지  즉 갯수로 count할때는 total//2 + 1
        # 1,2,3   4,5     odd : 3이 중간값 즉 갯수로 count할때는 total//2 + 1
        self.totalHalfCount = self.totalSize // 2 + 1
        self.isEven = False
        if (self.totalSize % 2) == 0:
            self.isEven = True
            
        self.nums1ConfirmedIndex = 0
        self.nums2ConfirmedIndex = 0
        # strait sequence (last element of one list is less than the first element of the other list)
        if (len(nums1) == 0) and (len(nums2) == 0) :  # [] []
            return 0.0
        if (len(nums1) == 1) and (len(nums2) == 1) :   # [1] [1]
            return (nums1[0] + nums2[0]) /2
        if len(nums1) == 0 :   # [] [1]   , [2] []
            return self.strait(nums1,nums2,self.isEven)
        elif len(nums2) == 0 :   # [] [1]   , [2] []
            return self.strait(nums2,nums1,self.isEven)
        elif nums1[-1] < nums2[0] :
            return self.strait(nums1,nums2,self.isEven)
        elif nums2[-1] < nums1[0] :
            return self.strait(nums2,nums1,self.isEven)
                
        # totalHalfCount 는 Index의 숫자까지 포함
        if self.isEven == True:
            if len(nums1) >= len(nums2) :
                self.nums1HalfIndex = len(nums1) // 2 + 1 - 1   # +1 for count , -1 for index
                self.nums2HalfIndex = self.totalHalfCount - (self.nums1HalfIndex+1) - 1
            else :
                self.nums2HalfIndex = len(nums2) // 2 + 1 - 1 
                self.nums1HalfIndex = self.totalHalfCount - (self.nums2HalfIndex+1) - 1
        else :
            if len(nums1) >= len(nums2) :
                self.nums1HalfIndex = len(nums1) // 2 
                self.nums2HalfIndex = self.totalHalfCount - self.nums1HalfIndex - 1
            else :
                self.nums2HalfIndex = len(nums2) // 2
                self.nums1HalfIndex = self.totalHalfCount - self.nums2HalfIndex - 1
                           
        # 
        self.halfMinSize = min(self.nums1HalfIndex + 1 , self.nums2HalfIndex + 1) // 2
        while True:
            if (self.nums1HalfIndex >= len(nums1)) or (self.nums1HalfIndex < 0) :
                print("error-1")
                break
            if (self.nums2HalfIndex >= len(nums2)) or (self.nums2HalfIndex < 0) :
                print("error-2")
                break
            if self.halfMinSize < self.SEQUENTIAL_LIMIT:
                if nums1[self.nums1HalfIndex] <  nums2[self.nums2HalfIndex] :
                    return self.mergeSequential(nums1,self.nums1ConfirmedIndex,self.nums1HalfIndex,nums2,self.nums2ConfirmedIndex,self.nums2HalfIndex, self.isEven)
                else :
                    return self.mergeSequential(nums2,self.nums2ConfirmedIndex,self.nums2HalfIndex,nums1,self.nums1ConfirmedIndex,self.nums1HalfIndex, self.isEven)
            
            if nums1[self.nums1HalfIndex] < nums2[self.nums2HalfIndex] :
                #print("< nums1HalfIndex:",self.nums1HalfIndex , " nums2HalfIndex:",self.nums2HalfIndex , " half:",self.halfMinSize)
                self.nums1ConfirmedIndex = self.nums1HalfIndex   # ConfirmnedIndex is 1 => only [0] is confirmed
                self.nums1HalfIndex += self.halfMinSize
                self.nums2HalfIndex -= self.halfMinSize
                self.halfMinSize //= 2
                #print("   < nums1HalfIndex:",self.nums1HalfIndex , " nums2HalfIndex:",self.nums2HalfIndex , " half:",self.halfMinSize)
            else :
                #print("> nums1HalfIndex:",self.nums1HalfIndex , " nums2HalfIndex:",self.nums2HalfIndex , " half:",self.halfMinSize)
                self.nums1HalfIndex -= self.halfMinSize
                self.nums2ConfirmedIndex = self.nums2HalfIndex   # ConfirmnedIndex is 1 => only [0] is confirmed
                self.nums2HalfIndex += self.halfMinSize
                self.halfMinSize //= 2
                #print("   > nums1HalfIndex:",self.nums1HalfIndex , " nums2HalfIndex:",self.nums2HalfIndex , " half:",self.halfMinSize)

    def mergeSequential(self,nums1,nums1ConfirmedIndex,nums1EndIndex,nums2,nums2ConfirmedIndex,nums2EndIndex,isEven):
        """merge sequentially with sorted two list
        
        nums1[nums1Start] is less than nums2[nums2Start]

        Args:
            nums1 (list): direction is positive.
            nums1Start (int): [description]
            nums2 (list): direction is negative.
            nums2Start (int): [description]
            isEven (bool): [description]
        Returns: float : median value
        """
        calCount = self.totalHalfCount - nums1ConfirmedIndex - nums2ConfirmedIndex
        num1Index = nums1ConfirmedIndex
        num2Index = nums2ConfirmedIndex
        numMax1st = 0
        numMax2nd = 0
        for i in range(0,calCount):
            if num1Index == len(nums1):   # [2] [1,3,4]
                if nums2[num2Index] >= numMax1st :
                    numMax2nd = numMax1st
                    numMax1st = nums2[num2Index]
                elif nums2[num2Index] > numMax2nd :
                    numMax2nd = nums2[num2Index]
                num2Index += 1
            elif num2Index == len(nums2):   # [2] [1,3,4]
                if nums1[num1Index] >= numMax1st :
                    numMax2nd = numMax1st
                    numMax1st = nums1[num1Index]
                elif nums1[num1Index] > numMax2nd :
                    numMax2nd = nums1[num1Index]
                num1Index += 1
            elif nums1[num1Index] == nums2[num2Index]:
                if nums1[num1Index] >= numMax1st :
                    numMax2nd = numMax1st
                    numMax1st = nums1[num1Index]
                elif nums1[num1Index] > numMax2nd :
                    numMax2nd = nums1[num1Index]
                if (num1Index + 1) == len(nums1):               # [0,0] [0,0]   , [1] [1]
                    num2Index += 1 
                else :
                    num1Index += 1
            elif nums1[num1Index] < nums2[num2Index]:
                if nums1[num1Index] >= numMax1st :
                    numMax2nd = numMax1st
                    numMax1st = nums1[num1Index]
                elif nums1[num1Index] > numMax2nd :
                    numMax2nd = nums1[num1Index]
                num1Index += 1
            else :
                if nums2[num2Index] >= numMax1st :
                    numMax2nd = numMax1st
                    numMax1st = nums2[num2Index]
                elif nums2[num2Index] > numMax2nd :
                    numMax2nd = nums2[num2Index]
                num2Index += 1               
            
        
        if isEven == True:
            return (numMax1st + numMax2nd)/2
        else:
            return (numMax1st) * 1.0

    
    def strait(self,nums1,nums2,isEven):
        """ last element of one list is less than the first element of the other list
        
        nums1[-1] is bigger than nums2[0]
        """  
        totalSize = len(nums1) + len(nums2)
        if isEven == True:           
            if len(nums1) == len(nums2):
                return (nums1[-1] + nums2[0])/2
            elif len(nums1) > len(nums2) :
                halfSizeIndex = totalSize // 2
                return (nums1[halfSizeIndex-1] + nums1[halfSizeIndex])/2
            else :
                halfSizeIndex = totalSize // 2
                halfSizeIndex -= len(nums1)
                return (nums2[halfSizeIndex-1] + nums2[halfSizeIndex])/2
        else :
            if len(nums1) > len(nums2) :
                halfSizeIndex = totalSize // 2
                return nums1[halfSizeIndex] * 1.0
            else :
                halfSizeIndex = totalSize // 2
                halfSizeIndex -= len(nums1)
                return nums2[halfSizeIndex] * 1.0
        

# OO is old and old (previous and previous) : if we have the same value in previous item , we should stop.
# 최종 처리하는 사이즈가 ?미만 일때는 sequential merge를 돌린다. 
#     끝의 처리가 힘들므로 ? 미만은 sequential로 처리
# 

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

    nums1 = [2,3,3]
    nums2 = [2,2,3]
    

    # nums1 = []
    # nums2 = []
    # for i in range(0,100):
    #     n = random.randint(1,3000)
    #     if n % 2 == 0 :
    #         nums1.append(n)
    #     else :
    #         nums2.append(n)
    # nums1.sort()
    # nums2.sort()
    
    merge = Solution()
    print(merge.findMedianSortedArrays(nums1,nums2))
