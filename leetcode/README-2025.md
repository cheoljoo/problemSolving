TOC
- [1. Find a Safe Walk Through a Grid (#3286) - medium / python / 2H / 2024.11.06](#1-find-a-safe-walk-through-a-grid-3286---medium--python--2h--20241106)
- [2. Largest Combination With Bitwise AND Greater Than Zero (#2275) - medium / python / 1H / 2024.11.07](#2-largest-combination-with-bitwise-and-greater-than-zero-2275---medium--python--1h--20241107)
- [3. Find if Array Can Be Sorted (#3011) - medium / python / 30M / 2024.11.06](#3-find-if-array-can-be-sorted-3011---medium--python--30m--20241106)
- [4. Total Characters in String After Transformations I (#3335) - medium / python / 2H / 2024.11.18](#4-total-characters-in-string-after-transformations-i-3335---medium--python--2h--20241118)
- [5. Construct 2D Grid Matching Graph Layout (#3311) - hard / python / 3D / 2024.12.30](#5-construct-2d-grid-matching-graph-layout-3311---hard--python--3d--20241230)
- [6. Minimum Number of Operations to Sort a Binary Tree by Level (#2471) - medium / python / 6H / 2024.12.24](#6-minimum-number-of-operations-to-sort-a-binary-tree-by-level-2471---medium--python--6h--20241224)
- [7. Count Ways To Build Good Strings (#2466) - medium / python / solution / 2025.01.02](#7-count-ways-to-build-good-strings-2466---medium--python--solution--20250102)
- [8. Minimum Time to Break Locks I (#3376) - medium / python / 2H / 2024.01.07](#8-minimum-time-to-break-locks-i-3376---medium--python--2h--20240107)
- [8. Shifting Letters II (#2381) - medium / python / 1H / 2024.01.09](#8-shifting-letters-ii-2381---medium--python--1h--20240109)

--------------------
leetcode : my profile -> https://leetcode.com/cheoljoo/

# 1. Find a Safe Walk Through a Grid (#3286) - medium / python / 2H / 2024.11.06
- https://leetcode.com/problems/find-a-safe-walk-through-a-grid
  - Runtime 63 ms Beats 90.75% / Memory 16.89 MB Beats 99.49%
- complexity : O()
- algorithm : 
- alternatives : 

# 2. Largest Combination With Bitwise AND Greater Than Zero (#2275) - medium / python / 1H / 2024.11.07
- https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero
  - Runtime 826 ms Beats 13.59% / Memory 26.81 MB Beats 45.06%
- complexity : O()
- algorithm : 
- alternatives : 

# 3. Find if Array Can Be Sorted (#3011) - medium / python / 30M / 2024.11.06
- https://leetcode.com/problems/find-if-array-can-be-sorted
  - Runtime 13 ms Beats 57.76% / Memory 16.65 MB Beats 89.52%
- complexity : O()
- algorithm : 
- alternatives : 

# 4. Total Characters in String After Transformations I (#3335) - medium / python / 2H / 2024.11.18
- https://leetcode.com/problems/total-characters-in-string-after-transformations-i
  - Runtime 5523 ms Beats 19.48% / Memory 17.25 MB Beats 81.27%
- complexity : O()
- algorithm : 
- alternatives : 

# 5. Construct 2D Grid Matching Graph Layout (#3311) - hard / python / 3D / 2024.12.30
- https://leetcode.com/problems/construct-2d-grid-matching-graph-layout
  - Runtime 4598 ms Beats 5.40% / Memory 67.48 MB Beats 9.46%
- complexity : O()
- algorithm : 
- alternatives : 

# 6. Minimum Number of Operations to Sort a Binary Tree by Level (#2471) - medium / python / 6H / 2024.12.24
- https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level
  - Runtime 293 ms Beats 14.34% / Memory 56.26 MB Beats 5.02%
- complexity : O()
- algorithm : 
- alternatives : 

# 7. Count Ways To Build Good Strings (#2466) - medium / python / solution / 2025.01.02
- https://leetcode.com/problems/count-ways-to-build-good-strings
- complexity : O()
- algorithm : 
- alternatives : 

# 8. Minimum Time to Break Locks I (#3376) - medium / python / 2H / 2024.01.07
- https://leetcode.com/problems/minimum-time-to-break-locks-i
  - Runtime 6837 ms Beats 15.88% / Memory 18.19 MB Beats 26.35%
- complexity : O()
- algorithm : 
- alternatives : 

# 8. Shifting Letters II (#2381) - medium / python / 1H / 2024.01.09
- first idea
  - brute force
  - use index and set the count in value of index and change character once.
  - get all boundaries (0,15) (5,20) (10,40) -> (0:1,16:-1) (5:1,21:-1) (10:1,41:-1) 로 하여 계산을 한다. 
    - 이 의미는 dict로 가지고 있으면 되며 , for i in range(len(s)) 를 할때 각 위치의 값이 dict가 있으면 해당 값을 더해주어 각 index에서 몇번을 left/right shift해야하는지 알수 있게 해주는 것이다.
- https://leetcode.com/problems/shifting-letters-ii
  - brute force : Time Limit Exceeded 32 / 39 testcases passed
  - 
- complexity : O()
- algorithm : 
- alternatives : 
