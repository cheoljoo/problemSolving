
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


## 1.7. 줄자접기
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=392&sca=3080
- make 5
  
- pass


##  1.8. 잃어버린 괄호
- https://www.acmicpc.net/problem/1541
  - 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
- make 6

- python regular expression : https://www.programiz.com/python-programming/regex


## 뒤집어진 소수
- https://www.acmicpc.net/problem/10859
  - 어제 자다가 알람 시계를 떨어뜨렸는지, 08:15분이 51:80분이 되어 있었다. 그때 나는 디지털로 표시된 어떤 숫자는 180도 뒤집혔을 때도 숫자가 될 수 있다는 걸 깨달았다.
  - 내가 좋아하는 숫자는 소수이다. 당신이 할 일은 주어진 숫자가 소수인지, 뒤집혀서도 소수인지 확인하는 것이다.
- make 7

