- [1. leetcode](#1-leetcode)
- [2. Meidan of Two Sorted Arrays](#2-meidan-of-two-sorted-arrays)
- [3. Regular Expression Matching](#3-regular-expression-matching)
- [4. Strange Printer](#4-strange-printer)
- [5. Third Maximum Number](#5-third-maximum-number)
- [6. Find All Numbers Disappeared in an Array](#6-find-all-numbers-disappeared-in-an-array)
- [7. Squares of a Sorted Array](#7-squares-of-a-sorted-array)
- [8. Remove Duplicates from Sorted Array](#8-remove-duplicates-from-sorted-array)
- [9. Single Number](#9-single-number)
- [10. Plus One](#10-plus-one)
- [11. Remove Nth Node From End of List (Linked List)](#11-remove-nth-node-from-end-of-list-linked-list)
- [12. Convert Sorted Array to Binary Search Tree (Trees : Height-Balanced Binary Search Trees)](#12-convert-sorted-array-to-binary-search-tree-trees--height-balanced-binary-search-trees)
- [13. is Balanced Binary Tree](#13-is-balanced-binary-tree)
- [14. First Bad Version](#14-first-bad-version)

--------------------
# 1. leetcode

# 2. Meidan of Two Sorted Arrays
- hard
- https://leetcode.com/problems/median-of-two-sorted-arrays/
- [findMedianSortedArrays2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findMedianSortedArrays2.py) : passed
- ex
  - [][] , [2][] , [][2] , [2][2] , [2][1,3,4] 

# 3. Regular Expression Matching
- hard
- https://leetcode.com/problems/regular-expression-matching/
- [isMatch.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch.py) : wrong answer
- [isMatch_dfs.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch_dfs.py) : time limit exceeded : 38 / 353 test cases passed.
- [isMatch.c](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch.c) : Code in site : time limit exceeded : 353 / 353 test cases passed, but took too long.

# 4. Strange Printer
- hard : DP dynamic programming
- https://leetcode.com/problems/strange-printer/
- get the code and hint from discussion
- [strangePrinter.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/strangePrinter.py) : passed

# 5. Third Maximum Number
- easy
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
- [thirdMaximumNumber.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/thirdMaximumNumber.py) : passed

# 6. Find All Numbers Disappeared in an Array
- medium : O(N)
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
- [findDisappearedNumbers.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findDisappearedNumbers.py) : passed

# 7. Squares of a Sorted Array
- medium : O(N)
- Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
- [sortedSquares.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortedSquares.py) : passed

# 8. Remove Duplicates from Sorted Array
- easy : Array
- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
- [removeDuplicates.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeDuplicates.py) : passed 
  - we should add empty lists to the
  - if len(nums) == 0 : return 0

# 9. Single Number
- easy or hard : Arrays
- Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
- [singleNumber.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/singleNumber.py) : passed 
  - O(N)
  - but , i used the dictionay with size of array.   is it a constant extra space? (NO)

# 10. Plus One
- easy : Array
- You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
  - Increment the large integer by one and return the resulting array of digits.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
- [plusOne.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/plusOne.py) : passed

# 11. Remove Nth Node From End of List (Linked List)
- easy : Linked List
- Given the head of a linked list, remove the nth node from the end of the list and return its head.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
- [removeNthFromEnd.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeNthFromEnd.py) : passed

# 12. Convert Sorted Array to Binary Search Tree (Trees : Height-Balanced Binary Search Trees)
- easy : Trees , but it is not AVL.
- Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree : https://www.programiz.com/dsa/avl-tree
  - avl.py
- Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
  - A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
- [sortedArrayToBST.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortedArrayToBST.py) : passed

# 13. is Balanced Binary Tree
- easy : Trees
- Given a binary tree, determine if it is height-balanced.
- For this problem, a height-balanced binary tree is defined as:
- a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
- https://leetcode.com/problems/balanced-binary-tree/
- [isBalanced2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isBalanced2.py) : passed
  - [isBalanced.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isBalanced.py) : running is ok. but it has warning in vsc.

# 14. First Bad Version
- easy : Sorting and Searching
- You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
- Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
- You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
- At first time I try to find sequentially.  but time exceeded.
- [firstBadVersion.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/firstBadVersion.py) : passed



