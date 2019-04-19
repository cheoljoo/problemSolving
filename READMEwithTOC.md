
Table of Contents
=================

   * [no0001.pl](#no0001pl)
   * [no0003.py](#no0003py)
   * [4 GALLERY](#4-gallery)
   * [5](#5)
   * [6 : Joined Longest Increasing Subsequence](#6--joined-longest-increasing-subsequence)
   * [7 : Longest Increasing Sequence](#7--longest-increasing-sequence)
   * [8 : K-th Longest Increasing Sequence](#8--k-th-longest-increasing-sequence)
   * [9 : D Tree](#9--d-tree)
   * [10 : Elivator](#10--elivator)
   * [11 : 조세퍼스 순열](#11--조세퍼스-순열)
   * [12 :  배낭 챙기기 1](#12---배낭-챙기기-1)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)



# no0001.pl
- https://www.algospot.com/judge/problem/read/BOOKSTORE
- perl no0001.pl < no0001.data


# no0003.py
- http://collab.lge.com/main/pages/viewpage.action?pageId=930044529
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1835&sca=3080
- python3 no0003.py < no0003.data
  - python tree program source
  - The result is timeout
- make 3cpp
    - std::ios_base::sync_with_stdio(false);
    - use global variable (no initilization)
- result : fail (timeout)

# 4 GALLERY
- https://algospot.com/judge/problem/read/GALLERY#
- 4.cpp : for debugging
- 4r.cpp : release
- 4rd.cpp : for debugging
- #4 is different from #3.
    - #4 can have the following case.     E - X - X - E
- result : fail
- Solution : 4r_goh.c  4r_lsh.cpp

# 5
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=540&sca=30a0
- 5.cpp : success with 2 sample
	- but, it is timeout and not solved.
	- I do not know what do I choose when I have multiple index with the maximum cross lines.
	- 5r2.cpp : find the proper index among the index with the same cross.
		- 5.data / 5.data2 / 5.data3 is ok. But , data6 is not ok.  case count is 400


# 6 : Joined Longest Increasing Subsequence
- https://algospot.com/judge/problem/read/JLIS
	- JLIS, Joined Longest Increasing Subsequence
	- Find all kinds of IS
	- First of all , I need KLIS. (kth-LIS)
- 6r.cpp   : site answer fail


# 7 : Longest Increasing Sequence
- https://algospot.com/judge/problem/read/LIS
- 7.cpp : site answer : runtime error but I do not understand. change the MAX into 500
	- ok

# 8 : K-th Longest Increasing Sequence
- https://algospot.com/judge/problem/read/KLIS
- 8.cpp  : based on 7.cpp
	- MAX*130 : memory limit exceed
	- MAX*120 : RTE (SIGSEGV: segmentation fault, probably incorrect memory access or stack overflow)
- 8moreC.cpp : based on 8.cpp
	- MAX*125 : memory limit exceed
	- new version to reduce the memory usage : But the following message
		- RTE (SIGSEGV: segmentation fault, probably incorrect memory access or stack overflow)
- 8cpp.cpp : based on 8moreC.cpp
	- this is almost cpp std. But, it takes a lot of memory.
	- RTE (SIGKILL: program was forcefully killed, probably memory limit exceeded)


# 9 : D Tree
- http://codeforces.com/problemset/problem/570/D
- 9.cpp :  sample is done.   succeed until test 5.    timeout in test 6 within 2 sec (500000 nodes)
- 9r2.cpp : cache 70 level.   timeout in test 35


# 10 : Elivator 
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=701&sca=4050
- 10.cpp :  I think that it is just get the mimimal using elivator count.  But , I should add the function of elivator history.
- 10r.cpp
- [10ans.cpp](https://github.com/cheoljoo/problemSolving/blob/master/ps/10ans.cpp)
    - 10.data       2 1 3 
    - 10.data2      4 5 4 2 1
    - 10.data3      5 5 4 2 1 3
    - [Result](http://www.jungol.co.kr/theme/jungol/reinfo.php?sid=??)
        - No.1  [Good] : 0.002
        - No.2  [Good] : 0.002
        - No.3  [Good] : 0.002
        - No.4  [Good] : 0.003
        - No.5  [Good] : 0.002
        - No.6  [RTE]
        - No.7  [Good] : 0.020
        - No.8  [Good] : 0.003
        - No.9  [Good] : 0.002
        - No.10 [Good] : 0.001
- algorithm
    - store story(floor) and elivator  from 0 to N-1
    - use DFS
    - restriction : 
            - store the cost (count or depth) for each story (floor)
            - check visited

# 11 : 조세퍼스 순열
- https://www.acmicpc.net/problem/1168
- [11.cpp](https://github.com/cheoljoo/problemSolving/blob/master/ps/11.cpp)  : for debugging 
- [11r.cpp](https://github.com/cheoljoo/problemSolving/blob/master/ps/11r.cpp)  :  [ok](https://www.acmicpc.net/status?user_id=healing&problem_id=1168&from_mine=1)

# 12 :  배낭 챙기기 1
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=357&sca=50

| |  12r.cpp  | 12r1.cpp   |  12r2.cpp |
|-|-----------|------------|-----------|
| type |  recursive | stack | stack |
| method | DFS  | BFS  | DFS  |
| real time |  0m0.119s | 0m1.352s | 0m1.198s |
| stack max (case : 12.data3) |           | 8397  | 5586  |
| result |  success | Time Limit Exceed(30) - 1704ms  | Memory Limit Exceed(30) - 74MB |



