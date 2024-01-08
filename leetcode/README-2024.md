- [1. unsolved](#1-unsolved)
  - [1.1. 3Sum (#15) - medium / python / 20M / 2024.01.05](#11-3sum-15---medium--python--20m--20240105)
- [2. solved](#2-solved)
  - [2.1. Remove Duplicates from Sorted Array II (#80) - medium / python / 30M / 2024.01.02](#21-remove-duplicates-from-sorted-array-ii-80---medium--python--30m--20240102)
  - [2.2. Convert an Array Into a 2D Array With Conditions (#2610) - medium / python / 30M / 2024.01.02](#22-convert-an-array-into-a-2d-array-with-conditions-2610---medium--python--30m--20240102)
  - [2.3. Best Time to Buy and Sell Stock (#121) - easy / python / 30M / 2024.01.02](#23-best-time-to-buy-and-sell-stock-121---easy--python--30m--20240102)
  - [2.4. Number of Laser Beams in a Bank (#2125) - medium / python / 30M / 2024.01.03](#24-number-of-laser-beams-in-a-bank-2125---medium--python--30m--20240103)
  - [2.5. Minimum Number of Operations to Make Array Empty (#2870) - medium / python / 30M / 2024.01.04](#25-minimum-number-of-operations-to-make-array-empty-2870---medium--python--30m--20240104)
  - [2.6. Valid Palindrome (#125) - easy / python / 9M / 2024.01.04](#26-valid-palindrome-125---easy--python--9m--20240104)
  - [2.7. Range Sum of BST (#938) - easy / python / 5M / 2024.01.08](#27-range-sum-of-bst-938---easy--python--5m--20240108)


--------------------
leetcode : my profile -> https://leetcode.com/cheoljoo/

# 1. unsolved
## 1.1. 3Sum (#15) - medium / python / 20M / 2024.01.05
- https://leetcode.com/problems/3sum/
- algorithm 1 : i use dictionary to calculate earlier. i save all information within O(N^2). but it is not solution. i am curious whether dictionay saving is budden.
  - i need to study more


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





