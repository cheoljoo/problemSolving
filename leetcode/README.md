- [1. knowledge](#1-knowledge)
  - [1.1. sort performance](#11-sort-performance)
  - [1.2. sort keys](#12-sort-keys)
  - [1.3. Euclidean-algorithm : 유클리드 호제법](#13-euclidean-algorithm--유클리드-호제법)
  - [1.4. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree](#14-height-balanced-binary-search-trees--avlcreatoradelson-velsky-and-landis-tree)
  - [1.5. hamming weight : number of '1' bits](#15-hamming-weight--number-of-1-bits)
  - [1.6. find (?,?) including A among [(x1,x2) , ....] if x1>x2](#16-find--including-a-among-x1x2---if-x1x2)
  - [1.7. two dimensional array initialize and set](#17-two-dimensional-array-initialize-and-set)
  - [1.8. regular expression (import re)](#18-regular-expression-import-re)
    - [1.8.1. difference between re.search() and re.match()](#181-difference-between-research-and-rematch)
  - [1.9. format string](#19-format-string)
- [2. Meidan of Two Sorted Arrays - hard](#2-meidan-of-two-sorted-arrays---hard)
- [3. Regular Expression Matching - hard](#3-regular-expression-matching---hard)
- [4. Strange Printer - hard](#4-strange-printer---hard)
- [5. Third Maximum Number - easy](#5-third-maximum-number---easy)
- [6. Find All Numbers Disappeared in an Array - medium](#6-find-all-numbers-disappeared-in-an-array---medium)
- [7. Squares of a Sorted Array - midium](#7-squares-of-a-sorted-array---midium)
- [8. Remove Duplicates from Sorted Array - easy](#8-remove-duplicates-from-sorted-array---easy)
- [9. Single Number - easy but hard](#9-single-number---easy-but-hard)
- [10. Plus One - easy](#10-plus-one---easy)
- [11. Remove Nth Node From End of List (Linked List) - easy](#11-remove-nth-node-from-end-of-list-linked-list---easy)
- [12. Convert Sorted Array to Binary Search Tree (Trees : Height-Balanced Binary Search Trees) - easy](#12-convert-sorted-array-to-binary-search-tree-trees--height-balanced-binary-search-trees---easy)
- [13. is Balanced Binary Tree - easy](#13-is-balanced-binary-tree---easy)
- [14. First Bad Version : Sorting and Searching - easy](#14-first-bad-version--sorting-and-searching---easy)
- [15. Maximum Subarray : DP - easy but hard](#15-maximum-subarray--dp---easy-but-hard)
- [16. Remove Outermost Parentheses (#1021) -easy](#16-remove-outermost-parentheses-1021--easy)
- [17. Zigzag Conversion (#6) - medium](#17-zigzag-conversion-6---medium)
- [18. House Robber (#198) - medium](#18-house-robber-198---medium)
- [19. Shuffle an Array (#384) - medium](#19-shuffle-an-array-384---medium)
- [20. Number of 1 Bits (#191) - easy](#20-number-of-1-bits-191---easy)
- [21. Hamming Distance (#461) - easy](#21-hamming-distance-461---easy)
- [22. Missing Number (#268) - easy](#22-missing-number-268---easy)
- [23. Minimize Deviation in Array (#1675)  -hard](#23-minimize-deviation-in-array-1675---hard)
- [24. Remove Covered Intervals (#1288) - medium](#24-remove-covered-intervals-1288---medium)
- [25. All Divisions With the Highest Score of a Binary Array - medium](#25-all-divisions-with-the-highest-score-of-a-binary-array---medium)
- [26. Majority Element - easy  , but hard with O(1) space](#26-majority-element---easy---but-hard-with-o1-space)
- [27. The Skyline Problem (#218) - hard](#27-the-skyline-problem-218---hard)
- [28. Clone Graph (#133) - medium](#28-clone-graph-133---medium)
- [29. Sort List (#148) - medium](#29-sort-list-148---medium)
- [30. Compare Version Numbers (#165) - medium](#30-compare-version-numbers-165---medium)
- [31. Count Array Pairs Divisible by K (#2183) - hard](#31-count-array-pairs-divisible-by-k-2183---hard)
- [32. Shortest Path Visiting All Nodes (#847) - hard](#32-shortest-path-visiting-all-nodes-847---hard)
- [33. Arithmetic Slices (#413) - medium](#33-arithmetic-slices-413---medium)
- [34. Champagne Tower (#799) - medium](#34-champagne-tower-799---medium)
- [35. Remove Duplicates from Sorted List II (#82) - medium](#35-remove-duplicates-from-sorted-list-ii-82---medium)
- [36. Count All Valid Pickup and Delivery Options (#1359) - hard](#36-count-all-valid-pickup-and-delivery-options-1359---hard)
- [37. Counting Bits (#338) - easy](#37-counting-bits-338---easy)
- [38. Rotate List (#61) - medium](#38-rotate-list-61---medium)
- [39. Copy List with Random Pointer (#138) - medium](#39-copy-list-with-random-pointer-138---medium)
- [40. Find All K-Distant Indices in an Array (#2200) - easy : weekly contest for amazon 2022-03-13](#40-find-all-k-distant-indices-in-an-array-2200---easy--weekly-contest-for-amazon-2022-03-13)
- [41. Count Artifacts That Can Be Extracted (#2201) - medium : weekly contest for amazon 2022-03-13](#41-count-artifacts-that-can-be-extracted-2201---medium--weekly-contest-for-amazon-2022-03-13)
- [42. Maximize the Topmost Element After K Moves (#2202) - medium : weekly contest for amazon 2022-03-13](#42-maximize-the-topmost-element-after-k-moves-2202---medium--weekly-contest-for-amazon-2022-03-13)
- [43. Minimum Weighted Subgraph With the Required Paths (#2203) - hard : weekly contest for amazon 2022-03-13 <fail>](#43-minimum-weighted-subgraph-with-the-required-paths-2203---hard--weekly-contest-for-amazon-2022-03-13-fail)
- [44. Simplify Path (#71) - medium](#44-simplify-path-71---medium)

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

## 1.6. find (?,?) including A among [(x1,x2) , ....] if x1>x2 
- 27. The Skyline Problem (#218) - Hard
- korean : [(x1,x2) , ....] 에서 A를 포함하는 것들을 구하시요.
- sort by x1 -> find x1 : 0 .. A .. x1 -> calulate
- if A is another sorted list [A1,A2...] , 0 .. A1 .. x1 and x2 A1 (sorted by x2) -> when we find pairs for A2 , we can skip until x2   

## 1.7. two dimensional array initialize and set
- ln = [[0] * 101] * (query_row+1)
  - ln[0][0]=2 then all row's [0] were changed into 2
- ln = [[0 for c in range(101)] for r in range(query_row+1)]
  - it is right solution to initialize two dimensional array
  - https://www.kite.com/python/answers/how-to-initialize-a-2d-array-in-python
  
## 1.8. regular expression (import re)
- https://www.programiz.com/python-programming/regex
- https://emilkwak.github.io/python-re-named-group
```python
  self.patternDate = re.compile('^\s*(?P<year>\d+)\/(?P<month>\d+)\/(?P<day>\d+)\s*$')
  self.patternTime = re.compile('^\s*(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\.(?P<microsec>\d+)\s*$')
  self.patternDateTime = re.compile('^\s*\[\s*(?P<year>\d+)\/(?P<month>\d+)\/(?P<day>\d+)\s+(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\.(?P<microsec>\d+)\s*\]\s*')

  result = self.patternDateTime.match(self.msg)
  if result:
    "%02d/%02d/%02d"%(int(result.group('year')),int(result.group('month')),int(result.group('day')))
    self.msg = self.patternDateTime.sub('',self.msg)
```
- (?......) 
  - https://docs.python.org/3/howto/regex.html
  - The solution chosen by the Perl developers was to use (?...) as the extension syntax. ? immediately after a parenthesis was a syntax error because the ? would have nothing to repeat, so this didn’t introduce any compatibility problems. The characters immediately after the ? indicate what extension is being used, so (?=foo) is one thing (a positive lookahead assertion) and (?:foo) is something else (a non-capturing group containing the subexpression foo).
  - The syntax for a named group is one of the Python-specific extensions: (?P<name>...).
  - This is another Python extension: (?P=name) indicates that the contents of the group called name should again be matched at the current point. The regular expression for finding doubled words, \b(\w+)\s+\1\b can also be written as \b(?P<word>\w+)\s+(?P=word)\b:
  - (?=...)
    - Positive lookahead assertion. This succeeds if the contained regular expression, represented here by ..., successfully matches at the current location, and fails otherwise. But, once the contained expression has been tried, the matching engine doesn’t advance at all; the rest of the pattern is tried right where the assertion started.
  - (?!...)
    - Negative lookahead assertion. This is the opposite of the positive assertion; it succeeds if the contained expression doesn’t match at the current position in the string.
```pythonpat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)
```

### 1.8.1. difference between re.search() and re.match()
- https://www.geeksforgeeks.org/python-re-search-vs-re-match/
- re.match() searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none.

## 1.9. format string
- https://hyjykelly.tistory.com/65
- performance comparison : https://brownbears.tistory.com/421

# 2. Meidan of Two Sorted Arrays - hard
- hard
- https://leetcode.com/problems/median-of-two-sorted-arrays/
- [findMedianSortedArrays2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findMedianSortedArrays2.py) : passed
- ex
  - [][] , [2][] , [][2] , [2][2] , [2][1,3,4] 

# 3. Regular Expression Matching - hard
- hard
- https://leetcode.com/problems/regular-expression-matching/
- [isMatch.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch.py) : wrong answer
- [isMatch_dfs.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch_dfs.py) : time limit exceeded : 38 / 353 test cases passed.
- [isMatch.c](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch.c) : Code in site : time limit exceeded : 353 / 353 test cases passed, but took too long.
- [isMatch2.c](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isMatch2.c) : passed
  - change call order : longest match is first.   -> passed
  - ```
      return go(s,sIndex+1,patternIndex+1,loopLevel+1) || go(s,sIndex+1,patternIndex,loopLevel+1) || go(s,sIndex,patternIndex+1,loopLevel+1)  ;
    ``` 

# 4. Strange Printer - hard
- hard : DP dynamic programming
- https://leetcode.com/problems/strange-printer/
- get the code and hint from discussion
- [strangePrinter.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/strangePrinter.py) : passed

# 5. Third Maximum Number - easy
- easy
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
- [thirdMaximumNumber.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/thirdMaximumNumber.py) : passed

# 6. Find All Numbers Disappeared in an Array - medium
- medium : O(N)
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
- [findDisappearedNumbers.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findDisappearedNumbers.py) : passed

# 7. Squares of a Sorted Array - midium
- medium : O(N)
- Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
- https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
- [sortedSquares.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortedSquares.py) : passed

# 8. Remove Duplicates from Sorted Array - easy
- easy : Array
- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
- [removeDuplicates.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeDuplicates.py) : passed 
  - we should add empty lists to the
  - if len(nums) == 0 : return 0

# 9. Single Number - easy but hard
- easy or hard : Arrays
- Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
- [singleNumber.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/singleNumber.py) : passed 
  - O(N)
  - but , i used the dictionay with size of array.   is it a constant extra space? (NO)

# 10. Plus One - easy
- easy : Array
- You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
  - Increment the large integer by one and return the resulting array of digits.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
- [plusOne.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/plusOne.py) : passed

# 11. Remove Nth Node From End of List (Linked List) - easy
- easy : Linked List
- Given the head of a linked list, remove the nth node from the end of the list and return its head.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
- [removeNthFromEnd.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeNthFromEnd.py) : passed

# 12. Convert Sorted Array to Binary Search Tree (Trees : Height-Balanced Binary Search Trees) - easy
- easy : Trees , but it is not AVL.
- Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree : https://www.programiz.com/dsa/avl-tree
  - [avl.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/avl.py)
- Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
  - A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
- [sortedArrayToBST.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortedArrayToBST.py) : passed

# 13. is Balanced Binary Tree - easy
- easy : Trees
- Given a binary tree, determine if it is height-balanced.
- For this problem, a height-balanced binary tree is defined as:
- a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
- https://leetcode.com/problems/balanced-binary-tree/
- [isBalanced2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isBalanced2.py) : passed
  - [isBalanced.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isBalanced.py) : running is ok. but it has warning in vsc.

# 14. First Bad Version : Sorting and Searching - easy
- easy : Sorting and Searching
- You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
- Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
- You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
- At first time I try to find sequentially.  but time exceeded.
- [firstBadVersion.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/firstBadVersion.py) : passed

# 15. Maximum Subarray : DP - easy but hard
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

# 16. Remove Outermost Parentheses (#1021) -easy
- easy : 
- Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
- Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
- https://leetcode.com/problems/remove-outermost-parentheses/
- [removeOuterParentheses.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeOuterParentheses.py) : passed

# 17. Zigzag Conversion (#6) - medium
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

# 18. House Robber (#198) - medium
- medium
- You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
- Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/    https://leetcode.com/problems/house-robber/
- [rob.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/rob.py) : passed

# 19. Shuffle an Array (#384) - medium
- medium : 판정 기준이 애매함.
- Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/    https://leetcode.com/problems/shuffle-an-array/
- passed

# 20. Number of 1 Bits (#191) - easy
- easy : hamming weight 
- Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://shumin.co.kr/algorithm-hamming-weight-bit-count/)).
- https://leetcode.com/problems/number-of-1-bits/ 
- passed : C (unsigned int) , python3 (int) 

- 8 bit : 1. shift 8  2. table
- 32bit : 1. shift 32 2. hamming weight-1 (4 operation * 5(1,2,4,8,16))  3. hamming weight-2 (4 operation * count) if count <= 5

# 21. Hamming Distance (#461) - easy
- easy : hamming distance / hamming weight (number of 1 bits)
```
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
```
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/     https://leetcode.com/problems/hamming-distance/
- [hammingDistance.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/hammingDistance.py) : passed

# 22. Missing Number (#268) - easy
- easy : jongkyung.byun teaches me. len() * (len() +1) / 2 is total sum.  so your missing number = total sum - input sum
- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
- https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/    https://leetcode.com/problems/missing-number/
- [missingNumber.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/missingNumber.py) : passed

# 23. Minimize Deviation in Array (#1675)  -hard
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

# 24. Remove Covered Intervals (#1288) - medium
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

# 25. All Divisions With the Highest Score of a Binary Array - medium
- medium
- You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:
  - numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
    - If i == 0, numsleft is empty, while numsright has all the elements of nums.
    - If i == n, numsleft has all the elements of nums, while numsright is empty.
    - The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.
  - Return all distinct indices that have the highest possible division score. You may return the answer in any order.
- https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
- [maxScoreIndices.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxScoreIndices.py) : passed

# 26. Majority Element - easy  , but hard with O(1) space
- easy  , but hard with O(1) space
- Given an array nums of size n, return the majority element.
  - The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
- https://leetcode.com/problems/majority-element/
- [majorityElement.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/majorityElement.py) : passed
- [majorityElement2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/majorityElement2.py) : passed   O(1) space
  - converted as C : 
    - Runtime: 30 ms, faster than 41.77% of C online submissions for Majority Element.
    - Memory Usage: 7.5 MB, less than 99.35% of C online submissions for Majority Element.

# 27. The Skyline Problem (#218) - hard
- hard : x 값이 어느 Boundary에 들어가는지를 가장 빨리 찾을수 있는 방법을 N 보다 작은 logN으로 찾아야 한다.
- A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
- https://leetcode.com/problems/the-skyline-problem/
- [getSkyline.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSkyline.py) : 39 / 40 test cases passed.     Status: Time Limit Exceeded
- [getSkyline4.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSkyline4.py) : passed  (205ms)
  - it takes very long time. 
- [getSkyline5.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSkyline5.py) : passed (remove unused codes)
  - down lines : answer is second max in DownList. DownList is all heights for x (many lines go through this number of x)
  - Runtime: 158 ms, faster than 66.63% of Python3 online submissions for The Skyline Problem.
  - Memory Usage: 20 MB, less than 33.75% of Python3 online submissions for The Skyline Problem.

# 28. Clone Graph (#133) - medium
- medium : TreeNode
- Given a reference of a node in a connected undirected graph. 
  - Return a deep copy (clone) of the graph.
- https://leetcode.com/problems/clone-graph/
- [cloneGraph.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/cloneGraph.py) : passed
  - only show ```def cloneGraph(self, node: 'Node') -> 'Node':```
  - 'Node' means class(Node)

# 29. Sort List (#148) - medium
- medium : Linked Lists
- Given the head of a linked list, return the list after sorting it in ascending order.
  - Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
- https://leetcode.com/problems/sort-list/
- [sortList.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortList.py) : O(N^2) 24 / 28 test cases passed.  status: Time Limit Exceeded   len:9828  total_time : 47.36812353134155
- [sortList2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortList2.py) : O(NlogN)  passed

# 30. Compare Version Numbers (#165) - medium
- medium 
- Given two version numbers, version1 and version2, compare them.
  - Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
  - To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
- https://leetcode.com/problems/compare-version-numbers/
- [compareVersion.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/compareVersion.py) : passed

# 31. Count Array Pairs Divisible by K (#2183) - hard
- hard
- Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:
  - 0 <= i < j <= n - 1 and 
  - nums[i] * nums[j] is divisible by k.
- https://leetcode.com/problems/count-array-pairs-divisible-by-k/
- [countPairs.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countPairs.py) : 92 / 115 test cases passed. Status: Time Limit Exceeded
- [countPairs2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countPairs2.py) : Time Limit Exceeded
  - check memory profiler  with @profiler  : this memory profile gives the running count of each line.
- [countPairs3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countPairs3.py) : passed
  - remove loop with prior calculation. (klist)
  - Runtime: 6060 ms, faster than 5.01% of Python3 online submissions for Count Array Pairs Divisible by K.
  - Memory Usage: 255.4 MB, less than 5.02% of Python3 online submissions for Count Array Pairs Divisible by K.
```python
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    30     24.4 MiB     24.4 MiB           1       @profile
    31                                             def countPairs(self, nums: List[int], k: int) -> int:
    32                                                 # k 소인수분해로 그 조합
    33                                                 # k = 8
    34     24.4 MiB      0.0 MiB           1           if timeFlag : start = time.time()
    35     24.4 MiB      0.0 MiB           1           nums.sort()
    36     24.4 MiB      0.0 MiB           1           if timeFlag : print(" nums.sort(%d):"%len(nums), time.time() - start , "-> ", end="")
    37     24.4 MiB      0.0 MiB           1           if timeFlag : start = time.time()
    38     24.4 MiB      0.0 MiB           1           d = k
    39     24.4 MiB      0.0 MiB           1           i = 1
    40                                                 # self.k.append(k)
    41     24.4 MiB      0.0 MiB         236           while i*i <= k :
    42     24.4 MiB      0.0 MiB         235               if d % i == 0 :
    43     24.4 MiB      0.0 MiB           6                   self.k.append(i)
    44     24.4 MiB      0.0 MiB           6                   t = d//i
    45     24.4 MiB      0.0 MiB           6                   if t != i : self.k.append(t)
    46     24.4 MiB      0.0 MiB         235               i += 1
    47     24.4 MiB      0.0 MiB           1           self.k.sort()
    48     24.4 MiB      0.0 MiB           1           if debugFlag : print("key:",self.k)
    49     24.4 MiB      0.0 MiB           1           if timeFlag : print(" k.sort(%d):"%len(self.k), time.time() - start , "-> ", end="")
    50     24.4 MiB      0.0 MiB           1           if timeFlag : start = time.time()
    51     24.4 MiB      0.0 MiB           1           kMultiple = 0
    52     24.4 MiB      0.0 MiB           1           divid0 = []
    53     24.4 MiB      0.0 MiB        1681           for t in reversed(nums) :
    54     24.4 MiB      0.0 MiB        1680               if t % k == 0 :
    55                                                         kMultiple += 1
    56     24.4 MiB      0.0 MiB        1680               divid0.append(kMultiple)
    57     24.4 MiB      0.0 MiB           1           divid0.reverse()
    58     24.4 MiB      0.0 MiB           1           if debugFlag : print("nums:",nums)
    59     24.4 MiB      0.0 MiB           1           if debugFlag : print("divid0:",divid0)
    60     24.4 MiB      0.0 MiB           1           if timeFlag : print(" multiple(%d):"%len(nums), time.time() - start , "-> ", end="")
    61     24.4 MiB      0.0 MiB           1           if timeFlag : start = time.time()
    62     24.4 MiB      0.0 MiB           1           r = []
    63     24.7 MiB      0.0 MiB        1681           for i in nums:
    64                                                     # n = set()
    65     24.7 MiB      0.1 MiB        1680               n = []
    66     24.7 MiB      0.0 MiB        1680               if i == 1 :
    67                                                         r.append([i,n])
    68                                                         continue
    69     24.7 MiB      0.0 MiB       21840               for d in self.k:
    70     24.7 MiB      0.0 MiB       20160                   if d == 1:
    71     24.7 MiB      0.0 MiB        1680                       continue
    72     24.7 MiB      0.0 MiB       18480                   if i % d == 0:
    73                                                             # n.add(d)
    74     24.7 MiB      0.0 MiB        1028                       n.append(d)
    75     24.7 MiB      0.1 MiB        1680               r.append([i,n])
    76     24.7 MiB      0.0 MiB           1           if debugFlag : print("result:",r)
    77     24.7 MiB      0.0 MiB           1           if timeFlag : print(" result(%d):"%len(r), time.time() - start , "-> ", end="")
    78     24.7 MiB      0.0 MiB           1           if timeFlag : start = time.time()
    79
    80     24.7 MiB      0.0 MiB           1           count = 0
    81                                                 # if nums[0] == 1 :
    82                                                 #     count += divid0[0]
    83                                                 # print("count:",count)
    84     24.7 MiB    -16.6 MiB        1681           for (idx,v) in enumerate(r):
    85     24.7 MiB    -16.6 MiB        1680               if v[0] % k == 0 :
    86                                                         count += len(r) - (idx+1)
    87                                                         if debugFlag : print("idx:",idx, "CASE:v[0]%k==0" , "v[0]:",v[0],"v[1]:",v[1],"count:",count)
    88     24.7 MiB    -16.6 MiB        1680               elif len(v[1]) == 0 :
    89     24.7 MiB    -10.1 MiB        1007                   count += divid0[idx]
    90     24.7 MiB    -10.1 MiB        1007                   if debugFlag : print("idx:",idx, "CASE:len(v[1])==0","v[0]:",v[0],"v[1]:",v[1],"count:",count )
    91                                                     else :
    92     24.7 MiB     -6.5 MiB         673                   if len(v[1]) > 0 :
    93                                                             # d != 1 :
    94     24.7 MiB     -6.5 MiB         673                       d = v[1][-1]
    95     24.7 MiB     -6.5 MiB         673                       another = k // d
    96     24.7 MiB  -3420.0 MiB      567078                       for t in range(idx+1,len(r)) :
    97     24.7 MiB  -3413.5 MiB      566405                           if another in r[t][1] :
    98     24.7 MiB     -0.4 MiB          72                               count += 1
    99     24.7 MiB     -0.4 MiB          72                               if debugFlag : print("idx:",idx,"t:",t,"d:",d,"another:",another,"r[%d]"%t,r[t],"r[%d][1]"%t,r[t][1],"pair:",v[0],r[t][0],"count:",count)
   100     24.7 MiB     -0.0 MiB           1           if timeFlag : print(" getr(%d):"%len(r), time.time() - start , "-> ", end="")
   101
   102     24.7 MiB      0.0 MiB           1           return count


 len : 1680 , total_time : 52.50429153442383 -> ERROR(0) -> 72 => k:55503  keys: [1, 3, 7, 9, 21, 63, 881, 2643, 6167, 7929, 18501, 55503]
```
- discussion (reference)
  - https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1785027/C%2B%2BPython-Easy-and-Concise-with-Explanation
  - https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1784712/Python-O(Nsqrt(K))-Easy-understand-solution

# 32. Shortest Path Visiting All Nodes (#847) - hard
- hard
- You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
  - Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
- https://leetcode.com/problems/shortest-path-visiting-all-nodes/
- [shortestPathLength.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathLength.py) : 46 / 51 test cases passed. Status: Time Limit Exceeded
- [shortestPathLength2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathLength2.py) : 34seconds  47 / 51 test cases passed. Status: Time Limit Exceeded
- [shortestPathLength3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathLength3.py) : dp (node1-> node2,mask) = value 51 seconds Time Limit Exceeded
- [shortestPathLength4.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathLength4.py) : dp (node,mask) = value 25 seconds  Time Limit Exceeded
- [shortestPathLength4-bfs.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathLength4-bfs.py) : passed - BFS (371 ms in site)
- DFS can show the path. but BFS can not show path.

# 33. Arithmetic Slices (#413) - medium
- medium
- An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
  - For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
  - Given an integer array nums, return the number of arithmetic subarrays of nums.
  - A subarray is a contiguous subsequence of the array.
- https://leetcode.com/problems/arithmetic-slices/
- [numberOfArithmeticSlices.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/numberOfArithmeticSlices.py) : passed
- Time: O(n)  Space: O(n) for cache : https://leetcode.com/problems/arithmetic-slices/discuss/1814595/Python3-CACHE-()-Explained

# 34. Champagne Tower (#799) - medium
- medium
- We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
  - Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
  - For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
  - Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)
- https://leetcode.com/problems/champagne-tower/
- [champagneTower.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/champagneTower.py) : passed
  - first of all , poured all basket in ln[0][0] then we calculate flowed water.
- algorithm
```
f(L,n) = ( f(L-1,n-1) + f(L-1,n) ) / 2   
f(0,0) = 1
f(L,0) = f(L,L) = 1 / 2**L


f(1,0) = 1/2  , f(1,1) = 1/2
f(2,0) = 1/4 , f(2,1) = (f(1,0)+f(1,1))/2 = 2/4
f(3,0) = 1/8 , f(3,1) = (f(2,0)+f(2,1))/2 = 3/8

we can calulate with only integer.  
we can predict that denominator is 2**L with Level L.

(L=33,n=17) = 32,16 and 32,17 should be full. 
```


# 35. Remove Duplicates from Sorted List II (#82) - medium
- medium : C++
- Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
- [deleteDuplicates.cpp](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/deleteDuplicates.cpp) : passed

# 36. Count All Valid Pickup and Delivery Options (#1359) - hard
- hard
- Given n orders, each order consist in pickup and delivery services. 
  - Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
  - Since the answer may be too large, return it modulo 10^9 + 7.
  - Explanation: All possible orders: 
    - (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
    - This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
- [countOrders.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countOrders.py) : passed

# 37. Counting Bits (#338) - easy
- easy
- Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
- Follow up:
  - It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
  - Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
- https://leetcode.com/problems/counting-bits/
- [countBits.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countBits.py) : passed     http://shumin.co.kr/algorithm-hamming-weight-bit-count/
  - class Solution : Hamming Weight -> 141 ms 20.9 MB
    - Your runtime beats 42.19 % of python3 submissions
  - class Sol2 :  Dynamic Programming   ->  76 ms   20.9 MB
    - Runtime: 76 ms, faster than 97.48% of Python3 online submissions for Counting Bits.
    - Memory Usage: 20.9 MB, less than 38.89% of Python3 online submissions for Counting Bits.

# 38. Rotate List (#61) - medium
- medium
- Given the head of a linked list, rotate the list to the right by k places.
- https://leetcode.com/problems/rotate-list/
- [rotateRight.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/rotateRight.py) : passed
  - Runtime: 40 ms, faster than 84.61% of Python3 online submissions for Rotate List.
  - Memory Usage: 13.9 MB, less than 88.66% of Python3 online submissions for Rotate List.

# 39. Copy List with Random Pointer (#138) - medium
- medium
- A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
  - Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
  - For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
  - Return the head of the copied linked list.
  - The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
  - Your code will only be given the head of the original linked list.
- https://leetcode.com/problems/copy-list-with-random-pointer/
- [copyRandomList.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/copyRandomList.py) : passed
  - Runtime: 56 ms, faster than 42.66% of Python3 online submissions for Copy List with Random Pointer.
  - Memory Usage: 14.9 MB, less than 55.97% of Python3 online submissions for Copy List with Random Pointer.
- O(1) space : [copyRandomList-O1.cpp](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/copyRandomList-O1.cpp)
  
# 40. Find All K-Distant Indices in an Array (#2200) - easy : weekly contest for amazon 2022-03-13
- easy
- You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
  - Return a list of all k-distant indices sorted in increasing order.
- https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
- [findKDistantIndices.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findKDistantIndices.py) : passed

# 41. Count Artifacts That Can Be Extracted (#2201) - medium : weekly contest for amazon 2022-03-13
- medium
- There is an n x n 0-indexed grid with some artifacts buried in it. You are given the integer n and a 0-indexed 2D integer array artifacts describing the positions of the rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith artifact is buried in the subgrid where:
  - (r1i, c1i) is the coordinate of the top-left cell of the ith artifact and (r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
  - You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.
  - Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will excavate the cell (ri, ci), return the number of artifacts that you can extract.
- https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
- [digArtifacts.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/digArtifacts.py) : passed

# 42. Maximize the Topmost Element After K Moves (#2202) - medium : weekly contest for amazon 2022-03-13
- medium : I didn't understand what measn until now. I saw the following article before solving this problem.
  - https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/discuss/1844542/Python-or-O(1)-space-O(1)-Time-or-Explanation-or-Comments-added
    - ![picture_explanation](https://assets.leetcode.com/users/images/63265d6c-7a19-4278-b73d-46f0999e47d8_1647147723.9620347.jpeg)
  - https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/discuss/1844225/Python-Solution-by-Analyzing-All-Cases.
- You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.
  - In one move, you can perform either of the following:
    - If the pile is not empty, remove the topmost element of the pile.
    - If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
  - You are also given an integer k, which denotes the total number of moves to be made.
  - Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.
- https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
- [maximumTop.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumTop.py) : passed

# 43. Minimum Weighted Subgraph With the Required Paths (#2203) - hard : weekly contest for amazon 2022-03-13 <fail>
- hard : I did not solve this probelm within contest. I can not try it because i can not understand the meaning of #2202.
- You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.
  - You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.
  - Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.
  - Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.
- https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
- algorithm : dest -> src1 , dest -> src2
- [minimumWeight.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumWeight.py) :  

# 44. Simplify Path (#71) - medium
- medium
- Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
  - In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
  - The canonical path should have the following format:
    - The path starts with a single slash '/'.
    - Any two directories are separated by a single slash '/'.
    - The path does not end with a trailing '/'.
    - The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
  - Return the simplified canonical path.
- https://leetcode.com/problems/simplify-path/
- [simplifyPath.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/simplifyPath.py) : passed







