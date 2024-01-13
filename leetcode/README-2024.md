- [1. unsolved](#1-unsolved)
  - [1.1. Longest Increasing Subsequence (#300) - medium / python / solution / 2024.01.12](#11-longest-increasing-subsequence-300---medium--python--solution--20240112)
- [2. solved](#2-solved)
  - [2.1. Remove Duplicates from Sorted Array II (#80) - medium / python / 30M / 2024.01.02](#21-remove-duplicates-from-sorted-array-ii-80---medium--python--30m--20240102)
  - [2.2. Convert an Array Into a 2D Array With Conditions (#2610) - medium / python / 30M / 2024.01.02](#22-convert-an-array-into-a-2d-array-with-conditions-2610---medium--python--30m--20240102)
  - [2.3. Best Time to Buy and Sell Stock (#121) - easy / python / 30M / 2024.01.02](#23-best-time-to-buy-and-sell-stock-121---easy--python--30m--20240102)
  - [2.4. Number of Laser Beams in a Bank (#2125) - medium / python / 30M / 2024.01.03](#24-number-of-laser-beams-in-a-bank-2125---medium--python--30m--20240103)
  - [2.5. Minimum Number of Operations to Make Array Empty (#2870) - medium / python / 30M / 2024.01.04](#25-minimum-number-of-operations-to-make-array-empty-2870---medium--python--30m--20240104)
  - [2.6. Valid Palindrome (#125) - easy / python / 9M / 2024.01.04](#26-valid-palindrome-125---easy--python--9m--20240104)
  - [2.7. Range Sum of BST (#938) - easy / python / 5M / 2024.01.08](#27-range-sum-of-bst-938---easy--python--5m--20240108)
  - [2.8. 3Sum (#15) - medium / python / 2D / 2024.01.05 (recommend)](#28-3sum-15---medium--python--2d--20240105-recommend)
    - [2.8.1. compare between list and set()  : 3Sum (#15)](#281-compare-between-list-and-set---3sum-15)
  - [2.9. Leaf-Similar Trees (#872) - easy / python / 5M / 2024.01.09](#29-leaf-similar-trees-872---easy--python--5m--20240109)
  - [2.10. Valid Number (#65) - hard / python / 30M / 2024.01.09](#210-valid-number-65---hard--python--30m--20240109)
  - [2.11. Amount of Time for Binary Tree to Be Infected (#2385) - medium / python / 2H / 2024.01.11](#211-amount-of-time-for-binary-tree-to-be-infected-2385---medium--python--2h--20240111)
  - [2.12. Maximum Difference Between Node and Ancestor (#1026) - medium / python / 4M / 2024.01.11](#212-maximum-difference-between-node-and-ancestor-1026---medium--python--4m--20240111)
  - [2.13. Determine if String Halves Are Alike (#1704) - easy / python / 5M / 2024.01.12](#213-determine-if-string-halves-are-alike-1704---easy--python--5m--20240112)
  - [2.14. Max Points on a Line (#149) - hard / python / 15M / 2024.01.12](#214-max-points-on-a-line-149---hard--python--15m--20240112)
  - [2.15. Group Anagrams (#49) - medium / python / 4M / 2024.01.12](#215-group-anagrams-49---medium--python--4m--20240112)
  - [2.16. Candy (#135) - hard / python / 40M / 2024.01.12](#216-candy-135---hard--python--40m--20240112)
  - [2.17. Minimum Number of Steps to Make Two Strings Anagram (#1347) - medium / python / 6M / 2024.01.13](#217-minimum-number-of-steps-to-make-two-strings-anagram-1347---medium--python--6m--20240113)
  - [2.18. Basic Calculator (#224) - hard / python / 1H / 2024.01.13](#218-basic-calculator-224---hard--python--1h--20240113)
  - [2.19. Summary Ranges (#228) - easy / python / 10M / 2024.01.13](#219-summary-ranges-228---easy--python--10m--20240113)
  - [2.20. Pow(x, n) (#50) - medium / python / 40M / 2024.01.13](#220-powx-n-50---medium--python--40m--20240113)
  - [2.21. Single Number II (#137) - medium / python / 10M / 2024.01.13](#221-single-number-ii-137---medium--python--10m--20240113)
  - [2.22. Merge Intervals (#56) - medium / python / 20M / 2024.01.13](#222-merge-intervals-56---medium--python--20m--20240113)
  - [2.23. Binary Tree Right Side View (#199) - medium / python / 25M / 2024.01.13](#223-binary-tree-right-side-view-199---medium--python--25m--20240113)
  - [2.24. Binary Tree Level Order Traversal (#102) - medium / python / 3M / 2024.01.13](#224-binary-tree-level-order-traversal-102---medium--python--3m--20240113)
  - [2.25. Binary Tree Zigzag Level Order Traversal (#103) - medium / python / 3M / 2024.01.13](#225-binary-tree-zigzag-level-order-traversal-103---medium--python--3m--20240113)
  - [2.26. Valid Sudoku (#36) - medium / python / 31M / 2024.01.13](#226-valid-sudoku-36---medium--python--31m--20240113)


--------------------
leetcode : my profile -> https://leetcode.com/cheoljoo/

# 1. unsolved
## 1.1. Longest Increasing Subsequence (#300) - medium / python / solution / 2024.01.12
- https://leetcode.com/problems/longest-increasing-subsequence
  - refer to https://leetcode.com/problems/longest-increasing-subsequence/solutions/4509322/c-python-binary-search-3-ms-beats-98-69
- complexity : O(NlogN)
- algorithm : 
  - ```
    Let's see the process for the testcase [10,9,2,5,3,7,101,18]:
    10<=10 replace:[10]
    9<=10 replace:[9]
    2<=9 replace:[2]
    5>2 append:[2, 5]
    3<=5 replace:[2, 3]
    7>3 append:[2, 3, 7]
    101>7 append:[2, 3, 7, 101]
    18<=101 replace:[2, 3, 7, 18]

    [0,1,0,3,2,3]
    [0, 1] 1
    [0, 1] 0
    [0, 1, 3] 3
    [0, 1, 2] 2
    [0, 1, 2, 3] 3

    [4,10,4,3,8,9]
    [4, 10] 10
    [4, 10] 4
    [3, 10] 3
    [3, 8] 8
    [3, 8, 9] 9
    ```


# 2. solved
## 2.1. Remove Duplicates from Sorted Array II (#80) - medium / python / 30M / 2024.01.02
- https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
  - Runtime 69 ms  Beats 12.96% /  Memory 17.2 MB  Beats 16.82%
- algorithm : modifying the input array in-place with O(1) extra memory.
- complexity : O(N)

## 2.2. Convert an Array Into a 2D Array With Conditions (#2610) - medium / python / 30M / 2024.01.02
- https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
  - Runtime 103 ms  Beats 5.01% /  Memory 17.3 MB  Beats 12.28%
- complexity : O(N)

## 2.3. Best Time to Buy and Sell Stock (#121) - easy / python / 30M / 2024.01.02
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
  - Runtime 2301 ms  Beats 5.01% /  Memory 29.4 MB  Beats 9.52%
- complexity : O(N)
- algorithm : left2right max, right2left max

## 2.4. Number of Laser Beams in a Bank (#2125) - medium / python / 30M / 2024.01.03
- https://leetcode.com/problems/number-of-laser-beams-in-a-bank
  - Runtime 275 ms  Beats 9.28% /  Memory 20 MB  Beats 6.86%
- complexity : O(MN)   m == bank.length   n == bank[i].length

## 2.5. Minimum Number of Operations to Make Array Empty (#2870) - medium / python / 30M / 2024.01.04
- https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
  - Runtime 586 ms  Beats 83.33% /  Memory 31.6 MB  Beats 18.18%
- complexity : O(N)
- algorithm : use dictionary and calculate directly from 3 and 2 multiply.

## 2.6. Valid Palindrome (#125) - easy / python / 9M / 2024.01.04
- https://leetcode.com/problems/valid-palindrome/
  - Runtime 54 ms  Beats 42.94% /  Memory 17.7 MB  Beats 48.45%
- complexity : O(N)

## 2.7. Range Sum of BST (#938) - easy / python / 5M / 2024.01.08
- https://leetcode.com/problems/range-sum-of-bst/
  - Runtime 125 ms  Beats 88.25% /  Memory 24.56 MB  Beats 79.04%
- complexity : O(N)

## 2.8. 3Sum (#15) - medium / python / 2D / 2024.01.05 (recommend)
- https://leetcode.com/problems/3sum/
  - Runtime 548 ms  Beats 96.53% /  Memory 21.3 MB  Beats 33.44%
- complexity : O(N^2)
- algorithm 1 : i use dictionary to calculate earlier. i save all information within O(N^2). but it is not solution. i am curious whether dictionay saving is budden.
  - i need to study more
### 2.8.1. compare between list and set()  : 3Sum (#15)
- list : tmplist = [nums[i],nums[j],nums[k]]
  - list.append(tmplist)
- set : tmptuple = (nums[i],nums[j],nums[k])
  - set.add(tmptuple)
- set is faster when we want to add item
  - if tmplist not in list:     list.append(tmplist)
  - set.add(tmptuple)

## 2.9. Leaf-Similar Trees (#872) - easy / python / 5M / 2024.01.09
- https://leetcode.com/problems/leaf-similar-trees/
  - Runtime 29 ms  Beats 96.99% /  Memory 17.39 MB  Beats 18.13%
- complexity : O(N)

## 2.10. Valid Number (#65) - hard / python / 30M / 2024.01.09
- https://leetcode.com/problems/valid-number/
  - Runtime 47ms Beats 28.93% , Memory 17.40MB Beats 14.83%
- complexity : O(N)

## 2.11. Amount of Time for Binary Tree to Be Infected (#2385) - medium / python / 2H / 2024.01.11
- https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
  - Runtime 280ms Beats 98.89% / Memory 58.45MB Beats 90.72%
- complexity : O(N)
- testcase
  - ```
    [1,5,3,null,4,10,6,9,2]
    3
    [1]
    1
    [1,null,2,3,4,null,5]
    4
    [1,2,null,3,null,4,null,5]
    2
    [5,2,3,4,null,null,null,1]
    4
    ```
- algorithm : tree traverse is first. then change tree that the start value's node will be root.  additionally start node dropped after child depth to reduce the calculation count.

## 2.12. Maximum Difference Between Node and Ancestor (#1026) - medium / python / 4M / 2024.01.11
- https://leetcode.com/problems/maximum-difference-between-node-and-ancestor
  - [ Time taken: 3 m 48 s ] Runtime 37ms Beats 88.16% / Memory 18.87MB Beats 89.04%
- complexity : O(N)
- algorithm : node value exists between min and max of his ancestors.

## 2.13. Determine if String Halves Are Alike (#1704) - easy / python / 5M / 2024.01.12
- https://leetcode.com/problems/determine-if-string-halves-are-alike
  - [ Time taken: 4 m 29 s ] Runtime 42ms Beats 55.68% / Memory 17.34MB Beats 19.92%
- complexity : O(N)

## 2.14. Max Points on a Line (#149) - hard / python / 15M / 2024.01.12
- https://leetcode.com/problems/max-points-on-a-line
  - [ Time taken: 14 m 53 s ] Runtime 100ms Beats 48.21% / Memory 41.68MB Beats 5.69%
- complexity : O(N^2)
- algorithm : y = Ax + B , consider one point , consider (A,B) , consider (1,3) , (2,3)
- https://leetcode.com/studyplan/top-interview-150/

## 2.15. Group Anagrams (#49) - medium / python / 4M / 2024.01.12
- https://leetcode.com/problems/group-anagrams
  - [ Time taken: 3 m 32 s ] Runtime 75ms Beats 99.34% / Memory 20.41MB  Beats 57.05%
- complexity : O(N^2*logN)
- algorithm : N * sorted(NlogN) / hashmap
- https://leetcode.com/studyplan/top-interview-150/

## 2.16. Candy (#135) - hard / python / 40M / 2024.01.12
- https://leetcode.com/problems/candy
  - Runtime 139ms Beats 64.60% / Memory 20.32MB Beats 17.86%
- complexity : O(N)
- algorithm : increased_array , decreased_array 
- https://leetcode.com/studyplan/top-interview-150/

## 2.17. Minimum Number of Steps to Make Two Strings Anagram (#1347) - medium / python / 6M / 2024.01.13
- https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram
  - [ Time taken: 5 m 37 s ] Runtime 190ms Beats 42.11% / Memory 18.21MB Beats 5.24%
- complexity : O(N)

## 2.18. Basic Calculator (#224) - hard / python / 1H / 2024.01.13
- https://leetcode.com/problems/basic-calculator
  - Runtime 160ms Beats 12.08% / Memory 19.60MB Beats 17.75%
- complexity : O(N)
- algorithm : stack and backtracking , consider +(22)
- https://leetcode.com/studyplan/top-interview-150/

## 2.19. Summary Ranges (#228) - easy / python / 10M / 2024.01.13
- https://leetcode.com/problems/summary-ranges
  - Runtime 33ms Beats 84.66% / Memory  17.26MB  Beats 30.86%
- complexity : O(N)
- algorithm : intervals
- https://leetcode.com/studyplan/top-interview-150/

## 2.20. Pow(x, n) (#50) - medium / python / 40M / 2024.01.13
- https://leetcode.com/problems/powx-n
  - Runtime 36ms Beats 68.98% / Memory 17.40 MB Beats 5.04%
- complexity : O(logN)

## 2.21. Single Number II (#137) - medium / python / 10M / 2024.01.13
- https://leetcode.com/problems/single-number-ii
  - Runtime 59ms Beats 75.62% / Memory 19.69MB Beats 6.91%
- complexity : O(N)
- algorithm : Bit Manipulation
- https://leetcode.com/studyplan/top-interview-150/

## 2.22. Merge Intervals (#56) - medium / python / 20M / 2024.01.13
- https://leetcode.com/problems/merge-intervals
  - [ Time taken: 30 m 29 s ] Runtime 135ms Beats 55.61% / Memory 21.44MB Beats 32.50%
- complexity : O(NlogN)
- algorithm : sort , intervals
- https://leetcode.com/studyplan/top-interview-150/

## 2.23. Binary Tree Right Side View (#199) - medium / python / 25M / 2024.01.13
- https://leetcode.com/problems/binary-tree-right-side-view
  - Runtime 37ms Beats 72.40% / Memory 17.48MB Beats 17.33%
- complexity : O(N)
- algorithm : Binary Tree DFS with depth  , BFS
- https://leetcode.com/studyplan/top-interview-150/

## 2.24. Binary Tree Level Order Traversal (#102) - medium / python / 3M / 2024.01.13
- https://leetcode.com/problems/binary-tree-level-order-traversal
  - [ Time taken: 2 m 52 s ] Runtime 39ms  Beats 84.61% / Memory 18.19MB  Beats 17.17%
- complexity : O(N)
- algorithm : Binary Tree DFS with depth , BFS
- https://leetcode.com/studyplan/top-interview-150/

## 2.25. Binary Tree Zigzag Level Order Traversal (#103) - medium / python / 3M / 2024.01.13
- https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
  - [ Time taken: 1 m 38 s ] Runtime 35ms Beats 84.20% / Memory 17.56MB Beats 17.02%
- complexity : O(N)
- algorithm : Binary Tree DFS with depth , BFS
- https://leetcode.com/studyplan/top-interview-150/

## 2.26. Valid Sudoku (#36) - medium / python / 31M / 2024.01.13
- https://leetcode.com/problems/valid-sudoku
  - [ Time taken: 30 m 53 s ] Runtime 96ms Beats 70.49% / Memory 17.30MB Beats 22.81%
- complexity : O(N)
- algorithm : Matrix
- https://leetcode.com/studyplan/top-interview-150/






