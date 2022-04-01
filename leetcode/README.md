- [1. knowledge](#1-knowledge)
  - [1.1. sort performance](#11-sort-performance)
  - [1.2. sort keys](#12-sort-keys)
  - [1.3. sorted data structure](#13-sorted-data-structure)
    - [1.3.1. bisect](#131-bisect)
    - [1.3.2. heapq](#132-heapq)
    - [1.3.3. PriorityQueue](#133-priorityqueue)
    - [1.3.4. sortedcontainers](#134-sortedcontainers)
  - [1.4. Euclidean-algorithm : 유클리드 호제법](#14-euclidean-algorithm--유클리드-호제법)
  - [1.5. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree](#15-height-balanced-binary-search-trees--avlcreatoradelson-velsky-and-landis-tree)
  - [1.6. hamming weight : number of '1' bits](#16-hamming-weight--number-of-1-bits)
  - [1.7. find (?,?) including A among [(x1,x2) , ....] if x1>x2](#17-find--including-a-among-x1x2---if-x1x2)
  - [1.8. two dimensional array initialize and set](#18-two-dimensional-array-initialize-and-set)
  - [1.9. regular expression (import re)](#19-regular-expression-import-re)
    - [1.9.1. difference between re.search() and re.match()](#191-difference-between-research-and-rematch)
  - [1.10. format string](#110-format-string)
  - [1.11. lexicographiacll order](#111-lexicographiacll-order)
  - [1.12. dictionary : Python Remove Key from a Dictionary: A Complete Guide](#112-dictionary--python-remove-key-from-a-dictionary-a-complete-guide)
  - [1.13. list : python remove element from a list](#113-list--python-remove-element-from-a-list)
  - [1.14. Books & URL](#114-books--url)
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
- [42. Maximize the Topmost Element After K Moves (#2202) - medium : weekly contest for amazon 2022-03-13 / <got help>](#42-maximize-the-topmost-element-after-k-moves-2202---medium--weekly-contest-for-amazon-2022-03-13--got-help)
- [43. Minimum Weighted Subgraph With the Required Paths (#2203) - hard : weekly contest for amazon 2022-03-13 <fail>](#43-minimum-weighted-subgraph-with-the-required-paths-2203---hard--weekly-contest-for-amazon-2022-03-13-fail)
- [44. Simplify Path (#71) - medium](#44-simplify-path-71---medium)
- [45. Minimum Remove to Make Valid Parentheses ($1249) - medium](#45-minimum-remove-to-make-valid-parentheses-1249---medium)
- [46. Validate Stack Sequences (#946) - medium / python / rust](#46-validate-stack-sequences-946---medium--python--rust)
- [47. Score of Parentheses (#856) - medium : / python](#47-score-of-parentheses-856---medium---python)
- [48. Remove Duplicate Letters (#316) (#1081) - medium : [python]](#48-remove-duplicate-letters-316-1081---medium--python)
- [49. Maximum Frequency Stack (#895) - hard : / python](#49-maximum-frequency-stack-895---hard---python)
- [50. Minimum Domino Rotations For Equal Row (#1007) - medium / python](#50-minimum-domino-rotations-for-equal-row-1007---medium--python)
- [51. Count Collisions on a Road (#2211) - medium / python : 2020-03-20 Weekly Contest 285](#51-count-collisions-on-a-road-2211---medium--python--2020-03-20-weekly-contest-285)
- [52. Maximum Points in an Archery Competition (#2212) - medium / python : 2020-03-20 Weekly Contest 285 (3H)](#52-maximum-points-in-an-archery-competition-2212---medium--python--2020-03-20-weekly-contest-285-3h)
- [53. Longest Substring of One Repeating Character (#2213) - hard : 2020-03-20 Weekly Contest 285  <fail>](#53-longest-substring-of-one-repeating-character-2213---hard--2020-03-20-weekly-contest-285--fail)
- [54. Partition Labels (#763) - medium / python / 2H](#54-partition-labels-763---medium--python--2h)
- [55. Smallest String With A Given Numeric Value (#1663) - medium / python / 2H](#55-smallest-string-with-a-given-numeric-value-1663---medium--python--2h)
- [56. Broken Calculator (#991) - medium / python / 3H](#56-broken-calculator-991---medium--python--3h)
- [57. Boats to Save People (#881) - medium / python / 1H](#57-boats-to-save-people-881---medium--python--1h)
- [58. Two City Scheduling (#1029) - medium / python / 1H](#58-two-city-scheduling-1029---medium--python--1h)
- [59. Minimum Operations to Halve Array Sum (#2208) - medium / python / <got help>](#59-minimum-operations-to-halve-array-sum-2208---medium--python--got-help)
- [60. Maximize Number of Subsequences in a String (#2207) - medium / python / 1H](#60-maximize-number-of-subsequences-in-a-string-2207---medium--python--1h)
- [61. Search in Rotated Sorted Array (#33) - medium / python / 2H](#61-search-in-rotated-sorted-array-33---medium--python--2h)
- [62. Search in Rotated Sorted Array II (#81) - medium / python / 2D](#62-search-in-rotated-sorted-array-ii-81---medium--python--2d)

--------------------
leetcode : my introduction https://leetcode.com/cheoljoo/
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

## 1.3. sorted data structure
### 1.3.1. bisect
- import bisect
- bisect.insort()

### 1.3.2. heapq
- sorted data structure : [0] is the smallest number
  - https://www.daleseo.com/python-heapq/
    - import heapq  
    - heapq.heappush(list,value) heapq.heappop(list)   
    - list[0] is minimal value.   
    - if you want to maximum value , * -1.0 

### 1.3.3. PriorityQueue
- priority Queue (sorted with priority order)
  - https://www.daleseo.com/python-priority-queue/
    - from queue import PriorityQueue
    - put()
    - get()

### 1.3.4. sortedcontainers
- SortedList
- SortedDict
- SortedSet
- URL
  - https://pythonlang.dev/repo/grantjenks-python-sortedcontainers/ 
  - https://grantjenks.com/docs/sortedcontainers/

## 1.4. Euclidean-algorithm : 유클리드 호제법
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

## 1.5. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree
- https://www.programiz.com/dsa/avl-tree
- [avl.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/avl.py)

## 1.6. hamming weight : number of '1' bits
- Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://shumin.co.kr/algorithm-hamming-weight-bit-count/)).

## 1.7. find (?,?) including A among [(x1,x2) , ....] if x1>x2 
- 27. The Skyline Problem (#218) - Hard
- korean : [(x1,x2) , ....] 에서 A를 포함하는 것들을 구하시요.
- sort by x1 -> find x1 : 0 .. A .. x1 -> calulate
- if A is another sorted list [A1,A2...] , 0 .. A1 .. x1 and x2 A1 (sorted by x2) -> when we find pairs for A2 , we can skip until x2   

## 1.8. two dimensional array initialize and set
- ln = [[0] * 101] * (query_row+1)
  - ln[0][0]=2 then all row's [0] were changed into 2
- ln = [[0 for c in range(101)] for r in range(query_row+1)]
  - it is right solution to initialize two dimensional array
  - https://www.kite.com/python/answers/how-to-initialize-a-2d-array-in-python
  
## 1.9. regular expression (import re)
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

### 1.9.1. difference between re.search() and re.match()
- https://www.geeksforgeeks.org/python-re-search-vs-re-match/
- re.match() searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none.

## 1.10. format string
- https://hyjykelly.tistory.com/65
- performance comparison : https://brownbears.tistory.com/421

## 1.11. lexicographiacll order
- alphaveticall order except we can not find this character  ex) cb  -> cb  ,  cbc -> bc
- https://leetcode.com/problems/remove-duplicate-letters/submissions/

## 1.12. dictionary : Python Remove Key from a Dictionary: A Complete Guide
- dictionary.pop(key_to_remove, not_found)
  - https://careerkarma.com/blog/python-remove-key-from-a-dictionary/#:~:text=To%20remove%20a%20key%20from,item%20after%20the%20del%20keyword.

## 1.13. list : python remove element from a list 
- thislist.remove("banana")
- thislist.pop(1)
- del thislist[0]
- thislist.clear()
  - https://www.w3schools.com/python/python_lists_remove.asp
## 1.14. Books & URL
- Python module of the week : http://pymotw.com/2/PyMOTW-1.133.pdf
- RealPython : http://www.realpython.org
- 
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

# 42. Maximize the Topmost Element After K Moves (#2202) - medium : weekly contest for amazon 2022-03-13 / <got help>
- medium : <got help> I didn't understand what measn until now. I saw the following article before solving this problem.
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

# 45. Minimum Remove to Make Valid Parentheses ($1249) - medium
- medium
- Given a string s of '(' , ')' and lowercase English characters.
  - Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
  - Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.
- https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
- [minRemoveToMakeValid.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minRemoveToMakeValid.py) : passed

# 46. Validate Stack Sequences (#946) - medium / python / rust
- medium
- Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
- https://leetcode.com/problems/validate-stack-sequences/
- [validateStackSequences.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/validateStackSequences.py) : passed
  - Runtime: 84 ms, faster than 73.30% of Python3 online submissions for Validate Stack Sequences.
  - Memory Usage: 14.2 MB, less than 63.80% of Python3 online submissions for Validate Stack Sequences.
- [validateStackSequences.rs](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/validateStackSequences.rs) : passed
  - Runtime: 0 ms, faster than 100.00% of Rust online submissions for Validate Stack Sequences.
  - Memory Usage: 2.2 MB, less than 33.33% of Rust online submissions for Validate Stack Sequences.

# 47. Score of Parentheses (#856) - medium : / python
- medium
- Given a balanced parentheses string s, return the score of the string.
  - The score of a balanced parentheses string is based on the following rule:
    - "()" has score 1.
    - AB has score A + B, where A and B are balanced parentheses strings.
    - (A) has score 2 * A, where A is a balanced parentheses string.
- https://leetcode.com/problems/score-of-parentheses/
- [scoreOfParentheses.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/scoreOfParentheses.py) : passed
  - Runtime: 28 ms, faster than 94.45% of Python3 online submissions for Score of Parentheses.
  - Memory Usage: 14 MB, less than 30.17% of Python3 online submissions for Score of Parentheses.

# 48. Remove Duplicate Letters (#316) (#1081) - medium : [python]
- medium : i need to understand lexicographiacll (alphaveticall) order
  - alphaveticall order except we can not find this character  ex) cb  -> cb  ,  cbc -> bc
- Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
- Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
- https://leetcode.com/problems/remove-duplicate-letters/
- https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
- [removeDuplicateLetters.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeDuplicateLetters.py) : passed
  - Runtime: 56 ms, faster than 48.34% of Python3 online submissions for Remove Duplicate Letters.
  - Memory Usage: 14 MB, less than 54.66% of Python3 online submissions for Remove Duplicate Letters.

# 49. Maximum Frequency Stack (#895) - hard : / python
- hard
- Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
  - Implement the FreqStack class:
    - FreqStack() constructs an empty frequency stack.
    - void push(int val) pushes an integer val onto the top of the stack.
    - int pop() removes and returns the most frequent element in the stack.
      - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
- https://leetcode.com/problems/maximum-frequency-stack/
- [FreqStack.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/FreqStack.py) : 36/37 timeout   Dictionary  
- [FreqStack2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/FreqStack2.py) : passed    List
  - Runtime: 9880 ms, faster than 5.04% of Python3 online submissions for Maximum Frequency Stack.
  - Memory Usage: 22.4 MB, less than 85.58% of Python3 online submissions for Maximum Frequency Stack.
- [FreqStack3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/FreqStack3.py) : passed  basic Llist , but dictionary is faster than list for finding whether it is in or not. 
  - Runtime: 9039 ms, faster than 5.04% of Python3 online submissions for Maximum Frequency Stack.
  - Memory Usage: 22.8 MB, less than 35.18% of Python3 online submissions for Maximum Frequency Stack.
- - [FreqStack4-BestSolution.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/FreqStack4-BestSolution.py)  : ***if i have the counter for each value , we can get top level instantly.  and we should use dictionary to run fast.*** 
- algorithm : what is faster find and push and pop between dictionary and list? 
  - [Faster Lookups In Python. Comparison of dictionaries and lists : The fastest way to repeatedly lookup data with millions of entries in Python is using dictionaries.](https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38)
```cpp
  freqStack.push(5); // The stack is [5]
    stack[0] = {5}
  freqStack.push(7); // The stack is [5,7]
      stack[0] = {5,7}   7 is recent 
  freqStack.push(5); // The stack is [5,7,5]
      stack[1] = {5}
      stack[0] = {5,7}
  freqStack.push(7); // The stack is [5,7,5,7]
      stack[1] = {5,7}
      stack[0] = {5,7}
  freqStack.push(4); // The stack is [5,7,5,7,4]
      stack[1] = {5,7}
      stack[0] = {5,7,4}
  freqStack.push(5); // The stack is [5,7,5,7,4,5]
      stack[2] = {5}     <- top stack level
      stack[1] = {5,7}
      stack[0] = {5,7,4}
  freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
      stack[2] = {}
      stack[1] = {5,7}   <- top stack level
      stack[0] = {5,7,4}
  freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
      stack[2] = {}
      stack[1] = {5}   <- top stack level
      stack[0] = {5,7,4}
  freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
  freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
```

# 50. Minimum Domino Rotations For Equal Row (#1007) - medium / python
- medium
- In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
  - We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
  - Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
  - If it cannot be done, return -1.
- https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
- [minDominoRotations.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minDominoRotations.py) : passed
  - Runtime: 1651 ms, faster than 36.16% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
  - Memory Usage: 14.9 MB, less than 94.32% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
- [minDominoRotations2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minDominoRotations2.py) : passed
  - Runtime: 1291 ms, faster than 71.83% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
  - Memory Usage: 15.1 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
- algorithm: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/1865386/python3-Easy-Understandable-but-not-fast-(Runtime%3A-1291-ms-faster-than-71.83-)
  - the same number is tops[0] or bottoms[0].
  - when we find top row will have the same number.
    - count tops[0] in tops   -> min (count , len(tops) - count)
    - count bottoms[0] in tops   -> min (count , len(tops) - count)
  - when we find bottom row will have the same number.
    - count tops[0] in bottoms   -> min (count , len(bottoms) - count)
    - count bottoms[0] in bottoms   -> min (count , len(bottms) - count)
  - minimum count of these counts is answer  

# 51. Count Collisions on a Road (#2211) - medium / python : 2020-03-20 Weekly Contest 285
- 2020-03-20 Weekly Contest 285 : https://leetcode.com/contest/weekly-contest-285/
- medium : it is good
- There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.
  - You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.
  - The number of collisions can be calculated as follows:
    - When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
    - When a moving car collides with a stationary car, the number of collisions increases by 1.
  - After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.
  - Return the total number of collisions that will happen on the road.
- https://leetcode.com/problems/count-collisions-on-a-road/
- [countCollisions.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countCollisions.py) : passed

# 52. Maximum Points in an Archery Competition (#2212) - medium / python : 2020-03-20 Weekly Contest 285 (3H)
- 2020-03-20 Weekly Contest 285 : https://leetcode.com/contest/weekly-contest-285/
- medium
- problem
```
Alice and Bob are opponents in an archery competition. The competition has set the following rules:
    Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
    The points are then calculated as follows:
        The target has integer scoring sections ranging from 0 to 11 inclusive.
        For each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
        However, if ak == bk == 0, then nobody takes k points.
    For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.
You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.
Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.
If there are multiple ways for Bob to earn the maximum total points, return any one of them.
```
- https://leetcode.com/problems/maximum-points-in-an-archery-competition/
- [maximumBobPoints.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumBobPoints.py) : passed  - we can get score from mask.(3H)
  - 510 ms
- [maximumBobPoints2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumBobPoints2.py) : passed - optimization (mask , score) (3H)
  - Runtime: 396 ms, faster than 100.00% of Python3 online submissions for Maximum Points in an Archery Competition
  - Memory Usage: 14.2 MB, less than 25.00% of Python3 online submissions for Maximum Points in an Archery Competition.
- algorithm :
  - DP solution
    - basically we can get score from mask. but we calculate simultaneously to reduce running time.
    - mem = {} key : (scoring_section,remaining_arrow_count) , value : (mask,score)
    - divide two part : including scoring_section or not
      - self.dp(numArrows- (aliceArrows[scoring_section]+1) , mask , scoring_section-1 , score , aliceArrows[:-1])
      - self.dp(numArrows , mask , scoring_section-1 , score , aliceArrows[:-1])

# 53. Longest Substring of One Repeating Character (#2213) - hard : 2020-03-20 Weekly Contest 285  <fail>
- 2020-03-20 Weekly Contest 285 : https://leetcode.com/contest/weekly-contest-285/
- hard : 
- problem :
  - You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.
  - The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].
  - Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.
- https://leetcode.com/problems/longest-substring-of-one-repeating-character/
- [longestRepeating.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/longestRepeating.py) : timeout  47 / 56 test cases passed.
- [longestRepeating2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/longestRepeating2.py) : SortedList timeout 47 / 57 test cases passed.
  - longestRepeating problem : total_time1 :  820.4899926185608 -> ERROR([0]) -> 91541 63248 63248
- algorithm :
  - ```for char, i in zip(queryCharacters, queryIndices):```
  - from sortedcontainers import SortedList

# 54. Partition Labels (#763) - medium / python / 2H
- medium
- problem :
  - You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
  - Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
  - Return a list of integers representing the size of these parts.
- https://leetcode.com/problems/partition-labels/
- [partitionLabels.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/partitionLabels.py) : passed (2H)
  - Runtime: 40 ms, faster than 92.01% of Python3 online submissions for Partition Labels.
  - Memory Usage: 13.8 MB, less than 78.97% of Python3 online submissions for Partition Labels.
- algorithm :
  - current character does not exist after this position.  (frequency)
    ```python
        freq = {}   # set frequency
        stack = {}  # this is dictionary push / pop
        for (i,c) in enumerate(list(s)) :
            freq[c] -= 1
            if freq[c] == 0 :
                stack.pop(c,None)  # pop
                if len(stack.keys()) == 0:
                    r.append(i+1-p)
                    p = i+1
            else :
                stack[c] = 0  # push    
    ```

# 55. Smallest String With A Given Numeric Value (#1663) - medium / python / 2H
- medium
- problem :
  - The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.
  - The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.
  - You are given two integers n and k. Return the ***lexicographically smallest string*** with length equal to n and numeric value equal to k.
  - Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
- https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
- [getSmallestString.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/getSmallestString.py) : passed (1H)
  - Runtime: 60 ms, faster than 89.86% of Python3 online submissions for Smallest String With A Given Numeric Value.
  - Memory Usage: 14.9 MB, less than 87.56% of Python3 online submissions for Smallest String With A Given Numeric Value.
- algorithm :
  - find z counts until remainK - remianN < 26
  - ord() chr()

# 56. Broken Calculator (#991) - medium / python / 3H
- medium
- problem :
  - There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
    - multiply the number on display by 2, or
    - subtract 1 from the number on display.
  - Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
- https://leetcode.com/problems/broken-calculator/
- [brokenCalc.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/brokenCalc.py) : passed (3H)
- algorithm :
  - if target is odd , target + 1 and count + 1
  - first of all , we reduce the target as half.  target//2 and count+1. then if target//2 is odd , target//2 + 1 and count + 1 until target//2 is greater than startValue.
- best : [C++] || iterative || 100% faster || O(1) space
  - https://leetcode.com/problems/broken-calculator/discuss/1875138/C%2B%2B-oror-iterative-oror-100-faster-oror-O(1)-space

# 57. Boats to Save People (#881) - medium / python / 1H
- medium
- problem :
  - You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
  - Return the minimum number of boats to carry every given person.
- https://leetcode.com/problems/boats-to-save-people/
- [numRescueBoats.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/numRescueBoats.py) : passed (1H)
  - Runtime: 690 ms, faster than 32.63% of Python3 online submissions for Boats to Save People.
  - Memory Usage: 20.9 MB, less than 80.59% of Python3 online submissions for Boats to Save People.
- algorithm :
  - one moves maximum two people . it is NP problem if some people.
  - maxium weight should ride with minimum weight. 

# 58. Two City Scheduling (#1029) - medium / python / 1H
- medium
- problem :
  - A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
  - Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
- https://leetcode.com/problems/two-city-scheduling/
- [twoCitySchedCost.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/twoCitySchedCost.py) : passed (1H)
  - Runtime: 44 ms, faster than 83.79% of Python3 online submissions for Two City Scheduling.
  - Memory Usage: 14 MB, less than 45.30% of Python3 online submissions for Two City Scheduling.
- algorithm :
  - if difference of distance between 2 cities is longer , we should choose this person to get in there with shorter distance.
  - so get difference , and sort and process from reversed order (from longer distance)

# 59. Minimum Operations to Halve Array Sum (#2208) - medium / python / <got help>
- medium
- problem : 
  - You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)
  - Return the minimum number of operations to reduce the sum of nums by at least half.
- https://leetcode.com/contest/biweekly-contest-74/problems/minimum-operations-to-halve-array-sum/
  - https://leetcode.com/problems/minimum-operations-to-halve-array-sum/  
- [halveArray.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/halveArray.py) : 34 / 62 test cases passed.  timeout
  - len: 6151 total_time1 :  0.0009927749633789062 ->  total_time1 :  0.18049407005310059 -> SUCCESS -> 4741 1566
  - len: 55140 total_time1 :  0.011967897415161133 ->  total_time1 :  16.77672529220581 -> ERROR(0) -> 42729 13876
- [halveArray2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/halveArray2.py) : slower
  - total_time1 :  2.7269339561462402 -> SUCCESS -> 4741 6150
- [halveArray3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/halveArray3.py) : passed <got help>
  - len: 6151 total_time1 :  0.0009980201721191406 ->  total_time1 :  0.009979724884033203 -> SUCCESS -> 4741 1566
  - len: 55140 total_time1 :  0.010994911193847656 ->  total_time1 :  0.10970282554626465 -> ERROR(0) -> 42729 13876
- algorithm : https://www.daleseo.com/python-heapq/
  - choose the largest number and set to half  then repeat again until sum is less than half of origin sum.
  - we need sorted data struture (insert : logN , get the largest number : logN)
  - <got help> sorted data structure : [0] is the smallest number
    - import heapq   : heapq.heappush(list,value) heapq.heappop(list)   list[0] is minimal value.   if you want to maximum value , * -1.0 

# 60. Maximize Number of Subsequences in a String (#2207) - medium / python / 1H
- medium
- problem :
  - You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.
  - You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.
  - Return the maximum number of times pattern can occur as a subsequence of the modified text.
    - A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
- https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
- [maximumSubsequenceCount.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumSubsequenceCount.py) : passed
  - Runtime: 430 ms, faster than 50.97% of Python3 online submissions for Maximize Number of Subsequences in a String.
  - Memory Usage: 19.7 MB, less than 17.05% of Python3 online submissions for Maximize Number of Subsequences in a String.
- algorithm :
  - A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).  https://leetcode.com/problems/is-subsequence/
  - if pattern[0] == pattern[1] ,  n!
  - if not , pattern[0]+text or text+pattern[1]. then count pair.

# 61. Search in Rotated Sorted Array (#33) - medium / python / 2H
- medium 
- problem :
  - There is an integer array nums sorted in ascending order (with distinct values).
  - Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
  - Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
  - You must write an algorithm with O(log n) runtime complexity.
- https://leetcode.com/problems/search-in-rotated-sorted-array/description/
- [search.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/search.py) : passed
  - Runtime: 40 ms, faster than 94.48% of Python3 online submissions for Search in Rotated Sorted Array.
  - Memory Usage: 14.4 MB, less than 22.57% of Python3 online submissions for Search in Rotated Sorted Array.
- algorithm :
  - find index of max value or min value within O(logN)

# 62. Search in Rotated Sorted Array II (#81) - medium / python / 2D
- medium 
- problem :
  - There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
  - Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
  - Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
  - You must decrease the overall operation steps as much as possible.
  - Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
- https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
- [search-Duplicatable.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/search-Duplicatable.py) : passed
- algorithm :
-  if sample is 1,1,1,1,1,1,1,1,1,1,1,1,1,1  
-  we can not find the direction from mid position.
-  so O(N) is the solution in the worst case.


































































