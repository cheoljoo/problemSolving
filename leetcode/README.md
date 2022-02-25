- [1. knowledge](#1-knowledge)
  - [1.1. sort performance](#11-sort-performance)
  - [1.2. sort keys](#12-sort-keys)
  - [1.3. Euclidean-algorithm : 유클리드 호제법](#13-euclidean-algorithm--유클리드-호제법)
  - [1.4. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree](#14-height-balanced-binary-search-trees--avlcreatoradelson-velsky-and-landis-tree)
  - [1.5. hamming weight : number of '1' bits](#15-hamming-weight--number-of-1-bits)
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
- [15. Maximum Subarray](#15-maximum-subarray)
- [16. Remove Outermost Parentheses (#1021)](#16-remove-outermost-parentheses-1021)
- [17. Zigzag Conversion (#6)](#17-zigzag-conversion-6)
- [18. House Robber (#198)](#18-house-robber-198)
- [19. Shuffle an Array (#384)](#19-shuffle-an-array-384)
- [20. Number of 1 Bits (#191)](#20-number-of-1-bits-191)
- [21. Hamming Distance (#461)](#21-hamming-distance-461)
- [22. Missing Number (#268)](#22-missing-number-268)
- [23. Minimize Deviation in Array (#1675)](#23-minimize-deviation-in-array-1675)
- [24. Remove Covered Intervals (#1288)](#24-remove-covered-intervals-1288)
- [25. All Divisions With the Highest Score of a Binary Array](#25-all-divisions-with-the-highest-score-of-a-binary-array)
- [26. Majority Element](#26-majority-element)
- [27. The Skyline Problem (#218) - Hard](#27-the-skyline-problem-218---hard)
- [28. Clone Graph (#133)](#28-clone-graph-133)
- [29. Sort List (#148)](#29-sort-list-148)
- [30. Compare Version Numbers (#165)](#30-compare-version-numbers-165)

--------------------
leetcode
# 1. knowledge
## 1.1. sort performance
- update and sort is faster than update-insert each elements
  - slow : remove() and bisect.insort()
  - fast : nums[]=? and sort()

## 1.2. sort keys
- https://realpython.com/python-sort/
- https://www.programiz.com/python-programming/methods/built-in/sorted
- runners.sort(key=lambda x: getattr(x, 'duration'))
```python
    >>> words = ['banana', 'pie', 'Washington', 'book']
    >>> sorted(words, key=lambda x: x[::-1], reverse=True)
    ['Washington', 'book', 'pie', 'banana']

    >>> phrases = ['when in rome', 
    ...     'what goes around comes around', 
    ...     'all is fair in love and war'
    ...     ]
    >>> phrases.sort(key=lambda x: x.split()[2][1], reverse=True)
    >>> phrases
    ['what goes around comes around', 'when in rome', 'all is fair in love and war']

    >>> from collections import namedtuple
    >>> StudentFinal = namedtuple('StudentFinal', 'name grade')
    >>> bill = StudentFinal('Bill', 90)
    >>> patty = StudentFinal('Patty', 94)
    >>> bart = StudentFinal('Bart', 89)
    >>> students = [bill, patty, bart]
    >>> sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True)
    [StudentFinal(name='Patty', grade=94), StudentFinal(name='Bill', grade=90), StudentFinal(name='Bart', grade=89)]
```

## 1.3. Euclidean-algorithm : 유클리드 호제법
- https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95 - good explanation with movie
```c
int GCD(int a, int b){
  int tmp;
  while(b){      //b가 0이 될 때까지
    tmp = a % b;
    a = b;
    b = tmp;
  }
  return a;
}
```

## 1.4. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree
- https://www.programiz.com/dsa/avl-tree
- [avl.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/avl.py)

## 1.5. hamming weight : number of '1' bits
- Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://shumin.co.kr/algorithm-hamming-weight-bit-count/)).

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
  - [avl.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/avl.py)
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

# 15. Maximum Subarray
- easy : DP dynamic programming  (나는 hard)
- Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- A subarray is a contiguous part of an array.
- Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
- [maxSubArray.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxSubArray.py) : timeout
  - RecursionError: maximum recursion depth exceeded in comparison
- [maxSubArray-norecursion.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxSubArray-norecursion.py) : O(N**2) it is not good. -> O(N) ?
- [maxSubArray-norecursion2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxSubArray-norecursion2.py) : passed O(N)  - this is not DP.
  - refer to discussion : https://leetcode.com/problems/maximum-subarray/discuss/159849/Python-solution
    - we should change my idea for O(N) : my code is not proper answer for start and end position. but we can get the right maxSubArray answer. -> solved
    - if subSum is negative , we can restart. 

# 16. Remove Outermost Parentheses (#1021)
- easy : 
- Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
- Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
- https://leetcode.com/problems/remove-outermost-parentheses/
- [removeOuterParentheses.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeOuterParentheses.py) : passed

# 17. Zigzag Conversion (#6)
- medium
- The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
 A P L S I I G
  Y   I   R
```
  - And then read line by line: "PAHNAPLSIIGYIR"
- https://leetcode.com/problems/zigzag-conversion/
- [zigzagConversion.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/zigzagConversion.py) : passed

# 18. House Robber (#198)
- medium
- You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
- Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/    https://leetcode.com/problems/house-robber/
- [rob.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/rob.py) : passed

# 19. Shuffle an Array (#384)
- medium : 판정 기준이 애매함.
- Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/    https://leetcode.com/problems/shuffle-an-array/
- passed

# 20. Number of 1 Bits (#191)
- easy : hamming weight 
- Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://shumin.co.kr/algorithm-hamming-weight-bit-count/)).
- https://leetcode.com/problems/number-of-1-bits/ 
- passed : C (unsigned int) , python3 (int) 

- 8 bit : 1. shift 8  2. table
- 32bit : 1. shift 32 2. hamming weight-1 (4 operation * 5(1,2,4,8,16))  3. hamming weight-2 (4 operation * count) if count <= 5

# 21. Hamming Distance (#461)
- easy : hamming distance / hamming weight (number of 1 bits)
```
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
```
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/     https://leetcode.com/problems/hamming-distance/
- [hammingDistance.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/hammingDistance.py) : passed

# 22. Missing Number (#268)
- easy : jongkyung.byun teaches me. len() * (len() +1) / 2 is total sum.  so your missing number = total sum - input sum
- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/    https://leetcode.com/problems/missing-number/
- [missingNumber.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/missingNumber.py) : passed

# 23. Minimize Deviation in Array (#1675)
- hard
- You are given an array nums of n positive integers.
```
You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.
```
- we choose 2 number : max even , min odd -> then do
- https://leetcode.com/problems/minimize-deviation-in-array/
- [minimumDeviation.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumDeviation.py) : 71 / 76 test cases passed.
- [minimumDeviation2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumDeviation2.py) : 75 / 76 test cases passed.  Status: Time Limit Exceeded
- [minimumDeviation3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumDeviation3.py) : optiomization (add time function)  75 / 76 test cases passed.  Status: Time Limit Exceeded
- [minimumDeviation4.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumDeviation4.py) : optiomization (add time function)  75 / 76 test cases passed.  Status: Time Limit Exceeded
  - sort time : 0.0 -> do2 time : 0.2184154987335205 -> do3 time : 0.0 -> do4-1 time : 0.0 -> do4-2 time : 0.0 -> do4-3 time : 0.0 ->   total_time : 0.22439837455749512 -> len(10000)
    - do2 :   # length(10000) 1.0s -> 0.2
    - do4-1 : # length(10000) 0.5s -> 0.0
  - sort time : 0.0 -> do2 time : 0.6432626247406006 -> do3 time : 0.0 -> do4-1 time : 0.0 -> do4-2 time : 0.001994609832763672 -> do4-3 time : 0.0 ->   total_time : 0.6572427749633789 -> len(20000)
  - sort time : 0.000982046127319336 -> do2 time : 4.376241207122803 -> do3 time : 0.0 -> do4-1 time : 0.0 -> do4-2 time : 0.00399017333984375 -> do4-3 time : 0.0 ->   total_time : 4.400253772735596 -> len(50000)
  - sort time : 0.0009975433349609375 -> **_do2 time : 21.690882444381714_** -> do3 time : 0.0 -> do4-1 time : 0.0009968280792236328 -> do4-2 time : 0.006982088088989258 -> do4-3 time : 0.0 ->   **_total_time : 21.740752696990967 -> len(100000)_**
- [minimumDeviation5.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumDeviation5.py) : passed
  - sort time : 0.022464990615844727 -> **_do2 time : 0.015959501266479492_** -> do3 time : 0.0 -> do4-1 time : 0.01715397834777832 -> do4-2 time : 0.03398728370666504 -> do4-3 time : 0.0 ->   total_time : 0.8623092174530029 -> len(20000)
  - **_total_time : 0.2331395149230957 -> len(100000)_**
- description in korean
  - sort()
  - getMaxOddNumber : this value will not changed. all values are compared with MaxOddNumber. 
  - do2() : fold all even number until below maxOddNumber if deviation will reduce
    - maxOddNumber보다 큰 짝수들은 모두 deviation이 기존 것보다 작아질때 반씩 줄여준다/접어준다.
      - (deviation = maxOddNumber - evenNumber) > (deviation = maxOddNumber - evenNumber//2)
  - do3() : reverse direction of do2().    all double until below maxOddNumber.   but it is not optimized. (TODO)
  - do4() : 4-1 is basic, but we should do more if we can get minimal deviation as we change 4-2 and 4-3
    - 4-1 : rearrange nums[0] and nums[-1] continuously if changed
    - 4-2 : try multiple changes apply above maxOddNumber to fold(//2)
      - maxOddNumber 보다 큰 수에 대해서 num[-1]부터 maxOddNumber까지 모든 수를 한개씩 효과가 있는지 본다. 
    - 4-3 : try multiple changes apply below maxOddNumber to double(*2)
      - maxOddNumber 보다 작은 수에 대해서 num[0]부터 maxOddNumber까지 모든 수를 한개씩 효과가 있는지 본다.
- knowledge
  - update and sort is faster than update-insert each elements
    - slow : remove() and bisect.insort()
    - fast : nums[]=? and sort()

# 24. Remove Covered Intervals (#1288)
- medium
- Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
  - The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d. 
  - Return the number of remaining intervals.
- https://leetcode.com/problems/remove-covered-intervals/
- [removeCoveredIntervals.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeCoveredIntervals.py) : passed
- knowledge (sort key)
  - https://realpython.com/python-sort/
  - https://www.programiz.com/python-programming/methods/built-in/sorted
  - runners.sort(key=lambda x: getattr(x, 'duration'))
  - ```python
    >>> words = ['banana', 'pie', 'Washington', 'book']
    >>> sorted(words, key=lambda x: x[::-1], reverse=True)
    ['Washington', 'book', 'pie', 'banana']

    >>> phrases = ['when in rome', 
    ...     'what goes around comes around', 
    ...     'all is fair in love and war'
    ...     ]
    >>> phrases.sort(key=lambda x: x.split()[2][1], reverse=True)
    >>> phrases
    ['what goes around comes around', 'when in rome', 'all is fair in love and war']

    >>> from collections import namedtuple
    >>> StudentFinal = namedtuple('StudentFinal', 'name grade')
    >>> bill = StudentFinal('Bill', 90)
    >>> patty = StudentFinal('Patty', 94)
    >>> bart = StudentFinal('Bart', 89)
    >>> students = [bill, patty, bart]
    >>> sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True)
    [StudentFinal(name='Patty', grade=94), StudentFinal(name='Bill', grade=90), StudentFinal(name='Bart', grade=89)]
    ```

# 25. All Divisions With the Highest Score of a Binary Array
- medium
- You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:
  - numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
    - If i == 0, numsleft is empty, while numsright has all the elements of nums.
    - If i == n, numsleft has all the elements of nums, while numsright is empty.
    - The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.
  - Return all distinct indices that have the highest possible division score. You may return the answer in any order.
- https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
- [maxScoreIndices.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxScoreIndices.py) : passed

# 26. Majority Element
- easy  , but hard with O(1) space
- Given an array nums of size n, return the majority element.
  - The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
- https://leetcode.com/problems/majority-element/
- [majorityElement.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/majorityElement.py) : passed
- [majorityElement2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/majorityElement2.py) : passed   O(1) space
  - converted as C : 
    - Runtime: 30 ms, faster than 41.77% of C online submissions for Majority Element.
    - Memory Usage: 7.5 MB, less than 99.35% of C online submissions for Majority Element.

# 27. The Skyline Problem (#218) - Hard
- hard : x 값이 어느 Boundary에 들어가는지를 가장 빨리 찾을수 있는 방법을 N 보다 작은 logN으로 찾아야 한다.
- A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
- https://leetcode.com/problems/the-skyline-problem/
- [getSkyline.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSkyline.py) : 39 / 40 test cases passed.     Status: Time Limit Exceeded
- [getSkyline4.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSkyline4.py) : passed  (205ms)
  - it takes very long time. 
- [getSkyline5.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSkyline5.py) : passed (remove unused codes)
  - Runtime: 158 ms, faster than 66.63% of Python3 online submissions for The Skyline Problem.
  - Memory Usage: 20 MB, less than 33.75% of Python3 online submissions for The Skyline Problem.

# 28. Clone Graph (#133)
- medium : TreeNode
- Given a reference of a node in a connected undirected graph. 
  - Return a deep copy (clone) of the graph.
- https://leetcode.com/problems/clone-graph/
- [cloneGraph.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/cloneGraph.py) : passed
  - only show ```def cloneGraph(self, node: 'Node') -> 'Node':```
  - 'Node' means class(Node)

# 29. Sort List (#148)
- medium : Linked Lists
- Given the head of a linked list, return the list after sorting it in ascending order.
  - Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
- https://leetcode.com/problems/sort-list/
- [sortList.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortList.py) : O(N^2) 24 / 28 test cases passed.  status: Time Limit Exceeded   len:9828  total_time : 47.36812353134155
- [sortList2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortList2.py) : O(NlogN)  passed

# 30. Compare Version Numbers (#165)
- medium 
- Given two version numbers, version1 and version2, compare them.
  - Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
  - To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
- https://leetcode.com/problems/compare-version-numbers/
- [compareVersion.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/compareVersion.py) : passed



