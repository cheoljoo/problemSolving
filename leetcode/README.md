- [1. knowledge](#1-knowledge)
  - [1.1. sort performance](#11-sort-performance)
  - [1.2. sort keys](#12-sort-keys)
  - [1.3. sorted data structure](#13-sorted-data-structure)
    - [1.3.1. bisect](#131-bisect)
    - [1.3.2. heapq](#132-heapq)
    - [1.3.3. PriorityQueue](#133-priorityqueue)
    - [1.3.4. sortedcontainers](#134-sortedcontainers)
    - [1.3.5. in place sort](#135-in-place-sort)
  - [1.4. Euclidean-algorithm : 유클리드 호제법](#14-euclidean-algorithm--유클리드-호제법)
  - [1.5. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree](#15-height-balanced-binary-search-trees--avlcreatoradelson-velsky-and-landis-tree)
  - [1.6. hamming weight : number of '1' bits](#16-hamming-weight--number-of-1-bits)
  - [1.7. find (?,?) including A among [(x1,x2) , ....] if x1>x2](#17-find--including-a-among-x1x2---if-x1x2)
  - [1.8. two dimensional array initialize and set](#18-two-dimensional-array-initialize-and-set)
  - [1.9. regular expression (import re)](#19-regular-expression-import-re)
    - [1.9.1. difference between re.search() and re.match()](#191-difference-between-research-and-rematch)
  - [1.10. format string](#110-format-string)
  - [1.11. lexicographical order](#111-lexicographical-order)
  - [1.12. dictionary : Python Remove Key from a Dictionary: A Complete Guide](#112-dictionary--python-remove-key-from-a-dictionary-a-complete-guide)
  - [1.13. list : python remove element from a list](#113-list--python-remove-element-from-a-list)
  - [1.14. graph](#114-graph)
    - [1.14.1. dijkstra](#1141-dijkstra)
  - [1.15. greedy algorithm](#115-greedy-algorithm)
    - [1.15.1. dijkstra's algorithm](#1151-dijkstras-algorithm)
    - [1.15.2. Ford-Fulkerson Algorithm](#1152-ford-fulkerson-algorithm)
    - [1.15.3. Kruskal's Algorithm : find minimum spanning tree : optimal graph connected all vertics](#1153-kruskals-algorithm--find-minimum-spanning-tree--optimal-graph-connected-all-vertics)
    - [1.15.4. Prim's Algorithm : find minimum spanning tree](#1154-prims-algorithm--find-minimum-spanning-tree)
    - [1.15.5. Huffman Coding : a technique of compressing data to reduce its size](#1155-huffman-coding--a-technique-of-compressing-data-to-reduce-its-size)
  - [1.16. Dynamic Programming](#116-dynamic-programming)
    - [1.16.1. Longest Common Subsequence](#1161-longest-common-subsequence)
    - [1.16.2. Floyd-Warshall Algorithm](#1162-floyd-warshall-algorithm)
  - [1.17. grouping : find & union](#117-grouping--find--union)
  - [1.18. deque](#118-deque)
  - [1.19. Books & URL](#119-books--url)
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
- [15. Maximum Subarray : DP - easy but hard (got help)](#15-maximum-subarray--dp---easy-but-hard-got-help)
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
- [42. Maximize the Topmost Element After K Moves (#2202) - medium : weekly contest for amazon 2022-03-13 / (got help)](#42-maximize-the-topmost-element-after-k-moves-2202---medium--weekly-contest-for-amazon-2022-03-13--got-help)
- [43. Minimum Weighted Subgraph With the Required Paths (#2203) - hard : weekly contest for amazon 2022-03-13 / (got help)](#43-minimum-weighted-subgraph-with-the-required-paths-2203---hard--weekly-contest-for-amazon-2022-03-13--got-help)
- [44. Simplify Path (#71) - medium](#44-simplify-path-71---medium)
- [45. Minimum Remove to Make Valid Parentheses ($1249) - medium](#45-minimum-remove-to-make-valid-parentheses-1249---medium)
- [46. Validate Stack Sequences (#946) - medium / python / rust](#46-validate-stack-sequences-946---medium--python--rust)
- [47. Score of Parentheses (#856) - medium : / python](#47-score-of-parentheses-856---medium---python)
- [48. Remove Duplicate Letters (#316) (#1081) - medium : [python]](#48-remove-duplicate-letters-316-1081---medium--python)
- [49. Maximum Frequency Stack (#895) - hard : / python](#49-maximum-frequency-stack-895---hard---python)
- [50. Minimum Domino Rotations For Equal Row (#1007) - medium / python](#50-minimum-domino-rotations-for-equal-row-1007---medium--python)
- [51. Count Collisions on a Road (#2211) - medium / python : 2020-03-20 Weekly Contest 285](#51-count-collisions-on-a-road-2211---medium--python--2020-03-20-weekly-contest-285)
- [52. Maximum Points in an Archery Competition (#2212) - medium / python : 2020-03-20 Weekly Contest 285 (3H)](#52-maximum-points-in-an-archery-competition-2212---medium--python--2020-03-20-weekly-contest-285-3h)
- [53. Longest Substring of One Repeating Character (#2213) - hard : 2020-03-20 Weekly Contest 285  (fail)](#53-longest-substring-of-one-repeating-character-2213---hard--2020-03-20-weekly-contest-285--fail)
- [54. Partition Labels (#763) - medium / python / 2H](#54-partition-labels-763---medium--python--2h)
- [55. Smallest String With A Given Numeric Value (#1663) - medium / python / 2H](#55-smallest-string-with-a-given-numeric-value-1663---medium--python--2h)
- [56. Broken Calculator (#991) - medium / python / 3H](#56-broken-calculator-991---medium--python--3h)
- [57. Boats to Save People (#881) - medium / python / 1H](#57-boats-to-save-people-881---medium--python--1h)
- [58. Two City Scheduling (#1029) - medium / python / 1H](#58-two-city-scheduling-1029---medium--python--1h)
- [59. Minimum Operations to Halve Array Sum (#2208) - medium / python / (got help)](#59-minimum-operations-to-halve-array-sum-2208---medium--python--got-help)
- [60. Maximize Number of Subsequences in a String (#2207) - medium / python / 1H](#60-maximize-number-of-subsequences-in-a-string-2207---medium--python--1h)
- [61. Search in Rotated Sorted Array (#33) - medium / python / 2H](#61-search-in-rotated-sorted-array-33---medium--python--2h)
- [62. Search in Rotated Sorted Array II (#81) - medium / python / 2D](#62-search-in-rotated-sorted-array-ii-81---medium--python--2d)
- [63. Valid Palindrome II (#680) - easy / python / 1H](#63-valid-palindrome-ii-680---easy--python--1h)
- [64. Next Permutation (#31) - medium / python / 2H](#64-next-permutation-31---medium--python--2h)
- [65. Container With Most Water(#11) - medium / python / 1H](#65-container-with-most-water11---medium--python--1h)
- [66. Kth Largest Element in a Stream (#703) - easy / python / 1H](#66-kth-largest-element-in-a-stream-703---easy--python--1h)
- [67. 3Sum With Multiplicity (#923) - medium / python / 1H](#67-3sum-with-multiplicity-923---medium--python--1h)
- [68. Top K Frequent Elements (#347) - medium / python / 1H](#68-top-k-frequent-elements-347---medium--python--1h)
- [69. Largest Number After Digit Swaps by Parity (#2231) - easy / python / 20M / 2020-04-10 Weekly Contest 288 (Airwallex)](#69-largest-number-after-digit-swaps-by-parity-2231---easy--python--20m--2020-04-10-weekly-contest-288-airwallex)
- [70. Minimize Result by Adding Parentheses to Expression (#2232) - medium / python / 34M / 2020-04-10 Weekly Contest 288 (Airwallex)](#70-minimize-result-by-adding-parentheses-to-expression-2232---medium--python--34m--2020-04-10-weekly-contest-288-airwallex)
- [71. Maximum Product After K Increments (#2233) - medium / python / 22M / 2020-04-10 Weekly Contest 288 (Airwallex)](#71-maximum-product-after-k-increments-2233---medium--python--22m--2020-04-10-weekly-contest-288-airwallex)
- [72. Maximum Total Beauty of the Gardens (#2234) - hard / python / (fail)  / 2020-04-10 Weekly Contest 288 (Airwallex)](#72-maximum-total-beauty-of-the-gardens-2234---hard--python--fail---2020-04-10-weekly-contest-288-airwallex)
- [73. Game of Life (#289) - medium / python / 15M](#73-game-of-life-289---medium--python--15m)
- [74. Spiral Matrix II (#59) - medium / python / 15M](#74-spiral-matrix-ii-59---medium--python--15m)
- [75. Trim a Binary Search Tree (#669) - medium / python / 10M](#75-trim-a-binary-search-tree-669---medium--python--10m)
- [76. Convert BST to Greater Tree (#538) - medium / python / 2H](#76-convert-bst-to-greater-tree-538---medium--python--2h)
- [77. Merge k Sorted Lists (#23) - hard / python / 3H](#77-merge-k-sorted-lists-23---hard--python--3h)
- [78. Increasing Order Search Tree (#897) - easy / python / 20M](#78-increasing-order-search-tree-897---easy--python--20m)
- [79. Largest Rectangle in Histogram (#84) - hard / python / 2D](#79-largest-rectangle-in-histogram-84---hard--python--2d)
- [80. Special Day solved 100 problems on leetcode (2002-04-17 Sunday)](#80-special-day-solved-100-problems-on-leetcode-2002-04-17-sunday)
- [81. Remove Invalid Parentheses (#301) - hard / python / 4H  / greedy : O(2^N)](#81-remove-invalid-parentheses-301---hard--python--4h---greedy--o2n)
- [82. Kth Smallest Element in a BST (#230) - medium / python / 30M](#82-kth-smallest-element-in-a-bst-230---medium--python--30m)
- [83. Longest Common Subsequence (#1143) - medium / python / 1H / (got help)](#83-longest-common-subsequence-1143---medium--python--1h--got-help)
- [84. Recover Binary Search Tree (#99) - medium / python / 30M](#84-recover-binary-search-tree-99---medium--python--30m)
- [85. Longest Valid Parentheses (#32) - hard / python / 4H](#85-longest-valid-parentheses-32---hard--python--4h)
- [86. Binary Search Tree Iterator (#173) - medium / c++ / 10M](#86-binary-search-tree-iterator-173---medium--c--10m)
- [87. Reverse Nodes in k-Group (#25) - hard / c++ / 20M / Top 100 Liked Questions](#87-reverse-nodes-in-k-group-25---hard--c--20m--top-100-liked-questions)
- [88. First Missing Positive (#41) - hard / python / 20M / Top 100 Liked Questions](#88-first-missing-positive-41---hard--python--20m--top-100-liked-questions)
- [89. Trapping Rain Water (#42) - hard / python / 30M / Top 100 Liked Questions / coalTar](#89-trapping-rain-water-42---hard--python--30m--top-100-liked-questions--coaltar)
- [90. Edit Distance (#72) - hard / python / 3H / (got help) / Top 100 Liked Questions / BEST DP problem](#90-edit-distance-72---hard--python--3h--got-help--top-100-liked-questions--best-dp-problem)
- [91. Maximal Rectangle (#85) - hard / python / 1D / Top 100 Liked Questions](#91-maximal-rectangle-85---hard--python--1d--top-100-liked-questions)
- [92. Encode and Decode TinyURL (#535) - medium / python / 5M](#92-encode-and-decode-tinyurl-535---medium--python--5m)
- [93. Design Underground System (#1396) - medium / python / c++ / 30M (caution : should be different between variables and funciton names)](#93-design-underground-system-1396---medium--python--c--30m-caution--should-be-different-between-variables-and-funciton-names)
- [94. Peeking Iterator (#284) - medium / python / c++ / 1H](#94-peeking-iterator-284---medium--python--c--1h)
- [95. Min Cost to Connect All Points (#1584) - medium / python / 3H](#95-min-cost-to-connect-all-points-1584---medium--python--3h)
- [96. Minimum Window Substring (#76) - hard / python / 2D / (got help) : sliding window (left->right) / Top 100 Liked Questions](#96-minimum-window-substring-76---hard--python--2d--got-help--sliding-window-left-right--top-100-liked-questions)
- [97. Smallest String With Swaps (#1202) - medium / python / 2D / (got help) : grouping](#97-smallest-string-with-swaps-1202---medium--python--2d--got-help--grouping)
- [98. Path With Minimum Effort (#1631) - medium / python / 1D / (got help) : Dijkstra](#98-path-with-minimum-effort-1631---medium--python--1d--got-help--dijkstra)
- [99. Is Graph Bipartite? (#785) - medium / python / 3H / black&white](#99-is-graph-bipartite-785---medium--python--3h--blackwhite)
- [100. Evaluate Division(#399) - medium / python / 3H / grouping : find&union](#100-evaluate-division399---medium--python--3h--grouping--findunion)
- [101. Sliding Window Maximum (#239) - hard / python / sliding : left->right : deque / Top 100 Liked Questions (got help)](#101-sliding-window-maximum-239---hard--python--sliding--left-right--deque--top-100-liked-questions-got-help)
- [102. hiking - hard / python / dijkstra / 1D / SW_TEST](#102-hiking---hard--python--dijkstra--1d--sw_test)
- [103. Binary Tree Maximum Path Sum (#124) - hard / python / 3H / tree : dfs : left,right,root,leftroot,rightroot,leftrootright / Top 100 Liked Questions](#103-binary-tree-maximum-path-sum-124---hard--python--3h--tree--dfs--leftrightrootleftrootrightrootleftrootright--top-100-liked-questions)
- [104. Find Median from Data Stream (#295) - hard / python / 2H / bisect / Top 100 Liked Questions](#104-find-median-from-data-stream-295---hard--python--2h--bisect--top-100-liked-questions)
- [105. Shortest Unsorted Continuous Subarray (#581) - medium / python / 1H](#105-shortest-unsorted-continuous-subarray-581---medium--python--1h)
- [106. Max Number of K-Sum Pairs (#1679) - medium / python / 1H](#106-max-number-of-k-sum-pairs-1679---medium--python--1h)
- [107. Wildcard Matching (#44) - hard / python / 1D / Top Interview Questions](#107-wildcard-matching-44---hard--python--1d--top-interview-questions)
- [108. Remove All Adjacent Duplicates in String II (#1209) - medium / python / 2H](#108-remove-all-adjacent-duplicates-in-string-ii-1209---medium--python--2h)
- [109. 132 Pattern (#456) - medium / python / 1D (got help)](#109-132-pattern-456---medium--python--1d-got-help)
- [110. Flatten Nested List Iterator (#341) - medium / python / 2H](#110-flatten-nested-list-iterator-341---medium--python--2h)
- [111. Letter Combinations of a Phone Number (#17) - medium / python / 1H](#111-letter-combinations-of-a-phone-number-17---medium--python--1h)
- [112. Word Ladder (#127) - hard / python / 3D / BFS / Top Interview Questions / (got help) / (fail)](#112-word-ladder-127---hard--python--3d--bfs--top-interview-questions--got-help--fail)
- [113. Count Sorted Vowel Strings (#1641) - medium / python / 1H](#113-count-sorted-vowel-strings-1641---medium--python--1h)
- [114. Combination Sum III (#216) - medium / python / 1H](#114-combination-sum-iii-216---medium--python--1h)
- [115. Longest Increasing Path in a Matrix (#329) - hard / python / 2H / dynamic programming / Top Interview Questions](#115-longest-increasing-path-in-a-matrix-329---hard--python--2h--dynamic-programming--top-interview-questions)
- [116. Permutations II (#47) - medium / python / 30M](#116-permutations-ii-47---medium--python--30m)
- [117. Populating Next Right Pointers in Each Node II (#117) - medium / python / BFS / find sibling node / 20M](#117-populating-next-right-pointers-in-each-node-ii-117---medium--python--bfs--find-sibling-node--20m)
- [118. Daily Temperatures (#739) - medium / python / stack / 15M / Top 100 Liked Questions](#118-daily-temperatures-739---medium--python--stack--15m--top-100-liked-questions)
- [119. Subarray Sum Equals K (#560) - medium / python / Top 100 Liked Questions / (got help)](#119-subarray-sum-equals-k-560---medium--python--top-100-liked-questions--got-help)
- [120. Network Delay Time (#743) - medium / python / graph / dijkstra](#120-network-delay-time-743---medium--python--graph--dijkstra)
- [121. Deepest Leaves Sum (#1302) - medium / python / dfs / tree traverse / 20M](#121-deepest-leaves-sum-1302---medium--python--dfs--tree-traverse--20m)
- [122. Shortest Path in Binary Matrix (#1091) - medium / python /  bfs / 1D](#122-shortest-path-in-binary-matrix-1091---medium--python---bfs--1d)
- [123. Target Sum (#494) - medium / python / dp / Top 100 Liked Questions / 45M](#123-target-sum-494---medium--python--dp--top-100-liked-questions--45m)
- [124. Critical Connections in a Network (#1192) - hard / python / graph / loop / (ing)](#124-critical-connections-in-a-network-1192---hard--python--graph--loop--ing)
- [125. Unique Paths II (#63) - medium / python / dfs / dp / 5H](#125-unique-paths-ii-63---medium--python--dfs--dp--5h)
- [126. template (#) - medium / python / (ing)](#126-template----medium--python--ing)

--------------------
leetcode : my profile -> https://leetcode.com/cheoljoo/
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
- dictionary sort
  - ```sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])```

## 1.3. sorted data structure
### 1.3.1. bisect
- import bisect
- from bisect import bisect_right , bisect_left
- bisect.insort()
- bisect.bisect_left()
- bisect.bisect_right()
- [bisectExample.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/bisectExample.py)
  - caution : it makes module error when you make the file as bisect.py.
  - Do NOT use the same filename with import module name.
```python
python3 bisectExample.py
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6] n: 4 bisect_left: 2
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6] n: 4 bisect_right: 2
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6] n: 5 bisect_left: 2
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6] n: 5 bisect_right: 9
```

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

### 1.3.5. in place sort
- ```nums[i:] = sorted(nums[i:])   # in place sort```

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

## 1.11. lexicographical order
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

## 1.14. graph
### 1.14.1. dijkstra
- [Dijkstra](https://www.programiz.com/dsa/dijkstra-algorithm#:~:text=Dijkstra's%20algorithm%20allows%20us%20to,the%20vertices%20of%20the%20graph.)  O(E Log V)
    - Src1 src2 -> dst 으로 갈때의 최소 path를 구하라. : 각각에서 가야하할때의 노드로 갈때의 최소값을 구한다  dijkstra.
    - 어떤 노드에서 3개의 목적지로 가는 최소값들을 가진 것 (src1 -> node , src2 -> node , dst -> node) 일때의 합이 최소가 되는 것이 src1,src2->node->dst로 가는 최소값이 된다.  node는 모든 node를 넣어볼수 있다. src1,src2,dst도 node가 될수 있다. 
    - 여기 쓴 내용은 방향성이 없을때.  양방향 가능
```python
    def dijkstra(self,n: int, graph: Dict[int,Tuple[int,int]], f: int): 
        result = [math.inf for _ in range(n)]
        q = [(0,f)]   # (total weight,node)
        while q:
            weight, start = heapq.heappop(q)
            if result[start]  != math.inf :
                continue
            result[start] = weight
            if start in graph:
                for nxt,w in graph[start]:
                    if result[nxt] == math.inf:
                        heapq.heappush(q,(weight + w,nxt))
        return result
```

## 1.15. greedy algorithm
- Greedy Choice Property : If an optimal solution to the problem can be found by choosing the best choice at each step without reconsidering the previous steps once chosen, the problem can be solved using a greedy approach. This property is called greedy choice property.
  - Problem: You have to make a change of an amount using the smallest possible number of coins.
    - Amount: $18
    - Available coins are
      -   $5 coin
      -   $2 coin
      -   $1 coin
    - There is no limit to the number of each coin you can use.
### 1.15.1. dijkstra's algorithm
- [1.14.1. dijkstra](#1141-dijkstra)

### 1.15.2. Ford-Fulkerson Algorithm
- Ford-Fulkerson algorithm is a greedy approach for calculating the maximum possible flow in a network or a graph.
- Each pipe has a certain capacity of liquid it can transfer at an instance. For this algorithm, we are going to find how much liquid can be flowed from the source to the sink at an instance using the network.
  - ![](https://cdn.programiz.com/sites/tutorial2program/files/flow-network.png)
- algorithm :
  1. find path with BFS (parent is path from sink.)
  2. sum path flow
  3. change graph (substract graph capacity when they used from sink)
  4. goto 1

### 1.15.3. Kruskal's Algorithm : find minimum spanning tree : optimal graph connected all vertics
- We start from the edges with the lowest weight and keep adding edges until we reach our goal. The steps for implementing Kruskal's algorithm are as follows:
  - Sort all the edges from low weight to high
  - Take the edge with the lowest weight and add it to the spanning tree. **If adding the edge created a cycle,** then reject this edge.
  - Keep adding edges until we reach all vertices.
  - ![](https://cdn.programiz.com/sites/tutorial2program/files/ka-1.png)
- algorithm :
  - checking the loop is key factor. if both vertics of edge are in current graph , it is loop.  <-  i think it is faster than suggested code.

### 1.15.4. Prim's Algorithm : find minimum spanning tree
- i do not know what is difference with kruskal's algorithm
  
### 1.15.5. Huffman Coding : a technique of compressing data to reduce its size
- Using the Huffman Coding technique, we can compress the string to a smaller size. Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.

| Character       | Frequency | Code | Size     |
| --------------- | --------- | ---- | -------- |
| A               | 5         | 11   | 5*2 = 10 |
| B               | 1         | 100  | 1*3 = 3  |
| C               | 6         | 0    | 6*1 = 6  |
| D               | 3         | 101  | 3*3 = 9  |
| 4 * 8 = 32 bits | 15 bits   |      | 28 bits  |

## 1.16. Dynamic Programming
- if there are overlapping among these subproblems, then the solutions to these subproblems can be saved for future reference. 
- This technique of storing the value of subproblems is called memoization. By saving the values in the array, we save time for computations of sub-problems we have already come across.

### 1.16.1. Longest Common Subsequence
- https://riptutorial.com/algorithm/example/24007/longest-common-subsequence-explanation
- O(MN) 
- Table[2][3] represents the length of the longest common subsequence between "ac" and "abc".
- 
    |     |     |   0 |   1 |   2 |   3 |   4 |   5 |   6 |
    |-----|-----|-----|-----|-----|-----|-----|-----|-----|
    |     | chʳ |     |  a  |  b  |  c  |  d  |  a  |  f  |
    |  0  |     |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
    |  1  |  a  |  0  |  1  |  1  |  1  |  1  |  1  |  1  |
    |  2  |  c  |  0  |  1  |     |     |     |     |     |
    |  3  |  b  |  0  |     |     |     |     |     |     |
    |  4  |  c  |  0  |     |     |     |     |     |     |
    |  5  |  f  |  0  |     |     |     |     |     |     |
- if s2[i] is not equal to s1[j] =>   Table[i][j] = max(Table[i-1][j], Table[i][j-1]
- if s2[i] equals to s1[j]       =>   Table[i][j] = Table[i-1][j-1] + 1

### 1.16.2. Floyd-Warshall Algorithm
- https://www.programiz.com/dsa/floyd-warshall-algorithm
- Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph. This algorithm works for both the directed and undirected weighted graphs. 
- ![](https://cdn.programiz.com/sites/tutorial2program/files/fw-Graph.png)  ![](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-1.png) ![](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-2.png)
- O(N^3)

## 1.17. grouping : find & union
- it is faster than union() in set.
```python
        p = list(range(len(s)))  # parent
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[py] = px
        # Grouping
        for x, y in pairs:
            union(x, y)
        for i in range(len(p)):
            p[i] = find(p[i])    
```

## 1.18. deque
- https://leonkong.cc/posts/python-deque.html
  - deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
  - deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
  - deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
  - deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
  - deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
  - deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
  - deque.remove(item): item을 데크에서 찾아 삭제한다.
  - deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

## 1.19. Books & URL
- Python module of the week : http://pymotw.com/2/PyMOTW-1.133.pdf
- RealPython : http://www.realpython.org
- For Beginners for graph : https://leetcode.com/discuss/study-guide/1808711/Graph-for-Beginers-Problems
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

# 15. Maximum Subarray : DP - easy but hard (got help)
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

# 42. Maximize the Topmost Element After K Moves (#2202) - medium : weekly contest for amazon 2022-03-13 / (got help)
- medium : (got help) I didn't understand what measn until now. I saw the following article before solving this problem.
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

# 43. Minimum Weighted Subgraph With the Required Paths (#2203) - hard : weekly contest for amazon 2022-03-13 / (got help)
- hard : (got help)
  - I did not solve this probelm within contest. I can not try it because i can not understand the meaning of #2202.
- You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.
  - You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.
  - Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.
  - Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.
- https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
- algorithm : dest -> src1 , dest -> src2
- [minimumWeight.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumWeight.py) :  failed.  83 / 86 test cases passed.
- [minimumWeight2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumWeight2.py) : passed
  - Runtime: 4126 ms, faster than 12.66% of Python3 online submissions for Minimum Weighted Subgraph With the Required Paths.
  - Memory Usage: 78.7 MB, less than 97.58% of Python3 online submissions for Minimum Weighted Subgraph With the Required Paths.
- [minimumWeight_dijkstra.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumWeight_dijkstra.py) : passed (got help)
  - Runtime: 3053 ms, faster than 57.42% of Python3 online submissions for Minimum Weighted Subgraph With the Required Paths.
  - Memory Usage: 75 MB, less than 99.62% of Python3 online submissions for Minimum Weighted Subgraph With the Required Paths.
- algorithm :
  - [Dijkstra](https://www.programiz.com/dsa/dijkstra-algorithm#:~:text=Dijkstra's%20algorithm%20allows%20us%20to,the%20vertices%20of%20the%20graph.)
    - Src1 src2 -> dst 으로 갈때의 최소 path를 구하라. : 각각에서 가야하할때의 노드로 갈때의 최소값을 구한다  dijkstra.
    - 어떤 노드에서 3개의 목적지로 가는 최소값들을 가진 것 (src1 -> node , src2 -> node , dst -> node) 일때의 합이 최소가 되는 것이 src1,src2->node->dst로 가는 최소값이 된다.  node는 모든 node를 넣어볼수 있다. src1,src2,dst도 node가 될수 있다. 
    - 여기 쓴 내용은 방향성이 없을때.  양방향 가능
    - ![](https://github.com/cheoljoo/problemSolving/blob/master/images/dijkstra2.jpg)
  - if graph has direction , src1 -> Vertex (from->to) / src2 -> Vertex (from->to)  / dest -> Vertex (to->from)
    - src1 -> node and src2 -> node and dest -> node : 이 최소가 되는 node를 통해서 가는 것이 shortest path가 되는 것이다. 
```python
    def dijkstra(self,n: int, graph: Dict[int,Tuple[int,int]], f: int): 
        result = [math.inf for _ in range(n)]
        q = [(0,f)]   # (total weight,node)
        while q:
            weight, start = heapq.heappop(q)
            if result[start]  != math.inf :
                continue
            result[start] = weight
            if start in graph:
                for nxt,w in graph[start]:
                    if result[nxt] == math.inf:
                        heapq.heappush(q,(weight + w,nxt))
        return result
```
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

# 53. Longest Substring of One Repeating Character (#2213) - hard : 2020-03-20 Weekly Contest 285  (fail)
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

# 59. Minimum Operations to Halve Array Sum (#2208) - medium / python / (got help)
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
- [halveArray3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/halveArray3.py) : passed (got help)
  - len: 6151 total_time1 :  0.0009980201721191406 ->  total_time1 :  0.009979724884033203 -> SUCCESS -> 4741 1566
  - len: 55140 total_time1 :  0.010994911193847656 ->  total_time1 :  0.10970282554626465 -> ERROR(0) -> 42729 13876
- algorithm : https://www.daleseo.com/python-heapq/
  - choose the largest number and set to half  then repeat again until sum is less than half of origin sum.
  - we need sorted data struture (insert : logN , get the largest number : logN)
  - (got help) sorted data structure : [0] is the smallest number
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

# 63. Valid Palindrome II (#680) - easy / python / 1H
- easy
- problem :
  - Given a string s, return true if the s can be palindrome after deleting at most one character from it.
- https://leetcode.com/problems/valid-palindrome-ii/
- [validPalindrome.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/validPalindrome.py) : passed

# 64. Next Permutation (#31) - medium / python / 2H
- medium : leetcode check the memory status whether solver returns different memory vs given memory.
- problem :
  - A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    - For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
  - The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
    - For example, the next permutation of arr = [1,2,3] is [1,3,2].
    - Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    - While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
  - Given an array of integers nums, find the next permutation of nums.
  - The replacement must be in place and use only constant extra memory.
- https://leetcode.com/problems/next-permutation/
- [nextPermutation.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/nextPermutation.py) : passed
  - Runtime: 79 ms, faster than 16.37% of Python3 online submissions for Next Permutation.
  - Memory Usage: 14 MB, less than 28.23% of Python3 online submissions for Next Permutation.
- algorithm : need in-place calculation
  - first : find decreaing index    ex) [1, 4, 7, 5, 3]   decreasing index nums[2]=7 i=2  so swap i-1 and minimun value among larger than nums[i-1]
  - second : swap and sort   ex) 4 , 5 swap  -> 7,4,3 sort -> 3,4,7    so answer is 1,5,3,4,7
  - in-place sort : ```nums[i:] = sorted(nums[i:])```

# 65. Container With Most Water(#11) - medium / python / 1H
- medium
- problem : 
  - You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
  - Find two lines that together with the x-axis form a container, such that the container contains the most water.
  - Return the maximum amount of water a container can store.
  - Notice that you may not slant the container.
- https://leetcode.com/problems/container-with-most-water/
- [maxArea.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxArea.py) : passed  O(NlogN)
  - Runtime: 2113 ms, faster than 5.00% of Python3 online submissions for Container With Most Water.
  - Memory Usage: 31.4 MB, less than 17.98% of Python3 online submissions for Container With Most Water.
- algorithm :
  - sort with height
  - start from higher bar then calculate area with location.  we can know the minimum and maximum location.
  - height * area [ max of abs(min or max - cur_location) ]
- best : 
  - Time: O(n) , Space: O(1) - https://leetcode.com/problems/container-with-most-water/discuss/1915108/Python3-GREEDY-TWO-POINTERS-~(~)-Explained
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
				l += 1
            else:
				r -= 1
        return area
```

# 66. Kth Largest Element in a Stream (#703) - easy / python / 1H
- easy
- problem : 
  - Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
  - Implement KthLargest class:
    - KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    - int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
- https://leetcode.com/problems/kth-largest-element-in-a-stream/
- [KthLargest.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/KthLargest.py) : passed
  - Runtime: 128 ms, faster than 62.88% of Python3 online submissions for Kth Largest Element in a Stream.
  - Memory Usage: 18.3 MB, less than 55.88% of Python3 online submissions for Kth Largest Element in a Stream.
- algorithm :
  - sort and pick largest to kth largest
  - to get kth largest element , we will use heapq
  - ***caution : test case is important.  first time , testcase is started from []. and they will add kth element.***

# 67. 3Sum With Multiplicity (#923) - medium / python / 1H
- medium
- problem :
  - Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
  - As the answer can be very large, return it modulo 10^9 + 7.
- https://leetcode.com/problems/3sum-with-multiplicity/
- [threeSumMulti.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/threeSumMulti.py) : passed
  - Runtime: 103 ms, faster than 78.10% of Python3 online submissions for 3Sum With Multiplicity.
  - Memory Usage: 14.4 MB, less than 7.07% of Python3 online submissions for 3Sum With Multiplicity.
- algorithm :
  - make distict array and sort
  - i == j == k 
  - i == j != k
  - i != j == j
  - i != j != k 

# 68. Top K Frequent Elements (#347) - medium / python / 1H
- medium
- problem :
  - Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
- https://leetcode.com/problems/top-k-frequent-elements
- [topKFrequent.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/topKFrequent.py) : passed
  - Runtime: 100 ms, faster than 96.24% of Python3 online submissions for Top K Frequent Elements.
  - Memory Usage: 18.7 MB, less than 68.16% of Python3 online submissions for Top K Frequent Elements.
- algorithm :
  - count & reversed sort
  - choose k element : ```ans = [key for (i,(value,key)) in enumerate(kfreq) if i < k ]```

# 69. Largest Number After Digit Swaps by Parity (#2231) - easy / python / 20M / 2020-04-10 Weekly Contest 288 (Airwallex)
- easy : 2020-04-10 Weekly Contest 288 (Airwallex)
- my best score of leetcode contest : ![](https://github.com/cheoljoo/problemSolving/blob/master/images/contest288.jpg)
- problem :
  - You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).
  - Return the largest possible value of num after any number of swaps.
- https://leetcode.com/contest/weekly-contest-288/problems/largest-number-after-digit-swaps-by-parity/
  - https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
- [largestInteger.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/largestInteger.py) : passed
- algorithm :
  - distinguish between odd and even.  and reverse sort odd / even list separately.
  - record the odd or even each position.
  - put odd/even number according to position.


# 70. Minimize Result by Adding Parentheses to Expression (#2232) - medium / python / 34M / 2020-04-10 Weekly Contest 288 (Airwallex)
- medium : 2020-04-10 Weekly Contest 288 (Airwallex)
- problem :
  - You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.
  - Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.
  - Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.
  - The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.
- https://leetcode.com/contest/weekly-contest-288/problems/minimize-result-by-adding-parentheses-to-expression/
  - https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
- [minimizeResult.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimizeResult.py) : passed
  - Runtime: 35 ms
- algorithm :
  - split into two number
  - first number : get all cases with (left part of parenthese , right part of parenthese , first 1 is the digit or not of number)
  -  ex) 247 -> (1, 247,1) (2,47,0) (24,7,0)
  -  ex) 12 -> (1,12,1) (1,2,0)
-  second number : get all cases
   -  ex) 38 -> (38,1,1) (3,8,0)

# 71. Maximum Product After K Increments (#2233) - medium / python / 22M / 2020-04-10 Weekly Contest 288 (Airwallex)
- medium : 2020-04-10 Weekly Contest 288 (Airwallex)
- problem :
  - You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.
  - Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7.
- https://leetcode.com/contest/weekly-contest-288/problems/maximum-product-after-k-increments/
  - https://leetcode.com/problems/maximum-product-after-k-increments/
- [maximumProduct.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumProduct.py) : passed
  - Runtime : 3081 ms  :  all solutions have the same algorithm. this time depends on computer status.
  
# 72. Maximum Total Beauty of the Gardens (#2234) - hard / python / (fail)  / 2020-04-10 Weekly Contest 288 (Airwallex)
- hard : 2020-04-10 Weekly Contest 288 (Airwallex)
- problem :
  - Alice is a caretaker of n gardens and she wants to plant flowers to maximize the total beauty of all her gardens.
  - You are given a 0-indexed integer array flowers of size n, where flowers[i] is the number of flowers already planted in the ith garden. Flowers that are already planted cannot be removed. You are then given another integer newFlowers, which is the maximum number of flowers that Alice can additionally plant. You are also given the integers target, full, and partial.
  - A garden is considered complete if it has at least target flowers. The total beauty of the gardens is then determined as the sum of the following:
    - The number of complete gardens multiplied by full.
    - The minimum number of flowers in any of the incomplete gardens multiplied by partial. If there are no incomplete gardens, then this value will be 0.
  - Return the maximum total beauty that Alice can obtain after planting at most newFlowers flowers.
- https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
- [maximumBeauty.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumBeauty.py) : 50 / 77 test cases passed.
- [maximumBeauty2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumBeauty2.py) : timeout 69 / 77 test cases passed.  fail 800 sec
  - O(N^2) : generally  it is timeout. -> wrong answer
- [maximumBeauty3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximumBeauty3.py) : timeout 69 / 77 test cases passed.  fail 12sec
  - O(NlogN) : but it is timeout  -> wrong answer
- algorithm : (got help)
  - https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/discuss/1931085/Python-Explanation-with-pictures-Greedy.
  - I had the same idea. but i could not archive the goal.
- learning point :
  - use bisect : do not make the code for binary search


# 73. Game of Life (#289) - medium / python / 15M 
- medium 
- problem :
  - According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
  - The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
    - Any live cell with fewer than two live neighbors dies as if caused by under-population.
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies, as if by over-population.
    - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
  - The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
- https://leetcode.com/problems/game-of-life/
- [gameOfLife.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/gameOfLife.py) : passed
  - Runtime: 36 ms, faster than 85.68% of Python3 online submissions for Game of Life.
  - Memory Usage: 14 MB, less than 12.69% of Python3 online submissions for Game of Life.
- algorithm :
  - make bigger board with border to calculate easily

# 74. Spiral Matrix II (#59) - medium / python / 15M
- medium : matrix
- problem :
  - Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.
- https://leetcode.com/problems/spiral-matrix-ii/
- [generateMatrix.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/generateMatrix.py) : passed
  - Runtime: 30 ms, faster than 92.84% of Python3 online submissions for Spiral Matrix II.
  - Memory Usage: 13.9 MB, less than 85.84% of Python3 online submissions for Spiral Matrix II.
- algorithm :
  - have direction (clockwise)

# 75. Trim a Binary Search Tree (#669) - medium / python / 10M
- medium : tree
- problem :
  - Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
  - Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
- https://leetcode.com/problems/trim-a-binary-search-tree/
- [trimBST.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/trimBST.py) : passed
  - Runtime: 44 ms, faster than 98.59% of Python3 online submissions for Trim a Binary Search Tree.
  - Memory Usage: 18.1 MB, less than 11.70% of Python3 online submissions for Trim a Binary Search Tree.
- algorithm : show the source code
  - if node.val is less than low , node.left do not need it. because all elements of node.left tree are less than low.
  - high is the same process.   less -> greater / low -> high / left -> right

# 76. Convert BST to Greater Tree (#538) - medium / python / 2H
- medium : tree
- problem :
  - iven the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
  - As a reminder, a binary search tree is a tree that satisfies these constraints:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.
- https://leetcode.com/problems/convert-bst-to-greater-tree/
- [convertBST.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/convertBST.py) : passed
  - Runtime: 89 ms, faster than 79.93% of Python3 online submissions for Convert BST to Greater Tree.
  - Memory Usage: 16.6 MB, less than 97.31% of Python3 online submissions for Convert BST to Greater Tree.
- algorithm :
  - sum of traverse order : this is tree traverse problem

# 77. Merge k Sorted Lists (#23) - hard / python / 3H
- hard : linked list
- problem :
  - You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
  - Merge all the linked-lists into one sorted linked-list and return it.
- https://leetcode.com/problems/merge-k-sorted-lists/
- [mergeKLists.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/mergeKLists.py) : passed
  - Runtime: 104 ms, faster than 91.25% of Python3 online submissions for Merge k Sorted Lists.
  - Memory Usage: 18.1 MB, less than 44.92% of Python3 online submissions for Merge k Sorted Lists.
- algorithm :
  - find minimum value -> use heapq
  - keep the node -> reuse the node : not create the node

# 78. Increasing Order Search Tree (#897) - easy / python / 20M
- easy : tree traverse
- problem :
  - Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
- https://leetcode.com/problems/increasing-order-search-tree/
- [increasingBST.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/increasingBST.py) : passed
  - Runtime: 36 ms, faster than 76.74% of Python3 online submissions for Increasing Order Search Tree.
  - Memory Usage: 14 MB, less than 13.79% of Python3 online submissions for Increasing Order Search Tree.

# 79. Largest Rectangle in Histogram (#84) - hard / python / 2D
- hard
- problem : 
  - Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
- https://leetcode.com/problems/largest-rectangle-in-histogram/
- [largestRectangleArea.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/largestRectangleArea.py) : passed O(N^2)
  - Runtime: 6923 ms, faster than 5.02% of Python3 online submissions for Largest Rectangle in Histogram.
  - Memory Usage: 28 MB, less than 79.09% of Python3 online submissions for Largest Rectangle in Histogram.
- algorithm :
  - gather if colsed histogram has the same height : 1000, 1000 , 1000 >> (1000,3) -> sort
  - O(N^2)  : caculdate left and right direction if he can go. 
- BEST (got help) : https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/1954731/EASY-C%2B%2B-SOLUTION-or-NSR-or-NSL-or-STACK
  - O(N)
  - get all left ( 0 -> N)  , get all right (N -> 0)
  - [largestRectangleArea2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/largestRectangleArea2.py) : passed O(N)
    - Runtime: 1278 ms, faster than 57.51% of Python3 online submissions for Largest Rectangle in Histogram.
    - Memory Usage: 27.8 MB, less than 83.45% of Python3 online submissions for Largest Rectangle in Histogram.

# 80. Special Day solved 100 problems on leetcode (2002-04-17 Sunday)
- ![](https://github.com/cheoljoo/problemSolving/blob/master/images/leetcode-100.jpg)


# 81. Remove Invalid Parentheses (#301) - hard / python / 4H  / greedy : O(2^N)
- hard : greedy algorithm  O(2^N)  len < 50
- problem :
  - Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
  - Return all the possible results. You may return the answer in any order.
- https://leetcode.com/problems/remove-invalid-parentheses/
- [removeInvalidParentheses.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeInvalidParentheses.py) : passed O(2^N)
  - Runtime: 538 ms, faster than 46.19% of Python3 online submissions for Remove Invalid Parentheses.
  - Memory Usage: 14 MB, less than 64.31% of Python3 online submissions for Remove Invalid Parentheses.
- algorithm : greedy algorithm  O(2^N)  len < 50
  - remove mis-order of start with ')' and end with '('. becasue it should be removed
  - greedy algorithm
    - check the finalization : if recursive reaches the end  and it is valid , this is the smallest removeCount.
    - if not end
      - copy stack and run recursive with both stay and remove.

# 82. Kth Smallest Element in a BST (#230) - medium / python / 30M
- medium
- problem :
  - Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
- https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- [kthSmallest.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/kthSmallest.py) : passed
  - Runtime: 47 ms, faster than 96.14% of Python3 online submissions for Kth Smallest Element in a BST.
  - Memory Usage: 18 MB, less than 48.12% of Python3 online submissions for Kth Smallest Element in a BST.

# 83. Longest Common Subsequence (#1143) - medium / python / 1H / (got help)
- medium
- problem :
  - Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
  - A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    - For example, "ace" is a subsequence of "abcde".
  - A common subsequence of two strings is a subsequence that is common to both strings.
- https://leetcode.com/problems/longest-common-subsequence/
- [longestCommonSubsequence.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/longestCommonSubsequence.py) : passed (got help)
  - Runtime: 416 ms, faster than 86.70% of Python3 online submissions for Longest Common Subsequence.
  - Memory Usage: 22 MB, less than 77.27% of Python3 online submissions for Longest Common Subsequence.
- algorithm : 
  - [1.16.1. Longest Common Subsequence](#1161-longest-common-subsequence)
    - https://riptutorial.com/algorithm/example/24007/longest-common-subsequence-explanation
    - https://leetcode.com/problems/longest-common-subsequence/discuss/1944428/C%2B%2B-Easy-brute-force-and-simple-DP-solution
  - if s2[i] is not equal to s1[j] =>   Table[i][j] = max(Table[i-1][j], Table[i][j-1]
  - if s2[i] equals to s1[j]       =>   Table[i][j] = Table[i-1][j-1] + 1
  
# 84. Recover Binary Search Tree (#99) - medium / python / 30M
- medium
- problem :
  - You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
  - Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
- https://leetcode.com/problems/recover-binary-search-tree/
- [recoverTree.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/recoverTree.py) : passed  O(n) space , O(NlogN) time complexity
  - Runtime: 76 ms, faster than 86.88% of Python3 online submissions for Recover Binary Search Tree.
  - Memory Usage: 14.3 MB, less than 65.76% of Python3 online submissions for Recover Binary Search Tree.
- [recoverTree2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/recoverTree2.py) : passed  O(1) space , O(N) time complexity
  - Runtime: 83 ms, faster than 71.70% of Python3 online submissions for Recover Binary Search Tree.
  - Memory Usage: 14.4 MB, less than 28.16% of Python3 online submissions for Recover Binary Search Tree.
- algorithm :
  - method 1: O(n) space , O(NlogN) time complexity 
    - traverse with sorted order.
    - if this order is not proper , it is mistake for swapping.
  - method 2 : O(1) space , O(N) time complexity
    - traverse twice
        - 1. get list  and check what is mistake
        - 2. change value
    - it has strange result. method 2 is slower than method 1.  -> I guess tree traverse is slower than sort or arrary (list) operation.

# 85. Longest Valid Parentheses (#32) - hard / python / 4H
- hard
- problem :
  - Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
  - longest continuous substring
- https://leetcode.com/problems/longest-valid-parentheses/
- [longestValidParentheses.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/longestValidParentheses.py) : passed  O(N)
  - Runtime: 66 ms, faster than 45.88% of Python3 online submissions for Longest Valid Parentheses.
  - Memory Usage: 15.9 MB, less than 7.48% of Python3 online submissions for Longest Valid Parentheses.
- algorithm :
  - use 2 stack : one is for parethesis and the other is for count.
  - stack :
    - () -> ['s',2]
    - (()) -> when input is last ')' , then stack is [ ['(',2] , ['s',2] ] .   so we backtrace to reach '('.  => stack is [ ['s',4 ] ]
  - pStack : we use it to check whether '(' remains or not.
- best :  use distance instead of () counts.
  - [Simple O(n) memory and time Python using stack in 10 lines](https://leetcode.com/problems/longest-valid-parentheses/discuss/1905363/Simple-O(n)-memory-and-time-Python-using-stack-in-10-lines)
  - The idea is to find the **distance** between the current close paranethesis and the last [potentially] unmatched close paranthese.
  - To avoid edge cases, we initialize the stack with -1, meaning that initially no sign of misalignment exists.


# 86. Binary Search Tree Iterator (#173) - medium / c++ / 10M
- medium : binary search tree
- problem : 
  - Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
    - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    - boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    - int next() Moves the pointer to the right, then returns the number at the pointer.
  - Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
  - You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
- https://leetcode.com/problems/binary-search-tree-iterator/
- [BSTIterator.cpp](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/BSTIterator.cpp) : passed
  - Runtime: 54 ms, faster than 18.47% of C++ online submissions for Binary Search Tree Iterator.
  - Memory Usage: 24.3 MB, less than 22.22% of C++ online submissions for Binary Search Tree Iterator.

# 87. Reverse Nodes in k-Group (#25) - hard / c++ / 20M / Top 100 Liked Questions
- hard : linked list
- problem : 
  - Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
  - k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
  - You may not alter the values in the list's nodes, only nodes themselves may be changed.
  - Follow-up: Can you solve the problem in O(1) extra memory space?
- https://leetcode.com/problems/reverse-nodes-in-k-group/
- [reverseKGroup.cpp](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/reverseKGroup.cpp) : passed  space:O(K) time-complexity:O(N)
  - Runtime: 12 ms, faster than 94.30% of C++ online submissions for Reverse Nodes in k-Group.
  - Memory Usage: 11.8 MB, less than 8.01% of C++ online submissions for Reverse Nodes in k-Group.
- algorithm :
  - // go to k-th next node
    - // remain node count is less than k  -> keep it (not change)
  - // change node values
  - goto loop

# 88. First Missing Positive (#41) - hard / python / 20M / Top 100 Liked Questions
- hard
- problem :
  - Given an unsorted integer array nums, return the smallest missing positive integer.
  - You must implement an algorithm that runs in O(n) time and uses constant extra space.
- https://leetcode.com/problems/first-missing-positive/
- [firstMissingPositive.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/firstMissingPositive.py) : passed   O(N) - long initiating time
  - Runtime: 5172 ms, faster than 5.02% of Python3 online submissions for First Missing Positive.
  - Memory Usage: 62.8 MB, less than 47.28% of Python3 online submissions for First Missing Positive.
- ```M = 5*(10**5)+1``` -> ```M = len(nums)+1``` : passed O(N)
  - Runtime: 969 ms, faster than 79.09% of Python3 online submissions for First Missing Positive.
  - Memory Usage: 63.2 MB, less than 46.60% of Python3 online submissions for First Missing Positive.
- algorithm :
  - key is that maximum length of list is 500000. so i reserved the memory.
  - if nums[i] is negative or is greater than 500000, we throw away it.
  - mem[0:500001] will set the value of nums[]

# 89. Trapping Rain Water (#42) - hard / python / 30M / Top 100 Liked Questions / coalTar
- hard : coalTar
- problem :
  - Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
- https://leetcode.com/problems/trapping-rain-water/
- [trap.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/trap.py) : passed   O(N)
  - Runtime: 100 ms, faster than 91.15% of Python3 online submissions for Trapping Rain Water.
  - Memory Usage: 15.7 MB, less than 92.92% of Python3 online submissions for Trapping Rain Water.
- algorithm :
  - find max (leftIndex , RightIndex of Max)
  - Left Trap
  - Max .. Max Trap
  - Right Trap

# 90. Edit Distance (#72) - hard / python / 3H / (got help) / Top 100 Liked Questions / BEST DP problem
- hard : BEST DP problem
- problem :
  - Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
  - You have the following three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character
- https://leetcode.com/problems/edit-distance/
- [minDistance.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minDistance.py) : passed  DP:O(MN)
  - Runtime: 187 ms, faster than 67.86% of Python3 online submissions for Edit Distance.
  - Memory Usage: 16.1 MB, less than 91.66% of Python3 online submissions for Edit Distance.
- algorithm : greedy O(2^N) , DP O(MN)  (got help)
  - https://leetcode.com/problems/edit-distance/discuss/1955895/Python-oror-Faster-than-95.38-oror-Easy-to-Understand-Solution

# 91. Maximal Rectangle (#85) - hard / python / 1D / Top 100 Liked Questions
- hard 
- problem :
  - Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
- https://leetcode.com/problems/maximal-rectangle/
- [maximalRectangle.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximalRectangle.py) : passed O(N^3)
  - Runtime: 1278 ms, faster than 7.04% of Python3 online submissions for Maximal Rectangle.
  - Memory Usage: 20.2 MB, less than 5.86% of Python3 online submissions for Maximal Rectangle.
- algorithm :
  - make matrix with 0 or 1 , 1's count until the end of 1' row , 1's count until the end of 1's column
  - for r for c -> get max rectangle with (r,c) --> get xsize and ysize of rectangle with 1
- BEST (got help) : O(N^2) histogram when we saw above specific row  : largest rectangle in histogram is O(N)
  - https://leetcode.com/problems/maximal-rectangle/discuss/1904690/illustrated-explanation
  - ![](https://assets.leetcode.com/users/images/0f9c1431-a088-4d22-b810-5abfd51f4630_1648848619.0584486.png)
  - [maximalRectangle2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maximalRectangle2.py) : passed O(N^2)
    - Runtime: 360 ms, faster than 57.59% of Python3 online submissions for Maximal Rectangle.
    - Memory Usage: 15.4 MB, less than 23.70% of Python3 online submissions for Maximal Rectangle.

# 92. Encode and Decode TinyURL (#535) - medium / python / 5M
- medium
- problem :
  - Note: This is a companion problem to the System Design problem: Design TinyURL.
  - TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
  - There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
  - Implement the Solution class:
    - Solution() Initializes the object of the system.
    - String encode(String longUrl) Returns a tiny URL for the given longUrl.
    - String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
- https://leetcode.com/problems/encode-and-decode-tinyurl/
- [TinyURL.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/TinyURL.py) : passed
  - Runtime: 48 ms, faster than 45.53% of Python3 online submissions for Encode and Decode TinyURL.
  - Memory Usage: 13.9 MB, less than 69.91% of Python3 online submissions for Encode and Decode TinyURL.

# 93. Design Underground System (#1396) - medium / python / c++ / 30M (caution : should be different between variables and funciton names)
- medium : map
- problem :
  - An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.
  - Implement the UndergroundSystem class:
    - void checkIn(int id, string stationName, int t)
      - A customer with a card ID equal to id, checks in at the station stationName at time t.
      - A customer can only be checked into one place at a time.
    - void checkOut(int id, string stationName, int t)
      - A customer with a card ID equal to id, checks out from the station stationName at time t.
    - double getAverageTime(string startStation, string endStation)
      - Returns the average time it takes to travel from startStation to endStation.
      - The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
      - The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
      - There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
  - You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
- https://leetcode.com/problems/design-underground-system/
- [UndergroundSystem.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/UndergroundSystem.py) : passed
  - Runtime: 268 ms, faster than 71.86% of Python3 online submissions for Design Underground System.
  - Memory Usage: 25.2 MB, less than 43.66% of Python3 online submissions for Design Underground System.
- [UndergroundSystem.cpp](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/UndergroundSystem.cpp) : passed
  - Runtime: 156 ms, faster than 82.84% of C++ online submissions for Design Underground System.
  - Memory Usage: 57.4 MB, less than 88.94% of C++ online submissions for Design Underground System.

# 94. Peeking Iterator (#284) - medium / python / c++ / 1H
- medium
- problem :
  - Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.
  - Implement the PeekingIterator class:
    - PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
    - int next() Returns the next element in the array and moves the pointer to the next element.
    - boolean hasNext() Returns true if there are still elements in the array.
    - int peek() Returns the next element in the array without moving the pointer.
  - Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.
- https://leetcode.com/problems/peeking-iterator/
- [PeekingIterator.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/PeekingIterator.py) : passed
  - Runtime: 40 ms , Your runtime beats 66.01 % of python3 submissions.
  - Memory Usage: 14.1 MB, Your memory usage beats 73.29 % of python3 submissions.
- [PeekingIterator.cpp](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/PeekingIterator.cpp) : passed
  - Runtime: 3 ms, faster than 79.17% of C++ online submissions for Peeking Iterator.
  - Memory Usage: 7.6 MB, less than 34.07% of C++ online submissions for Peeking Iterator.

# 95. Min Cost to Connect All Points (#1584) - medium / python / 3H
- medium
- problem :
  - You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
  - The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
  - Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
- https://leetcode.com/problems/min-cost-to-connect-all-points/
- [minCostConnectPoints.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minCostConnectPoints.py) : passed
  - Runtime: 1913 ms, faster than 69.45% of Python3 online submissions for Min Cost to Connect All Points.
  - Memory Usage: 80.9 MB, less than 75.10% of Python3 online submissions for Min Cost to Connect All Points.
- algorithm : 
  - input length 1000
    - 1.15.3. Kruskal's Algorithm : find minimum spanning tree
    - 1.15.4. Prim's Algorithm : find minimum spanning tree
  - sort by distance
  - put the same group if two vertices have edge.
  - use all hash to find faster whether it is in or not.
  - groupVertex[f] = v   f:vertext number , v : group number
  - group[v] has hash {from:to} ,  v : group number
  - if two vertices are in different groups , combine into one.  (delete group of [to])
- BEST : solution was opened. https://leetcode.com/problems/min-cost-to-connect-all-points/solution/

# 96. Minimum Window Substring (#76) - hard / python / 2D / (got help) : sliding window (left->right) / Top 100 Liked Questions
- hard
- problem :
  - Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
  - The testcases will be generated such that the answer is unique.
  - A substring is a contiguous sequence of characters within the string.
- https://leetcode.com/problems/minimum-window-substring/
- [minWindow.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minWindow.py) : 224 / 266 test cases passed. timeout
- [minWindow2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minWindow2.py) : passed (got help)
  - sliding window
    - Runtime: 251 ms, faster than 25.94% of Python3 online submissions for Minimum Window Substring.
    - Memory Usage: 18.3 MB, less than 5.05% of Python3 online submissions for Minimum Window Substring.
- BEST : sliding window
  - https://leetcode.com/problems/minimum-window-substring/solution/
  1. calculate left and right including target (target를 포함하는 left / right를 구한다.)
  2. left -> left+? until exists target. then right changes the position to include old removed chararcter of old left position.  (left를 한번 움직이면 , 기존에 있던 left위치의 문제가 없어지므로 , right에서 해당 문자를 추가하는 곳까지 가주어야 한다. )
  3. if removed left character does not filled with right position, old optiomizaed left/right is the answer. (right가 더 이상 갈게 없게 될때, left가 오른쪽으로 갈때 더이상 채워질 문자가 없어지게 될때, 그 전까지의 최적화된 것이 답)

# 97. Smallest String With Swaps (#1202) - medium / python / 2D / (got help) : grouping  
- medium
- problem :
  - You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
  - You can swap the characters at any pair of indices in the given pairs any number of times.
  - Return the lexicographically smallest string that s can be changed to after using the swaps.
- https://leetcode.com/problems/smallest-string-with-swaps/
- [smallestStringWithSwaps.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/smallestStringWithSwaps.py) : 5 / 36 test cases passed.
- [smallestStringWithSwaps2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/smallestStringWithSwaps2.py) : 35 / 36 test cases passed. timeout
  - (korean) 같이 연결된 것은 같은 group으로 해당 그룹안의 것은 sort된 것으로 처리 가능
  - the same group if they connected.   
  - disadvantage in my implementation. i guess it is the reason of timeout.
    - **union** : big slow
    - sort 2 times (char , index)
- [smallestStringWithSwaps3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/smallestStringWithSwaps3.py) : passed (got help)
  - union을 만들어 써야 함. parent를 찾아서 가는 방식을 사용해야 한다. 이것이 전체적으로 찾거나 하는 숫자의 차이가 있다. 
  - source smallestStringWithSwaps2.py 와 smallestStringWithSwaps3.py 을 비교할 것이다.  계산되는 횟수의 차이가 크다. 
  - This is fast code. 
    - n = 100000 total_time2 :  0.21922087669372559 c1:764287 c2:83863
  - ```python
        # Start of Union Find Data Structure
        p = list(range(len(s)))  # parent
        # each element in the pairs == node
        # used to store each node's parent based on its index
        # eg. pairs = [[0,3],[1,2]], p = [0, 1, 1, 0]
        # element 3 in pairs == p index 3 == 0 (because parent node of 3 is 0)

        def find(x):
            self.c1 += 1
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[py] = px
                self.c2 += 1
                
        # End of Union Find Data Structure

        # Grouping
        for x, y in pairs:
            union(x, y)
    ```
  - This is slow code : union and set with 'for' are slow
    - n = 100000 total_time2 :  35.675060510635376 c1:234347858 c2:21803
  - ```python
        for p in pairs:
            sg , eg = self.whichGroup(p[0]) , self.whichGroup(p[1])
            s,e = p[0],p[1]
            if sg == None and eg == None:
                self.group[s] = self.groupCount
                self.group[e] = self.groupCount
                self.groupList[self.groupCount] = {s,e}
                self.groupCount += 1
            elif sg == None:
                self.group[s] = self.group[e]
                self.groupList[self.group[e]].add(s)
            elif eg == None:
                self.group[e] = self.group[s]
                self.groupList[self.group[s]].add(e)
            else:
                if sg == eg:
                    pass
                else :
                    # union
                    t,f = self.group[s] , self.group[e]
                    for i in self.groupList[f]:
                        self.group[i] = t
                        c1 += 1
                    self.groupList[t] = self.groupList[t].union(self.groupList[f])
                    self.groupList[f].clear()
                    c2 += 1
    ```
- algorithm :
  - (korean) 같이 연결된 것은 같은 group으로 해당 그룹안의 것은 sort된 것으로 처리 가능.  group을 만들때 기본 set의 union을 사용하는 것보다 find / union을 만들어서 사용하는 방식이 훨씬 빠르다.

# 98. Path With Minimum Effort (#1631) - medium / python / 1D / (got help) : Dijkstra
- medium : (got help)
- problem :
  - You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
  - A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
  - Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
- https://leetcode.com/problems/path-with-minimum-effort/
- [minimumEffortPath.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumEffortPath.py) : 15 / 75 test cases passed.  Status: Time Limit Exceeded
  - 모든 내용이 확실히 풀릴 것으로 보이나 timeout
- [minimumEffortPath2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumEffortPath2.py) : fail 
  - need DP -> (n-1,n-1) -> (n-2,n-2) -> (n-3,n-3)
  - (n-1,n-1) 부터 위로 사각형을 만들어가며 , 최적의 숫자를 찾으려 했지만, 실제로 답이 예제 3번과 같이 사각형을 뚫고 나갔다 들어가는 경우는 해결이 안됨. 오히려 1번 푼 내용이 모든 내용이 맞음.
- [minimumEffortPath3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumEffortPath3.py) : passed (got help)
  - each room is vertex. difference between room's value is weight of edge.
  - 아래 BEST를 재구현을 해 봄.  아직 응용력이 부족함.
- BEST : https://leetcode.com/problems/path-with-minimum-effort/discuss/1989185/Dijkstra-Python-3
  - algorithm : Dijkstra (shortest weight path)
    1. start 에서 출발할때 각 노드까지 가는 가장 빠른 weight를 계산 
    2. start 에서 출발하여 edge가 작은 것부터 연결해가면서 q에 계속 넣어주면 결국 목적지에 도달하는 값이 나오게 된다. 이때 여기서는 weight 중 최대만을 찾는 것이므로 ,push시 weight를 넣었지만, path의 weight의 합일 경우에는 wegiht의 합으로 넣어서 계산을 하게 된다.
  - visit 한 것이면 처리하지 않는 이유는 이보다 큰 path를 처리를 할 필요가 없는데 , heapq를 사용하며 처리를 하므로 visit에는 항상 최소값이 들어가게 된다. 이중 while loop를 돌릴 필요가 없다.
    - weight의 합이 아니므로 , 딱 그 값만을 보고 결정하므로 이러헥 처리가 가능함.
```python
          while q:
            w,r,c = heapq.heappop(q)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if r == maxR-1 and c == maxC-1:
                return w
            for rp,cp in [(1,0),(0,1),(0,-1),(-1,0)]:
                nr,nc = r+rp , c+cp
                if 0 <= nr < maxR and 0 <= nc < maxC and (nr,nc) not in visit:
                    heapq.heappush(q,(max(w,self.diff([nr,nc],[r,c])),nr,nc))
```
# 99. Is Graph Bipartite? (#785) - medium / python / 3H / black&white
- medium
- problem :
  - There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
    - There are no self-edges (graph[u] does not contain u).
    - There are no parallel edges (graph[u] does not contain duplicate values).
    - If v is in graph[u], then u is in graph[v] (the graph is undirected).
    - The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
  - A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
  - Return true if and only if it is bipartite.
- https://leetcode.com/problems/is-graph-bipartite/
- [isBipartite.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/isBipartite.py) : passed
  - Runtime: 263 ms, faster than 39.11% of Python3 online submissions for Is Graph Bipartite?.
  - Memory Usage: 14.4 MB, less than 50.28% of Python3 online submissions for Is Graph Bipartite?.
- algorithm : black & white like othello game

# 100. Evaluate Division(#399) - medium / python / 3H / grouping : find&union
- medium
- problem :
  - you are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
  - You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
  - Return the answers to all queries. If a single answer cannot be determined, return -1.0.
  - Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
- https://leetcode.com/problems/evaluate-division/
- [calcEquation.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/calcEquation.py) : passed
  - Runtime: 52 ms, faster than 28.73% of Python3 online submissions for Evaluate Division.
  - Memory Usage: 14 MB, less than 16.96% of Python3 online submissions for Evaluate Division.
- algorithm : grouping
  - make a group
  - calculate each variables of each group
  - can not calculae when each variables not in same group.  return -1.0

# 101. Sliding Window Maximum (#239) - hard / python / sliding : left->right : deque / Top 100 Liked Questions (got help) 
- hard
- problem :
  - You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
  - Return the max sliding window.
- https://leetcode.com/problems/sliding-window-maximum/
- [maxSlidingWindow.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxSlidingWindow.py) : 58 / 61 test cases passed.  timeout  O(N^2)
  - 40000 total_time1 : 2.07 seconds
- [maxSlidingWindow2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxSlidingWindow2.py) : (got help)   O(N)
  - 40000 total_time1 : 0.01 seconds
    - Runtime: 2183 ms, faster than 59.64% of Python3 online submissions for Sliding Window Maximum.
    - Memory Usage: 29.7 MB, less than 79.71% of Python3 online submissions for Sliding Window Maximum.
- algorithm : 
  - keep sorted list but not sorted all.
  - first of all, find max. sorted sky line of histogram.
  - sliding의 경우는 left , right로 처리하면 잘된다.
    -  part1 : 0 .. k-1 : find max and sorted stack
    -  part2 : 0 .. len()-k+1 -> k-1 ~ len()
       -  if i > index of max -> pop of max
       -  pop while sorted_stack is less than added value
       -  push added value in sorted_stack 

# 102. hiking - hard / python / dijkstra / 1D / SW_TEST 
- hard : [1.14.1. dijkstra](#1141-dijkstra)
- problem :
  - n×n의 행렬로 지형도가 표시된 산이 있다. 행렬의 원소의 값은 양의 정수 값으로 그 위치에서의 높이를 말해준다.등산가들은 산의 바깥지역(높이 0)으로부터 목적지에 도달하기 위하여 가장 경제적인 루트를 탐색하려고 한다. 경제적인 경로란 힘을 가장 적게 들이고 목적지까지 올라갈 수 있는 길을 말한다.
  - 예를 보면서 설명해보자. 다음은 행렬 Mount[5,5]로 표시된 산악지형이다. 산의 목적지는 Mount[3,3]의 위치에 있으며, 그 높이는 6이다. 그리고 이 산의 바깥지역은 모두 해발이 0이다. 등산가가 산에 오르는 시작점의 위치는 산의 바깥지역의 어디에서 시작해도 좋다.
  - 등산가는 어떤 한 지역에서 그 위치에 인접한 네 방향(위, 아래, 왼쪽, 오른쪽)으로만 움직일 수 있다. 인접한 지역으로 움직일 수 있는 경우는 (1) 평지로 이동할 경우, (2) 내려갈 경우, (3) 올라갈 경우의 세 가지이다. 이 세 가지 경우에 필요한 "힘"의 양은 다음과 같이 표현될 수 있다.
    - (1)인접한 같은 높이의 지역을 수평 이동할 경우에는 그냥 평지를 걸어가면 되므로 힘이 전혀 들지 않는다고 가정한다. 예를 들면 Mount[5,2]에서 Mount[5,3]으로 이동하는 경우와 Mount[4,5]에서 Mount[5,5]로 이동하는 경우에는 전혀 힘이 들지 않는다.
    - (2)내리막길을 따라갈 경우(예를 들면, Mount[2,3]에서 Mount[2,2]로 갈 때)에는 그 높이 차이만큼의 힘이 든다. 즉 이 경우에는 5-3=2만큼의 힘이 든다.
    - (3)오르막길을 오를 경우에는 이동할 두 지역의 높이 차의 제곱만큼의 힘이 든다. 즉 Mount[1,2]에서 Mount[1,3]으로 갈 경우는 (4-2)2=4 만큼의 힘이 든다.
  - Input
    - 첫째 줄에는 산의 크기인 Mount[n,n]의 n값이 주어지고, 두 번째 줄에는 목적지의 위치 Mount[y,x]의 y, x값이 주어진다.
    - 단, Mount[n,n]에서 n은 100이하이고, 각 지형의 최대 높이는 50이하라고 가정한다.
    - 그 다음 n개의 줄은 산의 크기에 따른 각 지점의 높이가 양의 정수 값으로 주어진다.
  - Output
    - 첫째 줄에 목적지까지 도달하는 가장 경제적인 경로를 따라 올라가는데 사용된 힘을 출력한다.
- http://collab.lge.com/main/pages/viewpage.action?pageId=1629825838
- [hiking_Dijkstra.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/hiking_Dijkstra.py) : passed  (only 2 example in codes)
  - (방안1) 가능하면 더 많은 것을 넣은후에 비교하도록 ...  더 많은 것에서 최소를 찾게 ...  
- [hiking_Dijkstra2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/hiking_Dijkstra2.py) : passed  (all cases)
  - (방안2) Dijkstra로 풀었음. 둘레로 0을 넣어서 푸는 것도 가능하나, 이러면 edges수가 증가하므로 , 둘레는 붙이지 않고 푼다. 
    - 둘레를 붙이지 않고 푸는 대신, 마지막에 0 인 바닥에서 각 칸으로 올라갈때의 값을 더해주어야 한다.  (+차이**2)
  - 방안 1에서 특별 case들에 대해서 infinite loop를 도는 것은 if result[node] <= w: continue를 할때 <=  대신 <  을 사용했기 때문이다.  같을때도 다시 확장할 필요가 없다. 
  - 앞으로 optimization이 가능한 부분
    - q , nextQ로 하는 것을 하나로 합치기
    - heappush 하기 전에 먼저 check해서 아예 heap도 넣지 않게 하는 것
    - 같은 코드들은 변수에 대입시켜 사용하므로 실제 계산 횟수를 줄이기
```python
    def dijkstra(self,row : int , col : int , graph:Dict[Tuple[int,int],int],startNode:int) -> List[int]: # n : nodecount , graph[(x,y)] = (w,x1,y1) , from : (x,y)
        result = [math.inf for _ in range(row*col)]
        q = [(0,startNode)]
        while q:
            nextQ = []
            while q:
                w,node = heapq.heappop(q)
                if result[node] <= w:
                    continue
                result[node] = w
                # north : node - col , south : node + col , west : node - 1 , east : node + 1
                if node-col >= 0 :
                    heapq.heappush(nextQ,(w+graph[(node,node-col)],node-col))
                if node+col < row*col :
                    heapq.heappush(nextQ,(w+graph[(node,node+col)],node+col))
                if node%col != 0 :
                    heapq.heappush(nextQ,(w+graph[(node,node-1)],node-1))
                if node%col != col-1 :
                    heapq.heappush(nextQ,(w+graph[(node,node+1)],node+1))
            q = nextQ
```

# 103. Binary Tree Maximum Path Sum (#124) - hard / python / 3H / tree : dfs : left,right,root,leftroot,rightroot,leftrootright / Top 100 Liked Questions
- hard : tree
- problem :
  - A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
  - The path sum of a path is the sum of the node's values in the path.
  - Given the root of a binary tree, return the maximum path sum of any non-empty path.
  - ![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)
    - Input: root = [-10,9,20,null,null,15,7]
    - Output: 42
    - Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
- https://leetcode.com/problems/binary-tree-maximum-path-sum/
- [maxPathSum.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxPathSum.py) : passed  (tree traverse : DFS)
  - Runtime: 159 ms, faster than 17.42% of Python3 online submissions for Binary Tree Maximum Path Sum.
  - Memory Usage: 26.7 MB, less than 5.28% of Python3 online submissions for Binary Tree Maximum Path Sum.

# 104. Find Median from Data Stream (#295) - hard / python / 2H / bisect / Top 100 Liked Questions
- hard : bisect
- problem :
  - The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
    - For example, for arr = [2,3,4], the median is 3.
    - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
  - Implement the MedianFinder class:
    - MedianFinder() initializes the MedianFinder object.
    - void addNum(int num) adds the integer num from the data stream to the data structure.
    - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
- https://leetcode.com/problems/find-median-from-data-stream/
- [MedianFinder.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/MedianFinder.py) : passed
  - Runtime: 2025 ms, faster than 12.13% of Python3 online submissions for Find Median from Data Stream.
  - Memory Usage: 35.9 MB, less than 75.03% of Python3 online submissions for Find Median from Data Stream.

# 105. Shortest Unsorted Continuous Subarray (#581) - medium / python / 1H 
- medium 
- problem :
  - Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
  - Return the shortest such subarray and output its length.
- https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
- [findUnsortedSubarray.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findUnsortedSubarray.py) : passed
  - Runtime: 247 ms, faster than 67.57% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
  - Memory Usage: 15.3 MB, less than 54.83% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
- algorithm :
  - find minimum value (mn) after starting down from 0 index
  - find index (startIndex) for this minimum value from starting position
  - find maximum value (mx) after starting up from last index
  - find index (lastIndex) for this maximum value from last position
  - calculate difference between startIndex and lastIndex (lastIndex - startIndex + 1)

# 106. Max Number of K-Sum Pairs (#1679) - medium / python / 1H
- medium
- problem :
  - You are given an integer array nums and an integer k.
  - In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
  - Return the maximum number of operations you can perform on the array.
- https://leetcode.com/problems/max-number-of-k-sum-pairs/
- [maxOperations.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/maxOperations.py) : passed
  - Runtime: 971 ms, faster than 29.02% of Python3 online submissions for Max Number of K-Sum Pairs.
  - Memory Usage: 27.1 MB, less than 54.91% of Python3 online submissions for Max Number of K-Sum Pairs.

# 107. Wildcard Matching (#44) - hard / python / 1D / Top Interview Questions
- hard 
- problem:
  - Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
    - '?' Matches any single character.
    - '*' Matches any sequence of characters (including the empty sequence).
  - The matching should cover the entire input string (not partial).
- https://leetcode.com/problems/wildcard-matching/
- [wildcardMatching.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/wildcardMatching.py) : 
1725 / 1811 test cases passed.
- [wildcardMatching2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/wildcardMatching2.py) : passed
  - Runtime: 517 ms, faster than 77.45% of Python3 online submissions for Wildcard Matching.
  - Memory Usage: 14.4 MB, less than 79.48% of Python3 online submissions for Wildcard Matching.
- algorithm :
  - first of all , you reduce the problem.  이것을 안하고 했더니 뒤에서 더 많은 처리를 해야한다.  맞는 것을 일단 없애고 처리하자.
    - if you reduce the string and pattern , it is not complicated
  - if pattern has more than one asterrisk
  - if one of both directions is satisfied , it is True.
    - check whether this charter is in * or not.

# 108. Remove All Adjacent Duplicates in String II (#1209) - medium / python / 2H
- medium 
- problem :
  - You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
  - We repeatedly make k duplicate removals on s until we no longer can.
  - Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
  - ```
      Input: s = "deeedbbcccbdaa", k = 3
      Output: "aa"
      Explanation: 
      First delete "eee" and "ccc", get "ddbbbdaa"
      Then delete "bbb", get "dddaa"
      Finally delete "ddd", get "aa"
    ```
- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
- [removeDuplicates1209.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/removeDuplicates1209.py) : passed O(N)
  - Runtime: 566 ms, faster than 7.63% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
  - Memory Usage: 24.2 MB, less than 9.09% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
- algorithm : O(N)
  - make a list with length stack = [ ['a',3], ...]
  - scan and change it :
    - if length is more than k , remove it.
    - if i-1 and i 's character are same , combine it
- BEST : (got help) https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/2012330/python-3-oror-simple-stack-solution-oror-O(n)O(n)
```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                if stack[-1][1] == k - 1: 
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])
        return ''.join(c * count for c, count in stack)
```

# 109. 132 Pattern (#456) - medium / python / 1D (got help)
- medium
- problem :
  - Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
  - Return true if there is a 132 pattern in nums, otherwise, return false.
  - ```
      Input: nums = [-1,3,2,0]
      Output: true
      Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
    ```
- https://leetcode.com/problems/132-pattern/
- [find132pattern.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/find132pattern.py) : 100 / 102 test cases passed.
- [find132pattern-2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/find132pattern-2.py) : 101 / 102 test cases passed.
- [find132pattern-3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/find132pattern-3.py) : passe (got help)
  - Runtime: 497 ms, faster than 41.75% of Python3 online submissions for 132 Pattern.
  - Memory Usage: 35.3 MB, less than 5.61% of Python3 online submissions for 132 Pattern.
- algorithm : [79. Largest Rectangle in Histogram (#84) - hard / python / 2D](#79-largest-rectangle-in-histogram-84---hard--python--2d)
  - k 중심으로 생각해서 , 왼쪽의 최소값을 구한다. (이 최소값은 k보다는 커야 한다.) 오른쪽의 최대값을 구한다. (이 최대값은 왼쪽의 최소값보다는 커야 한다.)
  - left , right 값을 구한다. 
  - 연속 동일한 숫자 삭제
  - left[] : O(N)
  - right[] : O(N^2)  <- how to reduce it.
    - right[] : O(N) using stack
  - process [i] : left[i] -> nums[i] -> pop when stack[-1] is less than left[i] -> right[i] -> add nums[i] into stack 
    - ```python
        left = [math.inf for _ in range(len(nums))]
        right = [-math.inf for _ in range(len(nums))]
        mn = math.inf
        for i in range(len(nums)):
            left[i] = mn
            mn = min(mn,nums[i])
        stack = []
        for i in reversed(range(1,len(nums))):
            while stack and stack[-1] <= left[i]:
                stack.pop()
            if stack :
                right[i] = stack[-1]
            stack.append(nums[i])
        for i in range(len(nums)):
            if left[i] < nums[i] and left[i] < right[i] and nums[i] > right[i]:
                return True
        return False
      ```

        | [0]  | [1] | [2] | [3] | [4] | [5]  | [6]  | [7]   | index       |
        | ---- | --- | --- | --- | --- | ---- | ---- | ----- | -----------:|
        | inf  | 4   | 3   | 3   | 3   | 3    | 3    | 2     | -> left     |
        | 4    | 3   | 4   | 5   | 6   | 5    | 2    | 3<- > | nums        |
        | all  | 4   | x   | x   | x   | 2    | 3    | x     | <- pop      |
        | -inf | 5   | 5   | 6   | 5   | -inf | -inf | -inf  | <- right    |
        |      | 3   | 4   |     |     |      |      |       | stack[3]    |
        |      | 5   | 5   | 5   |     |      |      |       | stack[2]    |
        |      | 6   | 6   | 6   | 6   |      |      |       | stack[1]    |
        | 4    | 5   | 5   | 5   | 5   | 5    | 2    | 3     | <- stack[0] |
- BEST :
  - https://leetcode.com/problems/132-pattern/discuss/2015969/Python-Solution-using-stack
  - https://leetcode.com/problems/132-pattern/discuss/2015130/Going-from-O(N3)-greater-O(N2)-greater-O(N)-%2B-MEME
    - O(N)   (got hlep)  get right[] ==>  popped until stack[-1] > left[i] , right[i] = stack[-1] , then append nums[i] into stack to go next

# 110. Flatten Nested List Iterator (#341) - medium / python / 2H
- medium
- problem :
  - You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
  - Implement the NestedIterator class:
    - NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    - int next() Returns the next integer in the nested list.
    - boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
  - Your code will be tested with the following pseudocode:
    - initialize iterator with nestedList
    - res = []
    - while iterator.hasNext()
    -     append iterator.next() to the end of res
    - return res
  - If res matches the expected flattened list, then your code will be judged as correct.
  - ```
      Input: nestedList = [[1,2],3,[4,5]]
      Output: [1,2,3,4,5]
      Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5].
    ```
- https://leetcode.com/problems/flatten-nested-list-iterator/submissions/
- [NestedInteger.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/NestedInteger.py) : passed
  - Runtime: 115 ms, faster than 21.00% of Python3 online submissions for Flatten Nested List Iterator.
  - Memory Usage: 17.9 MB, less than 41.16% of Python3 online submissions for Flatten Nested List Iterator.

# 111. Letter Combinations of a Phone Number (#17) - medium / python / 1H
- medium
- problem :
  - Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
  - A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
  - ```
        self.table = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']
    ```
- https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- [letterCombinations.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/letterCombinations.py) : passed
  - Runtime: 37 ms, faster than 67.10% of Python3 online submissions for Letter Combinations of a Phone Number.
  - Memory Usage: 13.9 MB, less than 79.68% of Python3 online submissions for Letter Combinations of a Phone Number.
- next challenges : Generate Parentheses / Combination Sum / Binary Watch / Count Number of Texts

# 112. Word Ladder (#127) - hard / python / 3D / BFS / Top Interview Questions / (got help) / (fail)
- hard
- problem :
  - A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    - Every adjacent pair of words differs by a single letter.
    - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    - sk == endWord
  - Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
  - ```
      Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
      Output: 5
      Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    ```
- https://leetcode.com/problems/word-ladder/
- [ladderLength.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/ladderLength.py) : 36 / 50 test cases passed. timeout
  - Runtime: 1456 ms  <- 2370 items  with "passed" in "Run Code" 
  - 2370  tcount: 4273   **table :  1.4275891780853271** ->  while :  0.00419926643371582 ->  **total_time1 :  1.4318492412567139** -> SUCCESS -> 21 1757 catch
    - makeDiffTable() spent most of time. it was timeout because of it. we should reduce the time.
    - methods : 
      - In this case we calculate edges between all words. Then we calculate shortest path.
      - but , we do not need to search all cases. if you reach to target, we can stop it.
      - so combine search and makeDiffTable with BFS.
- [ladderLength_2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/ladderLength_2.py) : timeout
  - It took more time. it is useless.
  - 2370 table :  2.384185791015625e-07 ->  while :  3967 2.0570247173309326 ->  **total_time1 :  2.0571084022521973** -> SUCCESS -> 21 0 catch
- [ladderLength_best.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/ladderLength_best.py) : (got help)
  - string 을 비교하는 것에서 시간이 많이 소모된다.  diff count를 줄이고 , diff하는 시간을 줄이는 것이 관건!
    - ladderLength.py : 4273 q.append , 2807265 diff
    - ladderLength_2.py : 3967 q.append , 4119060 diff
  - 더 빠르게 diff하는 방법이 뭘까? (got help)  [discussion](https://leetcode.com/problems/word-ladder/discuss/1767680/Python-3-or-Faster-than-93-or-BFS-solution-orEasy-to-understand)
    - hot 라고 하면 h_t 라고 쓰고 , **nei{h_t , [hot,...]}**
    - 해당 문자에 대해서 hot 라고 하면 _ot , h_t , ho_ 으로 변경되는  word들을 가질 수 있으며,
    - _ot 에 해당되는 word들을 q에 넣어서 한칸 더 가라는 것이다. 
    - diff 를 해서 찾을수 있는 것을 바로 찾을수 있다. 
    - q.append : 1745 ,  neiCount : 11855
- [ladderLength_3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/ladderLength_3.py) : passed
  - Runtime: 300 ms, faster than 52.38% of Python3 online submissions for Word Ladder.
  - Memory Usage: 20.2 MB, less than 5.17% of Python3 online submissions for Word Ladder.
  - diff:11850 q:16548
- algorithm :
  - _를 중간에 넣어서 특정 word에서 변경될수 있는 모든 word를 찾는 것을 한번에 할수 있는 data structure를 생성한다.
- next challenges : Hash Table / String / Breadth-First Search

# 113. Count Sorted Vowel Strings (#1641) - medium / python / 1H
- medium
- problem :
  - Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
  - A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
  - ```
      Input: n = 2
      Output: 15
      Explanation: The 15 sorted strings that consist of vowels only are
      ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
      Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
    ```
- https://leetcode.com/problems/count-sorted-vowel-strings/
- [countVowelStrings.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/countVowelStrings.py) : passed
  - Runtime: 39 ms, faster than 64.17% of Python3 online submissions for Count Sorted Vowel Strings.
  - Memory Usage: 13.8 MB, less than 65.31% of Python3 online submissions for Count Sorted Vowel Strings.
- algorithm :
  - f1 : a , f2 : e , f3 : e  , f4 : o , f5 : u
  - ```
        f1(1) = 1
        f1(n) = 1
        f2(1) = 2
        f2(n) = f2(n-1) + f1(n-1)
        f3(n) = f3(n-1) + f2(n-1) + f1(n-1)
        f5(n) = f5(n-1) + f4(n-1) + f3(n-1) + f2(n-1) + f1(n-1)
        n = 1 => a:1 + e:1 + i:1 + o:1 + u:1
        n = 2 => a:5 + e:4 + i:3 + o:2 + u:1 => a:f5(1) + e:f4(1) + i:f3(1) + o:f2(1) + u:f1(1)
        n = 3 => a:f5(2) + e:f4(2) + i:f3(2) + o:f2(2) + u:f1(2)
    ```
- next challenges : Dynamic Programming

# 114. Combination Sum III (#216) - medium / python / 1H
- medium
- problem :
  - Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    - Only numbers 1 through 9 are used.
    - Each number is used at most once.
  - Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
  - ```
      Input: k = 3, n = 9
      Output: [[1,2,6],[1,3,5],[2,3,4]]
      Input: k = 4, n = 1
      Output: []
    ```
- https://leetcode.com/problems/combination-sum-iii/
- [combinationSum3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/combinationSum3.py) : passed
  - Runtime: 50 ms, faster than 35.44% of Python3 online submissions for Combination Sum III.
  - Memory Usage: 13.9 MB, less than 79.02% of Python3 online submissions for Combination Sum III.
- next challenges : Combination Sum

# 115. Longest Increasing Path in a Matrix (#329) - hard / python / 2H / dynamic programming / Top Interview Questions
- hard
- problem : 
  - Given an m x n integers matrix, return the length of the longest increasing path in matrix.
  - From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
- https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
- [longestIncreasingPath.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/longestIncreasingPath.py) : passed
  - Runtime: 514 ms, faster than 73.78% of Python3 online submissions for Longest Increasing Path in a Matrix.
  - Memory Usage: 14.7 MB, less than 86.30% of Python3 online submissions for Longest Increasing Path in a Matrix.
- algorithm : dynamic programming
  - Directed Graph (no infinite loop)
  - DFS traverse (recursive max depth in related to stack size : m*n)
- next challenges : Count Ways to Build Rooms in an Ant Colony / Minimum Number of Days to Eat N Oranges / Maximum Cost of Trip With K Highways

# 116. Permutations II (#47) - medium / python / 30M
- medium
- problem :
  - Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
  - ```
      Input: nums = [1,2,3]
      Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    ```
- https://leetcode.com/problems/permutations-ii/
- [permuteUnique.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/permuteUnique.py) :
  - Runtime: 132 ms, faster than 28.83% of Python3 online submissions for Permutations II.
  - Memory Usage: 14.2 MB, less than 60.03% of Python3 online submissions for Permutations II.
- next challenges : Permutations / Palindrome Permutation II / Number of Squareful Arrays

# 117. Populating Next Right Pointers in Each Node II (#117) - medium / python / BFS / find sibling node / 20M
- medium
- problem :
  - Given a binary tree
  - ```
      struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
      }
    ```
  - Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
  - Initially, all next pointers are set to NULL.
  - Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
- https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
- [connect.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/connect.py) : passed
  - Runtime: 57 ms, faster than 68.35% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
  - Memory Usage: 15.4 MB, less than 48.93% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
- algorithm : BFS / find sibling node 
- next challenges : Populating Next Right Pointers in Each Node

# 118. Daily Temperatures (#739) - medium / python / stack / 15M / Top 100 Liked Questions
- medium
- problem :
  - Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
  - ```
      Input: temperatures = [73,74,75,71,69,72,76,73]
      Output: [1,1,4,2,1,1,0,0]
      Input: temperatures = [30,40,50,60]
      Output: [1,1,1,0]
    ```
- https://leetcode.com/problems/daily-temperatures/
- [dailyTemperatures.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/dailyTemperatures.py) : passed
  - Runtime: 1348 ms, faster than 67.45% of Python3 online submissions for Daily Temperatures.
  - Memory Usage: 25.4 MB, less than 23.98% of Python3 online submissions for Daily Temperatures.
- algorithm : stack
- complexity : O(N)
- next challenges : Next Greater Element I /  Online Stock Span

# 119. Subarray Sum Equals K (#560) - medium / python / Top 100 Liked Questions / (got help)
- medium
- problem :
  - Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
  - ```
      Input: nums = [1,1,1], k = 2
      Output: 2
      Input: nums = [1,2,3], k = 3
      Output: 2
    ```
- [subarraySum.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/subarraySum.py) : 72 / 90 test cases passed.  timeout O(N^2)
  - **20000** total_time1 :  **19.059290885925293** -> SUCCESS -> 4012 200010000
- [subarraySum_2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/subarraySum_2.py) : (got help)  O(N)
  - https://leetcode.com/problems/subarray-sum-equals-k/discuss/1761064/C%2B%2B-Solution-oror-Code-%2B-Explanation
  - prefixSum[i] 는 i 까지의 합을 미리 계산한다.
  - i 부터 이후의 값 어디까지인가까자의 합이 k가 되어야 한다. prefixSum을 이용하는 경우는 i-1까지의 합 + k 가 되는 값이 i 이후에 있는지를 보면 된다.
  - **20000** total_time1 :  **0.010038614273071289** -> SUCCESS -> 4012 0
    - Runtime: 297 ms, faster than 62.84% of Python3 online submissions for Subarray Sum Equals K.
    - Memory Usage: 16.7 MB, less than 32.85% of Python3 online submissions for Subarray Sum Equals K.
- algorithm :
  - O(N) : prefixSum[i] 는 i 까지의 합을 미리 계산한다. i 부터 이후의 값 어디까지인가까자의 합이 k가 되어야 한다. prefixSum을 이용하는 경우는 i-1까지의 합 + k 가 되는 값이 i 이후에 있는지를 보면 된다.
- complexity : O(N^2) -> O(N)
- next challenges : Continuous Subarray Sum  / Subarray Product Less Than K / Find Pivot Index / Subarray Sums Divisible by K / Minimum Operations to Reduce X to Zero / K Radius Subarray Averages / Maximum Sum Score of Array

# 120. Network Delay Time (#743) - medium / python / graph / dijkstra 
- medium
- problem :
  - You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
  - We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
  - ```
      Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
      Output: 2
      Input: times = [[1,2,1]], n = 2, k = 2
      Output: -1
    ```
- [networkDelayTime.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/networkDelayTime.py) : passed
  - Runtime: 659 ms, faster than 38.98% of Python3 online submissions for Network Delay Time.
  - Memory Usage: 16 MB, less than 92.16% of Python3 online submissions for Network Delay Time.
- algorithm : graph / dijkstra 
- BEST : it has the same algorithm with the solution of best performance.
- complexity : O(N + ELogN) -Standard Time complexity of Dijkstra's algorithm
- next challenges : The Time When the Network Becomes Idle / Second Minimum Time to Reach Destination

# 121. Deepest Leaves Sum (#1302) - medium / python / dfs / tree traverse / 20M
- medium
- problem :
  - Given the root of a binary tree, return the sum of values of its deepest leaves.
  - ```
      Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
      Output: 15
      Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
      Output: 19
    ```
- https://leetcode.com/problems/deepest-leaves-sum/
- [deepestLeavesSum.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/deepestLeavesSum.py) : passed
  - Runtime: 237 ms, faster than 76.76% of Python3 online submissions for Deepest Leaves Sum.
  - Memory Usage: 17.7 MB, less than 66.46% of Python3 online submissions for Deepest Leaves Sum.
- algorithm : dfs / tree traverse
- complexity : O(N)
- next challenges : Maximum Width of Binary Tree / Sentence Similarity II / Time Needed to Inform All Employees

# 122. Shortest Path in Binary Matrix (#1091) - medium / python /  bfs / 1D
- medium
- problem :
  - Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
  - A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
  - The length of a clear path is the number of visited cells of this path.
  - ```
      Input: grid = [[0,1],[1,0]]
      Output: 2
      Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
      Output: 4
      Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
      Output: -1
    ```
- https://leetcode.com/problems/shortest-path-in-binary-matrix/
- [shortestPathBinaryMatrix.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathBinaryMatrix.py) : dfs 64 / 88 test cases passed. timeout
- [shortestPathBinaryMatrix_2.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/shortestPathBinaryMatrix_2.py) : bfs passed
  - Runtime: 726 ms, faster than 68.46% of Python3 online submissions for Shortest Path in Binary Matrix.
  - Memory Usage: 14.4 MB, less than 57.79% of Python3 online submissions for Shortest Path in Binary Matrix.
  - different while loop count : 88 vs 24 in case of ```[[0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0]]```
    - q에 넣으면서 visit도 check해주는게 가장 빠르다. 이미 넣었으므로 방문한 것으로 간주
  - ```
        q = [(1,sr,sc)]
        while q : 
            pc,sr,sc = q.pop(0)
            visit[sr][sc] = 1
            if sr == tr and sc == tc:        return pc
            for r in self.di:     for c in self.di: 
                    if r != 0 or c != 0:  if g[sr+r][sc+c] == 0 and visit[sr+r][sc+c] == math.inf:
                            q.append((pc+1,sr+r,sc+c))
    ```
  - ```
        q = [(1,sr,sc)]
        visit[sr][sc] = 1
        while q : 
            pc,sr,sc = q.pop(0)
            if sr == tr and sc == tc:        return pc
            for r in self.di:     for c in self.di: 
                    if r != 0 or c != 0:  if g[sr+r][sc+c] == 0 and visit[sr+r][sc+c] == math.inf:
                            visit[sr+r][sc+c] = 1
                            q.append((pc+1,sr+r,sc+c))
    ```
- algorithm : bfs
- complexity : O(BOX) = O(N**2)
- next challenges : Strobogrammatic Number II / Trapping Rain Water II / Web Crawler Multithreaded

# 123. Target Sum (#494) - medium / python / dp / Top 100 Liked Questions / 45M
- medium
- problem :
  - ou are given an integer array nums and an integer target.
  - You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    - For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
  - Return the number of different expressions that you can build, which evaluates to target.
  - ```
        Input: nums = [1,1,1,1,1], target = 3
        Output: 5
        Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
        -1 + 1 + 1 + 1 + 1 = 3
        +1 - 1 + 1 + 1 + 1 = 3
        +1 + 1 - 1 + 1 + 1 = 3
        +1 + 1 + 1 - 1 + 1 = 3
        +1 + 1 + 1 + 1 - 1 = 3
    ```
- https://leetcode.com/problems/target-sum/
- [findTargetSumWays.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/findTargetSumWays.py) : passed
  - Runtime: 798 ms, faster than 9.48% of Python3 online submissions for Target Sum.
  - Memory Usage: 15 MB, less than 53.89% of Python3 online submissions for Target Sum.
- algorithm : dynamic programming
- complexity : O(2**N)
- next challenges : Expression Add Operators

# 124. Critical Connections in a Network (#1192) - hard / python / graph / loop / (ing)
- hard
- problem :
  - There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
  - A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
  - Return all critical connections in the network in any order.
  - ```
      Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
      Output: [[1,3]]
      Explanation: [[3,1]] is also accepted.
    ```
- https://leetcode.com/problems/critical-connections-in-a-network/
- [criticalConnections.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/criticalConnections.py) : 9 / 17 test cases passed. timeout
  - 한개의 edge를 빼고 처리했을때 , 그 edge의 양 node가 같은 group에 있는지로 판별
  - node : 1000 , edge : 55787 -> timeout  O(E * E * N)
- algorithm : graph and loop and grouping problem
  - if this edge connects two different group , this is critial edge.
  - and consider with one node as group
- complexity :
- next challenges : 

# 125. Unique Paths II (#63) - medium / python / dfs / dp / 5H
- medium
- problem :
  - You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
  - An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
  - Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
  - The testcases are generated so that the answer will be less than or equal to 2 * 109.
  - ```
      Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
      Output: 2
      Explanation: There is one obstacle in the middle of the 3x3 grid above.
      There are two ways to reach the bottom-right corner:
      1. Right -> Right -> Down -> Down
      2. Down -> Down -> Right -> Right
    ```
- https://leetcode.com/problems/unique-paths-ii/
- [uniquePathsWithObstacles.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/uniquePathsWithObstacles.py) : passed
  - Runtime: 74 ms, faster than 22.35% of Python3 online submissions for Unique Paths II.
  - Memory Usage: 13.9 MB, less than 74.88% of Python3 online submissions for Unique Paths II.
- algorithm : dfs / dp 
  - if remove unreachable mark , it takes more time. 74 ms -> 464ms (remove self.u)
  - dp : v -> visited (do you have how many path from here to target)
    - M:3,N:4 -> v[1][1] includes the path count from (1,1) to (2,3)
- complexity : O(M*N)
- next challenges : Unique Paths / Unique Paths III














# 126. template (#) - medium / python / (ing)
- medium
- problem :
  - 
  - ```

    ```
- 
- [combinationSum3.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/combinationSum3.py) :
  - 
- algorithm :
- complexity :
- next challenges : 






