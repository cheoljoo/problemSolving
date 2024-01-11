- [1. unsolved](#1-unsolved)
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
  - [2.12. Longest Increasing Subsequence (#300) - medium / python / solution / 2024.01.12](#212-longest-increasing-subsequence-300---medium--python--solution--20240112)


--------------------
leetcode : my profile -> https://leetcode.com/cheoljoo/

# 1. unsolved


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

## 2.12. Longest Increasing Subsequence (#300) - medium / python / solution / 2024.01.12
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








