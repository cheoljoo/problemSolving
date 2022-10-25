
- [1. year 2022](#1-year-2022)
  - [1.1. 집합은 a, b를 싫어해](#11-집합은-a-b를-싫어해)
    - [1.1.1. virtualenv (numpy memory_profiler)](#111-virtualenv-numpy-memory_profiler)
    - [1.1.2. docstirngs](#112-docstirngs)
    - [1.1.3. 1st trial - dictionay version](#113-1st-trial---dictionay-version)
    - [1.1.4. 2nd trial - numpy version](#114-2nd-trial---numpy-version)
    - [1.1.5. memory difference with big N](#115-memory-difference-with-big-n)
  - [1.2. 색종이](#12-색종이)
  - [1.3. 주사위 굴리기 2 (삼성)](#13-주사위-굴리기-2-삼성)
  - [1.4. 모자른 나라](#14-모자른-나라)
  - [1.5. k개의 부분 배열](#15-k개의-부분-배열)
  - [1.6. 수열과 인연](#16-수열과-인연)
  - [1.7. 줄자접기](#17-줄자접기)
  - [1.8. 잃어버린 괄호](#18-잃어버린-괄호)
  - [1.9. 뒤집어진 소수](#19-뒤집어진-소수)
  - [1.10. 2020+Online+Code+Jam+2 A번 - 해적과보석 : [python]](#110-2020onlinecodejam2-a번---해적과보석--python)
- [2. 2020+Online+Code+Jam+2 B번 장난감 동맹군 : [python]](#2-2020onlinecodejam2-b번-장난감-동맹군--python)
- [3. 마라톤 대회(Bronze) (역량인증)](#3-마라톤-대회bronze-역량인증)
- [4. 콜타르 채우기](#4-콜타르-채우기)
- [5. histogram  : 제일 큰 직사각형 만들기](#5-histogram---제일-큰-직사각형-만들기)
- [6. 2022년 SW역량 4회차 기출문제 2번 : 머그컵](#6-2022년-sw역량-4회차-기출문제-2번--머그컵)
- [7. 2022년 SW역량 4회차 기출문제 3번 : TV 모델수](#7-2022년-sw역량-4회차-기출문제-3번--tv-모델수)
- [8. [ACT] 공주님의 정원](#8-act-공주님의-정원)
- [9. [ACT] 참외 밭](#9-act-참외-밭)
- [10. [ACT] 사회적 거리두기](#10-act-사회적-거리두기)
- [11. warehouse - 창고](#11-warehouse---창고)

----------

# 1. year 2022

## 1.1. 집합은 a, b를 싫어해
- https://codeup.kr/problem.php?id=2128
- cd 2022
- make 1
- 통과   ( 1-lowMem3.py )
  - 고성대 책임님이 지적해 주신 것이 맞았습니다. 앞으로 int ( ? / ? ) 으로 하면 안되고 , // operator을 사용해서 몫을 int로 바로 구해야 문제 없습니다.
  - int ( ? / ? ) 으로 하면 ?/? 에서 float로 변경을 할때 많은 뒤의 상세한 값들을 잃어버리게 된다고 합니다. 그래서 , 몫을 구할때  // operator를 써야 정확하게 integer의 몫을 구할수 있다고 합니다.

### 1.1.1. virtualenv (numpy memory_profiler)
- virtualenv a
- source a/bin/activate
- pip install numpy
- pip install memory_profiler
- pip install mkdocs

### 1.1.2. docstirngs
- pip install mkdocs
- pip install mkdocstrings
- pip install mkdocs-material

- command
    - mkdocs new [yours]
    - cd [yours]
    - copy your files and change yml and others
    - mkdocs build

- http://lotto645.lge.com:8088/cheoljoo.lee/code/problemSolving/2022/docstring/site/my_page/

### 1.1.3. 1st trial - dictionay version
- https://github.com/cheoljoo/problemSolving/blob/220107/1_hate_a_b/2022/1.1.py
```txt
$  echo "10000000000 2000000000 2" | python3 -m memory_profiler ./1.1.py
9999999996
Filename: ./1.1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     34.3 MiB     34.3 MiB           1       @profile
    26                                             def get_count(self):
    27     34.3 MiB      0.0 MiB           1           sn ,sa , sb = input().split()
    28     34.3 MiB      0.0 MiB           1           n = int(sn)
    29     34.3 MiB      0.0 MiB           1           a = int(sa)
    30     34.3 MiB      0.0 MiB           1           b = int(sb)
    31     34.3 MiB      0.0 MiB           1           if debug :
    32                                                     print(n , a , b,debug)
    33
    34     34.3 MiB      0.0 MiB           1           x = defaultdict(dict)
    35                                                 #x = np.zeros(n)
    36     34.3 MiB      0.0 MiB           1           count = n
    37     34.3 MiB      0.0 MiB           5           for i in range(1 , n+1):
    38     34.3 MiB      0.0 MiB           5               stridx = str(a*i+b)
    39     34.3 MiB      0.0 MiB           5               stri = str(i)
    40     34.3 MiB      0.0 MiB           5               if debug :
    41                                                         print("element:",i, stri, x[stri])
    42     34.3 MiB      0.0 MiB           5               if x[stri] != 1 :
    43     34.3 MiB      0.0 MiB           5                   if debug :
    44                                                             print("x:",stridx, a*i+b , x[stridx])
    45     34.3 MiB      0.0 MiB           5                   if (a*i+b) > n :
    46     34.3 MiB      0.0 MiB           1                       break
    47                                                         else :
    48     34.3 MiB      0.0 MiB           4                       x[stridx] = 1
    49     34.3 MiB      0.0 MiB           4                       if debug :
    50                                                                 print("set x:",stridx,a*i+b , x[stridx])
    51     34.3 MiB      0.0 MiB           4                       count -= 1
    52
    53     34.3 MiB      0.0 MiB           1           if debug :
    54                                                     print("result : ",end="")
    55     34.3 MiB      0.0 MiB           1           print(count)
```

```txt
$  echo "10000000000 200000 2" | python3 -m memory_profiler ./1.1.py
9999950001
Filename: ./1.1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     34.2 MiB     34.2 MiB           1       @profile
    26                                             def get_count(self):
    27     34.2 MiB      0.0 MiB           1           sn ,sa , sb = input().split()
    28     34.2 MiB      0.0 MiB           1           n = int(sn)
    29     34.2 MiB      0.0 MiB           1           a = int(sa)
    30     34.2 MiB      0.0 MiB           1           b = int(sb)
    31     34.2 MiB      0.0 MiB           1           if debug :
    32                                                     print(n , a , b,debug)
    33
    34     34.2 MiB      0.0 MiB           1           x = defaultdict(dict)
    35                                                 #x = np.zeros(n)
    36     34.2 MiB      0.0 MiB           1           count = n
    37     56.9 MiB      0.0 MiB       50000           for i in range(1 , n+1):
    38     56.9 MiB      0.0 MiB       50000               stridx = str(a*i+b)
    39     56.9 MiB      0.0 MiB       50000               stri = str(i)
    40     56.9 MiB      0.0 MiB       50000               if debug :
    41                                                         print("element:",i, stri, x[stri])
    42     56.9 MiB     18.8 MiB       50000               if x[stri] != 1 :
    43     56.9 MiB      0.0 MiB       50000                   if debug :
    44                                                             print("x:",stridx, a*i+b , x[stridx])
    45     56.9 MiB      0.0 MiB       50000                   if (a*i+b) > n :
    46     56.9 MiB      0.0 MiB           1                       break
    47                                                         else :
    48     56.9 MiB      3.9 MiB       49999                       x[stridx] = 1
    49     56.9 MiB      0.0 MiB       49999                       if debug :
    50                                                                 print("set x:",stridx,a*i+b , x[stridx])
    51     56.9 MiB      0.0 MiB       49999                       count -= 1
    52
    53     56.9 MiB      0.0 MiB           1           if debug :
    54                                                     print("result : ",end="")
    55     56.9 MiB      0.0 MiB           1           print(count)
```


### 1.1.4. 2nd trial - numpy version
- https://github.com/cheoljoo/problemSolving/blob/220107/1_hate_a_b/2022/1.py
- I got memory overflow on site.  
    - conclusion : numpy's initialization needs more memory.
```txt
$  echo "10002000300040 200020003 2" | python3 -m memory_profiler 1.py
Filename: 1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    22   34.129 MiB   34.129 MiB           1       @profile
    23                                             def __init__(self, n , a , b, debug=0):
    24   34.129 MiB    0.000 MiB           1           self.debug = debug
    25   34.129 MiB    0.000 MiB           1           self.n = n
    26   34.129 MiB    0.000 MiB           1           self.a = a
    27   34.129 MiB    0.000 MiB           1           self.b = b
    28   34.129 MiB    0.000 MiB           1           self.x = np.zeros(n+1,dtype=np.int8)
    29
    30                                                 super().__init__()
    31
    32                                                 if self.debug :
    33                                                     print(sys._getframe().f_code.co_name ,":",self.n , self.a , self.b,self.debug)


Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/data01/cheoljoo.lee/code/problemSolving/2022/a/lib/python3.8/site-packages/memory_profiler.py", line 1349, in <module>
    exec_with_profiler(script_filename, prof, args.backend, script_args)
  File "/data01/cheoljoo.lee/code/problemSolving/2022/a/lib/python3.8/site-packages/memory_profiler.py", line 1250, in exec_with_profiler
    exec(compile(f.read(), filename, 'exec'), ns, ns)
  File "1.py", line 82, in <module>
    count_obj = CountAntiSet(n,a,b,debug)
  File "/data01/cheoljoo.lee/code/problemSolving/2022/a/lib/python3.8/site-packages/memory_profiler.py", line 759, in f
    return func(*args, **kwds)
  File "1.py", line 28, in __init__
    self.x = np.zeros(n+1,dtype=np.int8)
numpy.core._exceptions.MemoryError: Unable to allocate 9.10 TiB for an array with shape (10002000300041,) and data type int8
```


### 1.1.5. memory difference with big N
```txt
$  echo "10293842 6 2" | python3 1.1.1.dict_bool.py

8823293
Filename: 1.1.1.dict_bool.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     33.5 MiB     33.5 MiB           1       @profile
    26                                             def get_count(self):
    27     33.5 MiB      0.0 MiB           1           sn ,sa , sb = input().split()
    28     33.5 MiB      0.0 MiB           1           n = int(sn)
    29     33.5 MiB      0.0 MiB           1           a = int(sa)
    30     33.5 MiB      0.0 MiB           1           b = int(sb)
    31     33.5 MiB      0.0 MiB           1           if debug :
    32                                                     print(n , a , b,debug)
    33
    34     33.5 MiB      0.0 MiB           1           x = defaultdict(bool)
    35                                                 #x = np.zeros(n)
    36     33.5 MiB      0.0 MiB           1           count = n
    37    284.8 MiB      0.0 MiB     1715641           for i in range(1 , n+1):
    38    284.8 MiB      0.0 MiB     1715641               nxt = a*i+b
    39    284.8 MiB     90.4 MiB     1715641               if debug :
    40                                                         print("element:",i, x[i])
    41    284.8 MiB    107.0 MiB     1715641               if x[i] != True :
    42    284.8 MiB      0.0 MiB     1470550                   if debug :
    43                                                             print("x:",nxt, x[nxt])
    44    284.8 MiB      0.0 MiB     1470550                   if nxt > n :
    45    284.8 MiB      0.0 MiB           1                       break
    46                                                         else :
    47    284.8 MiB     54.0 MiB     1470549                       x[nxt] = True
    48    284.8 MiB      0.0 MiB     1470549                       if debug :
    49                                                                 print("set x:",nxt, a*i+b , x[nxt])
    50    284.8 MiB      0.0 MiB     1470549                       count -= 1
    51
    52    284.8 MiB      0.0 MiB           1           if debug :
    53                                                     print("result : ",end="")
    54    284.8 MiB      0.0 MiB           1           print(count)




$  echo "10293842 6 2" | python3 -m memory_profiler 1.py
8823293
Filename: 1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    46   34.141 MiB   34.141 MiB           1       @profile
    47                                             def __init__(self, n , a , b, debug=0):
    48                                                 """
    49                                                 get the count of elements to meet the rule. (2)
    50
    51                                                 :param n: max number
    52                                                 :param a: ax+b
    53                                                 :param b: ax+b
    54                                                 :param debug: debug mode
    55                                                 :return:
    56                                                 """
    57   34.141 MiB    0.000 MiB           1           self.debug = debug
    58   34.141 MiB    0.000 MiB           1           self.n = n
    59   34.141 MiB    0.000 MiB           1           self.a = a
    60   34.141 MiB    0.000 MiB           1           self.b = b
    61   34.141 MiB    0.000 MiB           1           self.x = np.zeros(n+1,dtype=np.int8)
    62
    63   34.141 MiB    0.000 MiB           1           super().__init__()
    64
    65   34.141 MiB    0.000 MiB           1           if self.debug :
    66                                                     print(sys._getframe().f_code.co_name ,":",self.n , self.a , self.b,self.debug)


Filename: 1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68   34.141 MiB   34.141 MiB           1       @profile
    69                                             def get_count(self):
    70                                                 """
    71                                                 get the count of elements to meet the rule. (2)
    72                                                 """
    73
    74   34.141 MiB    0.000 MiB           1           count = self.n
    75   43.914 MiB    0.000 MiB     1715641           for i in range(1 , self.n+1):
    76   43.914 MiB    0.000 MiB     1715641               nxt = self.a*i+self.b
    77   43.914 MiB    0.000 MiB     1715641               if self.x[i] != 1 :
    78   43.914 MiB    0.000 MiB     1470550                   if self.debug :
    79                                                             print("x:",i , ", x[i]:",self.x[i])
    80   43.914 MiB    0.000 MiB     1470550                   if nxt > self.n :
    81   43.914 MiB    0.000 MiB           1                       break
    82                                                         else :
    83   43.914 MiB    9.773 MiB     1470549                       self.x[nxt] = 1
    84   43.914 MiB    0.000 MiB     1470549                       if self.debug :
    85                                                                 self.print_set()
    86   43.914 MiB    0.000 MiB     1470549                       count -= 1
    87
    88   43.914 MiB    0.000 MiB           1           if self.debug :
    89                                                     print("result : ",end="")
    90   43.914 MiB    0.000 MiB           1           print(count)
```



## 1.2. 색종이
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=712&sca=2060#n
- jungol에서는 numpy와 같은 추가적인듈을 사용하면 안된다.
- 통과

- cd 2022
- make 2

## 1.3. 주사위 굴리기 2 (삼성)
- https://www.acmicpc.net/problem/23288   : 백준
- memory이슈까지 고민하여 문제 풀 예정
  - 주사위 동작할때 변하는 모습 미리 fix : 맨 아래값 고정 , 다음을 위한 변환된 주사위 모양 저장
  - 판에서 현 위치에서와 같은 연결되된 구간의 갯수 구하는 것
- unittest를 적용해보자. 기본 값을 가졌을때 이미 알고 있는 값들이 있으니 unit test구현 가능할 것으로 보임.
- 실패 : 예제는 통과했지만, site에서는 런탕미에러 (IndexError)
  - 다른 사람들은 모두 C++로 풀었네요.

- make 3 

## 1.4. 모자른 나라
- https://codeup.kr/problem.php?id=3808

## 1.5. k개의 부분 배열
- https://codeup.kr/problem.php?id=3092


## 1.6. 수열과 인연
- https://codeup.kr/problem.php?id=2127
- GCD : 유클리드 호제법 : 240 , 46 -> 46 , 240%46=10 -> 10 , 6 -> 6 , 4 -> 4 , 2 -> 2 , 0  답 2

- make 4
- vsc에서는 값이 잘 나오는 것 같은데, 3 1 8 이 답인데 사이트에서는 꼭 1 1 8 이라는 값으로 나오네요.
- 4-2.py : 메모리 초과 문제 해결하니 시간초과

## 1.7. 줄자접기
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=392&sca=3080
- make 5
  
- pass


##  1.8. 잃어버린 괄호
- https://www.acmicpc.net/problem/1541
  - 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
- make 6

- python regular expression : https://www.programiz.com/python-programming/regex


## 1.9. 뒤집어진 소수
- https://www.acmicpc.net/problem/10859
  - 어제 자다가 알람 시계를 떨어뜨렸는지, 08:15분이 51:80분이 되어 있었다. 그때 나는 디지털로 표시된 어떤 숫자는 180도 뒤집혔을 때도 숫자가 될 수 있다는 걸 깨달았다.
  - 내가 좋아하는 숫자는 소수이다. 당신이 할 일은 주어진 숫자가 소수인지, 뒤집혀서도 소수인지 확인하는 것이다.
- make 7

## 1.10. 2020+Online+Code+Jam+2 A번 - 해적과보석 : [python]
- http://collab.lge.com/main/download/attachments/1164888924/A-kor.pdf?version=1&modificationDate=1595823807000&api=v2
- Problem
  - 6점
```
시간제한 : 1 초
메모리제한 256 MB
Alice 와 Bob 두해적은 최근 보물섬에서 엄청난 양의 보물을 발견했다.
총 N개의보물상자를발견했는데, 공평하게 번갈아가며 보물상자를 하나씩골라가지기로하였다.
각 보물상자의가치는객관적으로 정하기어렵기때문에 두사람 모두 자신이 생각하는 가치가 얼마인지 적어서 서로에게 공유했다.
즉, i번째 보물상자는 Alice에겐 A[i] 달러만큼의 가치를갖고 Bob에겐 B[i] 달러만큼의 가치를갖는다.
상자를 나누어 갖기 위해 Alice부터 시작하여 Alice와 Bob은 번갈아 가며 남은 상자들 중 하나를 가져가기로 했다.
상자를 하나 가져오면 상대방의 차례가 되며, N개의 상자가 모두 주인을 찾은 후 둘은 각자 갈길을 떠나기로 했다.
편의상 보물상자를 모두 나눈후 Alice가가져간 상자의 (Alice 기준대로의) 가치의총합을 Score_A라하고
Bob이가져간상자의 (Bob 기준대로의) 가치의총합을 Score_B라 하자.
Alice와 Bob은 서로 약속은 지키는 의리 있는 해적 이지만, 욕심이 많기때문에
Alice의목표는 (Score_A - Score_B)가 최대가 되도록 상자를 선택하는 것이고
Bob의목표는 (Score_B - Score_A)가 최대가 되도록 상자를 선택하는 것이다.
이 두사람은 언제나 최선을 다해서 어떤상자를 가져갈지 결정한다.
예를들어 N = 3 인경우 세개의 보물상자가 있으며, 각 해적이 생각하는 보물상자의 가치는 아래와같다.

상자1: A[1] = 10 & B[1] = 5
상자2: A[2] = 100 & B[2] = 90
상자 3: A[3] = 2 & B[3] = 0

이때 Alice가상자 2를먼저가져가고, 그후 Bob이상자 1을가져간후, 마지막으로 Alice가상자 3을가져간다면,
Alice는총 102 달러만큼보물을챙기고 Bob은 총 5달러 만큼 보물을 챙기게된다.
만약 Alice가자신의 첫차례에 상자 2가아닌 다른상자를가져간다면 (상자 1 혹은상자 3), Bob은 자신의 차례에 상자 2를가져갈테니,
이경우 Alice는 10+2 = 12 달러  그리고 Bob은 90달러만큼의 보물을 챙기게된다.
따라서 Alice가최선을다한다면 첫차례에 반드시보물 2를 가져 가야한다
보물상자의 수 N과 해적 둘이 각자 생각하는 보물상자의 가치가 주어졌을때,
두사람이 최선을 다해 각자의 목표를 최대화 했을때 (Score_A - Score_B) 값이 무엇인지 구하는 프로그램을 작성하시오.
```
- Input
```
첫줄에테스트케이스의수 T가주어진다.
각테스트케이스에대해첫줄에정수 N이주어지며이는보물상자의수를나타낸다.
다음 N줄에걸쳐서각보물의가치가공백으로구분되어주어진다
(첫수는 Alice가생각하는가치, 두번째수는 Bob이생각하는가치).
1 ≤ T ≤ 10
1 ≤ N ≤ 100,000
0 ≤ A[i], B[i] ≤ 100,000
```
- Output
  - 각테스트케이스에 대하여 두사람이 최선을 다해 게임을 플레이했을때, (ScoreA - ScoreB) 값을구하여출력한다.
- [pirateJewel.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/pirateJewel.py) : passed

# 2. 2020+Online+Code+Jam+2 B번 장난감 동맹군 : [python]
- 2개의 동맹으로 나눌 수 있는지? YES or NO
- [toyAlly.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/toyAlly.py) : passed
- [toyAlly2.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/toyAlly2.py) : passed   optimized to find starting node each group
- algorithm :
  - 들어오는 순서대로 처리하면 안 될 듯!
  - 일단 전체적으로 서로 엮여 있는 것들이 group이다.
    - 각 group이 모두 잘 분류가 되어져있는지 판단한다.


# 3. 마라톤 대회(Bronze) (역량인증)
- problem :
    - 학생들이 건강하지 못하다고 생각한 선생님은 학생들을 위한 마라톤 대회를 열었고, 우승 후보인 기연이도 이 대회에 참가할 예정이다.
    - 마라톤 코스는 N(3≤N≤100,000)개의 체크 포인트로 구성되어 있으며, 1번 체크포인트에서 시작해서 모든 체크 포인트를 순서대로 방문한 후 N번 체크포인트에서 마라톤이 끝난다. 기연이는 우승해야 한다는 부담감 때문에 중간에 있는 체크포인트 한 개를 몰래 건너 뛰려고 한다. 단, 1번과 N번 체크포인트는 건너 뛰지 않을 생각이다.
    - 기연이가 체크포인트 한 개를 건너뛰면서 달릴 수 있다면, 과연 달려야 하는 최소 거리는 얼마일까?
    - 참고로, 마라톤 대회는 수원시내 한복판에서 진행될 예정이기 때문에 거리는 “맨하탄 거리”로 측정한다. 위치(X1, Y1)와 위치(X2, Y2)의 거리는 |X1-X2| + |Y1-Y2|이다. (|X|는 절대값 기호이다)
- algorithm
    - totalsum - maxMove
    - move difference is (x0,y0) -> (x1,y1) -> (x2,y2) -  (x0,y0) -> (x2,y2)
- ```make marathon```

# 4. 콜타르 채우기
- make coaltar
- O(NlogN) : coalTar.py
- O(N) : coalTar2.py

# 5. histogram  : 제일 큰 직사각형 만들기
- make histogram

# 6. 2022년 SW역량 4회차 기출문제 2번 : 머그컵
- problem:
  - 입력은 출발점에서 가게까지의 거리와 머그컵의 가격이 주어진다. 
  - 구매 조건
    - 현재 가게의 가격보다 다음 방문할 가게에 더 싼 머그컵이 있다면 가격이 싼 첫 번째 가게에서 구매한다.
    - 방문할 다음 가게에 더 싼 머그컵이 없다면 현재 가게에서 구매한다.
    - 마지막 가게인 경우 다음 가게가 없으므로 그 가게에서 구매한다. 
  - 설명 : 
    - 첫 번째 Test Case의 경우 출발점에서 가까운 순서데로 정리하면
      - 2       5       7         9
      - 15     46     12       7
    - 이 된다.
    - 가격이 가장 싼 경우는 7원 이지만 문제에서는 가격이 싼 첫번째 가게에서 구매한다고 되어 있으므로 구매할 가격을 정리하면 12 12 7 7 이 되어 38원이 정답이 된다.
- http://collab.lge.com/main/pages/viewpage.action?pageId=1652529841
- [mugCup.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/mugCup.py)
- Complexity : O(N)

# 7. 2022년 SW역량 4회차 기출문제 3번 : TV 모델수
- problem:
  - LG는 고객 그룹의 요구조건을 정리하여 출시할 TV의 모델 수를 최소로 하고 싶어한다.
  - 고객 그룹의 요구조건은 최소와 최대로 주어지며 각 (-1000<= 요구조건 <= 1000 )의 값을 가진다.
  - 선호도가 겹치는 경우를 잘 찾아서 최소 모델 수를 구하는 문제
  - 각 고객의 요구조건이 아래와 같을 경우 TV는 요구조건 10과 100으로 하면 2대로 4개 고객그룹의 요구조건을 만족할 수 있다.
- http://collab.lge.com/main/pages/viewpage.action?pageId=1652532232
- [tvModel.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/tvModel.py)
  - Complexity : O(N^2*(N+logN)) = O(N^3)
- [tvModel_2.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/tvModel_2.py) : (got help)
  - []   , [[1,3]]
  - Complexity : O(NlogN + N)

# 8. [ACT] 공주님의 정원
- problem : 
  - 오늘은 공주님이 태어난 경사스러운 날이다. 왕은 이 날을 기념하기 위해 늘 꽃이 피어있는 작은 정원을 만들기로 결정했다.
  - 총 N개의 꽃이 있는데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다. 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다. (올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있음)
  - 이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.
    1. 공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
    2. 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다.
  - N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오.
- <제약조건>
  - 전체 테스트 데이터의 20%는 N≤30
  - 전체 테스트 데이터의 50%는 N≤10,000
- http://collab.lge.com/main/pages/viewpage.action?pageId=1662689380
- [princess.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/princess.py)  <- 3번째 문제의 답은 3이어야 정상임. 틀림
  - data : https://github.com/cheoljoo/problemSolving/blob/master/2022/princess.data
- [princess2.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/princess2.py)
  - make princess2  답은 3
- algorithm :
  - 먼저 값이 0일때를 걸르고 , 
  - 이후에는 위의 'TV 모델수' 문제로 푼다.  <- 이렇게 풀면 안됨. slide window를 사용하는게 맞을 듯!  <- 이건 아님
  - princess2.py로 sort를 한 후에 max 기준으로 찾으면서 내부에 포함된 것은 skip 하며 count한다. 
    - 1. 전의 max의 내부에 포함된 것은 skip
    - 2. 더 큰게 있다면 그 중에서 max를 찾아서 1번을 다시 수행  (sol += 1)
    - 3. 다 끝나면 sol이 답
- algorithm 2 : 강영규 씨
  - 365일에 창안
  - Input을 365의 dictionary로 최장만 기억
  - for 문을 돌때 365일을 0 ~ 364까지 loop를 하여 , sort하지 않고 처리
  - [princess3.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/princess3.py)

# 9. [ACT] 참외 밭
- problem :
  - 시골에 있는 태양이의 삼촌 댁에는 커다란 참외밭이 있다. 문득 태양이는 이 밭에서 자라는 참외가 도대체 몇 개나 되는지 궁금해졌다. 어떻게 알아낼 수 있는지 골똘히 생각하다가 드디어 좋은 아이디어가 떠올랐다. 유레카! 1㎡의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있다. 이를 위하여 1㎡의 넓이에 자라는 참외의 개수를 헤아린 다음 참외밭의 넓이를 구하고자 하였다. 참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형으로 구성된다. 또한 밭의 경계(6개의 변으로 이루어진 다각형)는 계산이 편하도록 모두 동서 방향이거나 남북 방향으로만 이루어 지고 사선 방향으로는 절대 이루어지지 않는다. 이때 밭의 크기를 측정하려면 한 모퉁이에서 출발하여 6면의 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하여야 한다.
  - 예를 들어 참외밭이 위 그림과 같은 모양이라고 하자. 편의상 그림에서 오른쪽은 동쪽, 왼쪽은 서쪽, 아래쪽은 남쪽, 위쪽은 북쪽이라 한다면. 이 그림의 좌측상단 꼭지점에서 출발하여, 반시계방향으로 남쪽으로 30m, 동쪽으로 60m, 남쪽으로 20m, 동쪽으로 100m, 북쪽으로 50m, 서쪽으로 160m 이동하면 6개의 변을 지나서 다시 출발점으로 되돌아가게 된다. 이때 지나온 변의 길이를 이용하여 참외밭의 면적을 구하면 참외밭 면적은 6800㎡이다. 만약 1㎡의 넓이에 자라는 참외의 개수가 7개라고 한다면, 이 밭에서 자라는 참외의 개수는 47600으로 계산될 수 있다.
  - 1㎡의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 6개의 각 변의 길이를 임의의 한 꼭지점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어질 때 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오. (주의: 참외밭의 둘레를 구하는 것이 아니라 면적을 구해야 함)
  - 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 표시한다.
- http://collab.lge.com/main/pages/viewpage.action?pageId=1662701118
- [kmelon.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/kmelon.py) : make kmelon
- algotithm : 
  - 처음을 (0,0)으로 set하여 그림을 그리고 , 각 9개의 점 중에서 없는 점을 구하고 없는 점에서의 작은 사각형을 구해서 뺀다.

# 10. [ACT] 사회적 거리두기
- problem :
  - 농부 John은 전염성이 높은 COWVID-19이 발생한 이후, 소들의 건강이 걱정되었다. 
  - 병의 전염을 막기 위해서, 농부 John의 N마리 소들은 '사회적 거리두기'를 실행하기로 결정하고 농장 전체에 흩어졌다. (2<=N<=105)
  - 농부 John의 농장은 1차원 직선의 모양으로, M개의 서로 분리된 구간의 방목할 잔디가 구성되어 있다. (1<=M<=105)
  - 소는 D의 값을 최대화하기 위해 각각 잔디구간의 정수 지점에 위치하려고 한다. 여기서 D는 가장 가까운 소 두 마리 사이의 거리를 말한다. 소가 D의 가능한 가장 큰 값을 가질수 있도록 도와주자.
  - (입력 예시에 대한 상황이 아래 '부가정보'에 그림으로 잘 표현되어 있다. 해당 내용을 참고하자.)
- input :
  - 첫째 줄에는 N과 M이 주어진다. (2<=N<=105, 1<=M<=105)
  - 다음 M개 줄에는 잔디구간을 나타내는 두개의 정수 a,b가 주어진다.(0<=a<=b<=1018)
  - 구간이 겹치거나 같은 지점에서 만나는 경우는 존재하지 않는다. 그리고 소들은 각 구간의 끝지점에도 서있을 수 있다.
- output :
  - 가능 최대값 D를 출력하라. 모든 소들의 쌍은 D이상 떨어져 있어야 한다.
  - 모든 입력은 0보다 큰 D값이 항상 존재한다.
- ```
    5 3
    0 2
    4 7
    9 9
    => 답 2
  ```
- http://collab.lge.com/main/pages/viewpage.action?pageId=1669212041
- [socialDistance.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/socialDistance.py) : make socialDistance
- algotithm : 
  - 제일 작은 distance : 전체 cow가 위치할수 있는 땅  / cow 수   or 1
  - 최대 distance : (위치할수 있는 땅 + 빈땅 )의 최대값 or M
  - binary search : N
  - O(NlogN)
    - O ( N log 10^18 )  :  log 10^18 이 너무 크려나요?   18 / log2 = 59.x   이므로 max 60번 계산   => 계산 MAX : 10^5 * 60

## 11. event - 사은품
- Description
  - N 명의 사람들에 대해 M개의 사은품을 나눠주려 한다. (1 <= N, M <= 5000)
  - 각 사은품에는 1 부터 M까지 번호가 하나씩 부여되어 있다. 각 사람들은 자신들이 원하는 1순위 사은품과 2순위 사은품의 번호를 적어 제출한다.
  - 아래의 규칙대로 사은품을 수령한다.
    - 사람들은 순서대로 사은품을 받는다.
    - 1순위의 사은품이 남아있을 경우에는 1순위 사은품을 받고,
    - 1순위 사은품이 없을 경우에는 2순위 사은품을 받고,
    - 2순위의 사은품마저 없을 경우에는 사은품을 받지 못 한다.
```
1번째 사람부터 N번째 사람까지 사은품을 받는 경우,
2번째 사람부터 N번쨰 사람까지 사은품을 받는 경우,
...
N-1번째 사람부터 N번째 사람까지 사은품을 받는 경우,
그리고 마지막으로 N번째 사람만 사은품을 받는 경우에 대해 총 선물받은 사은품의 개수를 구하라.
```
- Input
  - 첫번째 줄은 N 과 M을 입력 받는다.
  - 그 다음 N개의 줄에서 각각 사람들의 1순위와 2순위 사은품 번호를 입력 받는다.
- Output
  - 각 줄에 경우 별로 받을 수 있는 총 사은품 숫자를 출력한다.
  - 첫번째 사람부터 N번째 사람까지 사은품을 받는 경우
  - 두번째 사람부터 N번째 사람까지 사은품을 받는 경우
  - ...
  - N-1번째 사람부터 N번째 사람까지 사은품을 받는 경우
  - N번째 사람부터 N번째 사람까지 사은품을 받는 경우
- http://collab.lge.com/main/pages/viewpage.action?pageId=1672640242&focusedCommentId=1680178985
- [event.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/event.py) : python3 event.py

# 11. warehouse - 창고
- Description
  - 4개의 창고에 제품을 보관하고 있다.
  - 4개의 창고에 같은 수의 제품을 보관하기 위해 제품을 이동 시키려고 한다.
  - 제품의 이동은 아래와 같은 규칙을 따른다.
    1. 제품 수가 많은 창고에서 제품 수가 적은 창고로 옮길 수 있다.
    2. 제품 수가 적은 창고의 제품 수를 n 이라고 하였을 때, n/2 만큼 옮겨야 한다.
    3. n이 홀수일 때는 나누었을 때의 나머지는 버린다.
  - 각 창고의 제품 수(n1, n2, n3, n4)를 입력 받는다. 1 <= n1, n2, n3, n4 <= 50
  - 이때 최소 이동 숫자를 입력하여라.
  - 4개의 창고에서 같은 수의 제품을 보관할 수 없다면 -1을 출력하라.
- Input
  - 각 창고의 제품 수(n1, n2, n3, n4) 1 <= n1, n2, n3, n4 <= 50
- Output
  - 제품 수가 같아지기 위한 최소 이동 숫자 (불가능하면 -1)
- - http://collab.lge.com/main/pages/viewpage.action?pageId=1672640242&focusedCommentId=1680178985
- [warehouse.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/warehouse.py) : python3 warehouse.py

# burstBallon : 풍선 터트리기
- http://collab.lge.com/main/pages/viewpage.action?pageId=1809798914
- https://school.programmers.co.kr/learn/courses/30/lessons/68646?language=python3
- [burstBallon.py](https://github.com/cheoljoo/problemSolving/blob/master/2022/burstBallon.py) : python3 burstBallon.py
