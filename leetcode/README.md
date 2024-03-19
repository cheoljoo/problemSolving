- [1. yearly report](#1-yearly-report)
- [2. Python3 knowledge](#2-python3-knowledge)
  - [2.1. sort performance](#21-sort-performance)
  - [2.2. sort keys](#22-sort-keys)
  - [2.3. sorted data structure](#23-sorted-data-structure)
    - [2.3.1. bisect](#231-bisect)
    - [2.3.2. heapq](#232-heapq)
      - [2.3.2.1. last largest l count is in heap.  \<- To maintain the largest n elements while processing the smallest one](#2321-last-largest-l-count-is-in-heap----to-maintain-the-largest-n-elements-while-processing-the-smallest-one)
  - [2.4. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree](#24-height-balanced-binary-search-trees--avlcreatoradelson-velsky-and-landis-tree)
  - [2.5. hamming weight : number of '1' bits](#25-hamming-weight--number-of-1-bits)
  - [2.6. find (?,?) including A among \[(x1,x2) , ....\] if x1\>x2](#26-find--including-a-among-x1x2---if-x1x2)
  - [2.7. two dimensional array initialize and set](#27-two-dimensional-array-initialize-and-set)
  - [2.8. regular expression (import re)](#28-regular-expression-import-re)
    - [2.8.1. difference between re.search() and re.match()](#281-difference-between-research-and-rematch)
  - [2.9. format string](#29-format-string)
  - [2.10. lexicographical order](#210-lexicographical-order)
  - [2.11. palindromic](#211-palindromic)
  - [2.12. dictionary : Python Remove Key from a Dictionary: A Complete Guide](#212-dictionary--python-remove-key-from-a-dictionary-a-complete-guide)
  - [2.13. list : python remove element from a list](#213-list--python-remove-element-from-a-list)
  - [2.14. compare between list and set()  : 3Sum (#15)](#214-compare-between-list-and-set---3sum-15)
  - [2.15. graph](#215-graph)
    - [2.15.1. dijkstra](#2151-dijkstra)
  - [2.16. greedy algorithm](#216-greedy-algorithm)
    - [2.16.1. dijkstra's algorithm](#2161-dijkstras-algorithm)
    - [2.16.2. Ford-Fulkerson Algorithm](#2162-ford-fulkerson-algorithm)
    - [2.16.3. Kruskal's Algorithm : find minimum spanning tree : optimal graph connected all vertics](#2163-kruskals-algorithm--find-minimum-spanning-tree--optimal-graph-connected-all-vertics)
    - [2.16.4. Prim's Algorithm : find minimum spanning tree](#2164-prims-algorithm--find-minimum-spanning-tree)
    - [2.16.5. Huffman Coding : a technique of compressing data to reduce its size](#2165-huffman-coding--a-technique-of-compressing-data-to-reduce-its-size)
  - [2.17. Dynamic Programming](#217-dynamic-programming)
    - [2.17.1. Longest Common Subsequence](#2171-longest-common-subsequence)
    - [2.17.2. Floyd-Warshall Algorithm](#2172-floyd-warshall-algorithm)
  - [2.18. grouping : find \& union](#218-grouping--find--union)
  - [2.19. deque](#219-deque)
  - [2.20. window slide to get max in moving range](#220-window-slide-to-get-max-in-moving-range)
  - [2.21. OrderedDict](#221-ordereddict)
  - [2.22. 2^16 traverse](#222-216-traverse)
  - [2.23. maximum profit when buy and sell stock](#223-maximum-profit-when-buy-and-sell-stock)
  - [2.24. sometimes initializing time is slower than calulation.](#224-sometimes-initializing-time-is-slower-than-calulation)
  - [2.25. BFS](#225-bfs)
  - [2.26. Zero Sum Consecutive](#226-zero-sum-consecutive)
  - [2.27. appendix (technique)](#227-appendix-technique)
- [3. C++ Knowledge](#3-c-knowledge)
  - [3.1. add this statements in starting points](#31-add-this-statements-in-starting-points)
  - [3.2. sort](#32-sort)
- [4. Books \& URL](#4-books--url)

--------------------
leetcode : my profile -> https://leetcode.com/cheoljoo/

# 1. yearly report
- [2022~2023 Problem Solving](./README-2022-2023.md)
- [2024 Problem Solving](./README-2024.md)

# 2. Python3 knowledge
## 2.1. sort performance
- update and sort is faster than update-insert each elements
  - slow : remove() and bisect.insort()
  - fast : nums[]=? and sort()

## 2.2. sort keys
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

    list.sort(key=lambda r:r[0])

    # https://linuxhint.com/sort-lambda-python/
    # Example-1: Sort a list of numerical string data
    # Declare a list of string with number values
    n_list = ['11', '50', '5', '1', '37', '19']
    # Sort the list using lambda and sorted function
    sorted_list = sorted(n_list, key=lambda x: int(x[0:]))

    # Example-2: Sort a list of tuples
    # Declare a list of tuples
    tuple_list = [("HTML", 15, 'M01'), ("JavaScript", 10, 'M03'), ("Bootstrap", 5, 'M02')]
    # Sort the list based on the first item of the tuple
    sorted_list1 = sorted(tuple_list, key=lambda x: x[0])
    # Print the first sorted list
    print("The sorted list based on the first item:\n", sorted_list1)
    # Sort the list based on the second item of the tuple
    sorted_list2 = sorted(tuple_list, key=lambda x: x[1])
    # Print the second sorted list
    print("The sorted list based on the second item:\n", sorted_list2)
    # Sort the list based on the third item of the tuple
    sorted_list3 = sorted(tuple_list, key=lambda x: x[2])

    # Example-4: Sort a list of dictionaries
    # Declare the list of dictionary
    dic_list = [{"code": "CSE-401", "name": "Multimedia", "Credit": 2.0},
            {"code": "CSE-101", "name": "Computer Fundamental", "Credit": 1.5},
            {"code": "CSE-305", "name": "Unix Programming", "Credit": 3.0}]
    # Print the sorted dictionary based on code
    print("Sorting based on the code:\n", sorted(dic_list, key=lambda i: i['code']))
    # Print the sorted dictionary based on name
    print("Sorting based on the name:\n", sorted(dic_list, key=lambda i: (i['name'])))
    # Print the sorted dictionary based on code and name
    print("Sorting based on the code and name:\n", sorted(dic_list, key=lambda i: (i['code'], i['name'])))
    # Print the sorted dictionary in descending based on name
    print("Sorting in descending order based on the name:\n", sorted(dic_list, key=lambda i: i['name'], reverse=True))
```
- dictionary sort
  - ```sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])```

## 2.3. sorted data structure
### 2.3.1. bisect
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
len(nums): 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 4 bisect_left: 2 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 4 bisect_right: 2 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 5 bisect_left: 2 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 5 bisect_right: 9 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 1 bisect_left: 0 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 1 bisect_right: 0 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 6 bisect_left: 9 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 6 bisect_right: 10 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 81 bisect_left: 10 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 81 bisect_right: 10 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 181 bisect_left: 11 len(nums) 11
nums: [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100] n: 181 bisect_right: 11 len(nums) 11
```

### 2.3.2. heapq
- sorted data structure : [0] is the smallest number
  - https://www.daleseo.com/python-heapq/
    - import heapq  
    - heapq.heappush(list,value) heapq.heappop(list)   
    - list[0] is minimal value.   
    - if you want to maximum value , * -1.0 

#### 2.3.2.1. last largest l count is in heap.  <- To maintain the largest n elements while processing the smallest one 
- ```python
    st.append(h)
      if laddersmx == -1 or laddersmx < h:
          st.sort()
    # ====> 
    heapq.heappush(heap, diff)
    if len(heap) > ladders:
        bricks -= heapq.heappop(heap)
  ```
#### 

### 2.3.3. PriorityQueue
- priority Queue (sorted with priority order)
  - https://www.daleseo.com/python-priority-queue/
    - from queue import PriorityQueue
    - put()
    - get()

### 2.3.4. sortedcontainers
- SortedList
- SortedDict
- SortedSet
- URL
  - https://pythonlang.dev/repo/grantjenks-python-sortedcontainers/ 
  - https://grantjenks.com/docs/sortedcontainers/

### 2.3.5. in place sort
- ```nums[i:] = sorted(nums[i:])   # in place sort```

## 2.4. Euclidean-algorithm : 유클리드 호제법
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

## 2.4. Height-Balanced Binary Search Trees : AVL(creator:Adelson-Velsky and Landis) Tree
- https://www.programiz.com/dsa/avl-tree
- [avl.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/avl.py)

## 2.5. hamming weight : number of '1' bits
- Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://shumin.co.kr/algorithm-hamming-weight-bit-count/)).

## 2.6. find (?,?) including A among [(x1,x2) , ....] if x1>x2 
- 27. The Skyline Problem (#218) - Hard
- korean : [(x1,x2) , ....] 에서 A를 포함하는 것들을 구하시요.
- sort by x1 -> find x1 : 0 .. A .. x1 -> calulate
- if A is another sorted list [A1,A2...] , 0 .. A1 .. x1 and x2 A1 (sorted by x2) -> when we find pairs for A2 , we can skip until x2   

## 2.7. two dimensional array initialize and set
- ln = [[0] * 101] * (query_row+1)
  - ln[0][0]=2 then all row's [0] were changed into 2
- ln = [[0 for c in range(101)] for r in range(query_row+1)]
  - it is right solution to initialize two dimensional array
  - https://www.kite.com/python/answers/how-to-initialize-a-2d-array-in-python
  
## 2.8. regular expression (import re)
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

### 2.8.1. difference between re.search() and re.match()
- https://www.geeksforgeeks.org/python-re-search-vs-re-match/
- re.match() searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none.

## 2.9. format string
- https://hyjykelly.tistory.com/65
- performance comparison : https://brownbears.tistory.com/421

## 2.10. lexicographical order
- alphaveticall order except we can not find this character  ex) cb  -> cb  ,  cbc -> bc
- https://leetcode.com/problems/remove-duplicate-letters/submissions/

## 2.11. palindromic 
- a word, phrase, sentence, or number that reads the same backward or forward "Step on no pets" is a palindrome.
- [63. Valid Palindrome II (#680) - easy / python / 1H](#63-valid-palindrome-ii-680---easy--python--1h)

## 2.12. dictionary : Python Remove Key from a Dictionary: A Complete Guide
- dictionary.pop(key_to_remove, not_found)
  - https://careerkarma.com/blog/python-remove-key-from-a-dictionary/#:~:text=To%20remove%20a%20key%20from,item%20after%20the%20del%20keyword.

## 2.13. list : python remove element from a list 
- thislist.remove("banana")
- thislist.pop(1)
- del thislist[0]
- thislist.clear()
  - https://www.w3schools.com/python/python_lists_remove.asp

## 2.14. compare between list and set()  : 3Sum (#15)
- list : tmplist = [nums[i],nums[j],nums[k]]
  - list.append(tmplist)
- set : tmptuple = (nums[i],nums[j],nums[k])
  - set.add(tmptuple)
- set is faster when we want to add item
  - if tmplist not in list:     list.append(tmplist)
  - set.add(tmptuple)

## 2.15. graph
### 2.15.1. dijkstra
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

## 2.16. greedy algorithm
- Greedy Choice Property : If an optimal solution to the problem can be found by choosing the best choice at each step without reconsidering the previous steps once chosen, the problem can be solved using a greedy approach. This property is called greedy choice property.
  - Problem: You have to make a change of an amount using the smallest possible number of coins.
    - Amount: $18
    - Available coins are
      -   $5 coin
      -   $2 coin
      -   $1 coin
    - There is no limit to the number of each coin you can use.
### 2.16.1. dijkstra's algorithm
- [1.14.1. dijkstra](#1141-dijkstra)

### 2.16.2. Ford-Fulkerson Algorithm
- Ford-Fulkerson algorithm is a greedy approach for calculating the maximum possible flow in a network or a graph.
- Each pipe has a certain capacity of liquid it can transfer at an instance. For this algorithm, we are going to find how much liquid can be flowed from the source to the sink at an instance using the network.
  - ![](https://cdn.programiz.com/sites/tutorial2program/files/flow-network.png)
- algorithm :
  1. find path with BFS (parent is path from sink.)
  2. sum path flow
  3. change graph (substract graph capacity when they used from sink)
  4. goto 1

### 2.16.3. Kruskal's Algorithm : find minimum spanning tree : optimal graph connected all vertics
- We start from the edges with the lowest weight and keep adding edges until we reach our goal. The steps for implementing Kruskal's algorithm are as follows:
  - Sort all the edges from low weight to high
  - Take the edge with the lowest weight and add it to the spanning tree. **If adding the edge created a cycle,** then reject this edge.
  - Keep adding edges until we reach all vertices.
  - ![](https://cdn.programiz.com/sites/tutorial2program/files/ka-1.png)
- algorithm :
  - checking the loop is key factor. if both vertics of edge are in current graph , it is loop.  <-  i think it is faster than suggested code.

### 2.16.4. Prim's Algorithm : find minimum spanning tree
- i do not know what is difference with kruskal's algorithm
  
### 2.16.5. Huffman Coding : a technique of compressing data to reduce its size
- Using the Huffman Coding technique, we can compress the string to a smaller size. Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.

| Character       | Frequency | Code | Size     |
| --------------- | --------- | ---- | -------- |
| A               | 5         | 11   | 5*2 = 10 |
| B               | 1         | 100  | 1*3 = 3  |
| C               | 6         | 0    | 6*1 = 6  |
| D               | 3         | 101  | 3*3 = 9  |
| 4 * 8 = 32 bits | 15 bits   |      | 28 bits  |

## 2.17. Dynamic Programming
- if there are overlapping among these subproblems, then the solutions to these subproblems can be saved for future reference. 
- This technique of storing the value of subproblems is called memoization. By saving the values in the array, we save time for computations of sub-problems we have already come across.

### 2.17.1. Longest Common Subsequence
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
- ```python
        table = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]  # col : word1 , row : word2
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else :
                    table[i][j] = max(table[i-1][j],table[i][j-1])
        # print(table)
        return len(word1) + len(word2) - table[len(word2)][len(word1)]*2
  ```

### 1.17.2. Longest Common Substring (application)
- O(MN)
- 
    |     |     |   0 |   1 |   2 |   3 |   4 |   5 |   6 |
    |-----|-----|-----|-----|-----|-----|-----|-----|-----|
    |     | chʳ |     |  a  |  b  |  c  |  d  |  a  |  f  |
    |  0  |     |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
    |  1  |  a  |  0  |  1  |  0  |  0  |  0  |  1  |  0  |
    |  2  |  c  |  0  |  0  |  0  |  1  |  0  |  0  |  0  |
    |  3  |  b  |  0  |  0  |  1  |  0  |  0  |  0  |  0  |
    |  4  |  c  |  0  |  0  |  0  |  **2**  |  0  |  0  |  0  |
    |  5  |  f  |  0  |  0  |  0  |  0  |  0  |  0  |  1  |
- if s2[i] equals to s1[j]       =>   Table[i][j] = Table[i-1][j-1] + 1
  - max is 2 . maxsubstring size is 2
- ```python
        table = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]  # col : word1 , row : word2
        mx = 0
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                    mx = max(mx,table[i][j])
        print(mx,table)
        return len(word1) + len(word2) - mx*2   
  ```

### 2.17.2. Floyd-Warshall Algorithm
- https://www.programiz.com/dsa/floyd-warshall-algorithm
- Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph. This algorithm works for both the directed and undirected weighted graphs. 
- ![](https://cdn.programiz.com/sites/tutorial2program/files/fw-Graph.png)  ![](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-1.png) ![](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-2.png)
- O(N^3)

## 2.18. grouping : find & union
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

## 2.19. deque
- https://leonkong.cc/posts/python-deque.html
  - deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
  - deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
  - deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
  - deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
  - deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
  - deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
  - deque.remove(item): item을 데크에서 찾아 삭제한다.
  - deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

## 2.20. window slide to get max in moving range
- heapq를 이용한 window slide시 max 값을 가져오는 방법
```python
        heapwindow = [(-dp[-1],-1)]
        for i in range(2,len(nums)+1):
            mi = -i
            while True:
                vw , iw = heapq.heappop(heapwindow)
                if mi+1 <= iw  and iw <= mi+k:
                    heapq.heappush(heapwindow,(vw,iw))
                    break
                else:
                    continue
            dp[mi] = nums[mi] + -vw
            heapq.heappush(heapwindow,(-dp[mi],mi))
```

## 2.21. OrderedDict
- collections.OrderedDict : https://docs.python.org/3/library/collections.html#ordereddict-objects
- A regular dict can emulate OrderedDict’s od.move_to_end(k, last=True) with d[k] = d.pop(k) which will move the key and its associated value to the rightmost (last) position.

## 2.22. 2^16 traverse
- O(2^16)
- algorithm : how to traverse 2^16 like binary number. use DFS (index,not include / include me)
```python
self.dp(arr,1,arr[0])
self.dp(arr,1,"")
def dp(self,arr,idx,result):  # fromIdx .. toIdx
        self.count += 1
        # print(idx,result)
        if idx >= len(arr):
            self.ans = max(self.ans,len(result))
            return
        self.dp(arr,idx+1,result)
        ....
        if flag == False:
            self.dp(arr,idx+1,result+arr[idx])
        return
```

## 2.23. maximum profit when buy and sell stock
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/3667440/beats-100-c-java-python-beginner-friendly
- Time complexity: O(n)     Space complexity: O(1)
```python
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell
```

## 2.24. sometimes initializing time is slower than calulation.
- https://leetcode.com/problems/climbing-stairs

## 2.25. BFS
- better code for BFS uses only queue.  we do not need to use heapq in this case because it will increase path in BFS.
- BFS is the best when we find shortest path in maze
- https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

## 2.26. Zero Sum Consecutive
- [1,2,3,-3,4]  -> accumulative [1,3,6,3,7]  index 1 and 3 's value is the same 3.   sum of index 2~3  is zero.

## 2.27. appendix (technique)
- dictionary is faster than set
- defaultdict is faster than {}  : 37 -> 31 ms : https://leetcode.com/problems/custom-sort-string/submissions/
- several line of condition check (if) does not have any benefit of performance.
  - ```if (0 <= r + rr < self.R) and (0<= c+cc < self.C) and (grid[r+rr][c+cc] == 1):```
- for check is better "in" command
  - ```for c in range(self.C): if grid[r][c] == 1: return -1``` is better than ```if 1 in grid[r]:```
- deque() is better than ```[]```.   deque().popleft() / pop() / append()
- declaration as valuable is better.   ```for rr,cc in [[1,0],[-1,0],[0,1],[0,-1]]:``` -> ```direction = [[1,0],[-1,0],[0,1],[0,-1]]```
- list :  rs += rooms[r]  --> rs.extend(rooms[r])
- set differnce :  set(nums1) - set(nums2)
- d = Counter(tasks)  is faster than  d = {}









# 3. C++ Knowledge
## 3.1. add this statements in starting points
```cpp
ios_base::sync_with_stdio(false);
cin.tie(NULL);
```
## 3.2. sort
- sort(nums.begin(), nums.end());

# 4. Books & URL
- Python module of the week : http://pymotw.com/2/PyMOTW-1.133.pdf
- RealPython : http://www.realpython.org
- For Beginners for graph : https://leetcode.com/discuss/study-guide/1808711/Graph-for-Beginers-Problems
 
