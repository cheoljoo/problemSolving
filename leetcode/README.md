- [1. leetcode](#1-leetcode)
- [2. Meidan of Two Sorted Arrays](#2-meidan-of-two-sorted-arrays)
- [3. Regular Expression Matching](#3-regular-expression-matching)
- [4. Strange Printer](#4-strange-printer)
- [5. Third Maximum Number](#5-third-maximum-number)
- [6. Find All Numbers Disappeared in an Array](#6-find-all-numbers-disappeared-in-an-array)
- [7. Squares of a Sorted Array](#7-squares-of-a-sorted-array)
- [8. Remove Duplicates from Sorted Array](#8-remove-duplicates-from-sorted-array)

--------------------
# 1. leetcode

# 2. Meidan of Two Sorted Arrays
- hard
- https://leetcode.com/problems/median-of-two-sorted-arrays/
- findMedianSortedArrays2.py
- solved
- ex
  - [][] , [2][] , [][2] , [2][2] , [2][1,3,4] 

# 3. Regular Expression Matching
- hard
- https://leetcode.com/problems/regular-expression-matching/
- isMatch.py : wrong answer
- isMatch_dfs.py : time limit exceeded : 38 / 353 test cases passed.
- isMatch.c : Code in site : time limit exceeded : 353 / 353 test cases passed, but took too long.

# 4. Strange Printer
- hard
- https://leetcode.com/problems/strange-printer/
- get the code and hint from discussion
- strangePrinter.py : passed

# 5. Third Maximum Number
- easy
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
- thirdMaximumNumber.py : passed

# 6. Find All Numbers Disappeared in an Array
- medium : O(N)
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
- findDisappearedNumbers.py : passed

# 7. Squares of a Sorted Array
- medium : O(N)
- Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
- sortedSquares.py : passed

# 8. Remove Duplicates from Sorted Array
- easy : Array
- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
- removeDuplicates.py : passed 
  - we should add empty lists to the
  - if len(nums) == 0 : return 0

