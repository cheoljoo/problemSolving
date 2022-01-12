# year 2022

## 집합은 a, b를 싫어해
- https://codeup.kr/problem.php?id=2128
- cd 2022
- make 1
- 통과 했습니다.  ( 1-lowMem3.py )
  - 고성대 책임님이 지적해 주신 것이 맞았습니다. 앞으로 int ( ? / ? ) 으로 하면 안되고 , // operator을 사용해서 몫을 int로 바로 구해야 문제 없습니다.
  - int ( ? / ? ) 으로 하면 ?/? 에서 float로 변경을 할때 많은 뒤의 상세한 값들을 잃어버리게 된다고 합니다. 그래서 , 몫을 구할때  // operator를 써야 정확하게 integer의 몫을 구할수 있다고 합니다.

### virtualenv (numpy memory_profiler)
- virtualenv a
- source a/bin/activate
- pip install numpy
- pip install memory_profiler
- pip install mkdocs

### docstirngs
- pip install mkdocs
- pip install mkdocstrings
- pip install mkdocs-material

- command
    - mkdocs new [yours]
    - cd [yours]
    - copy your files and change yml and others
    - mkdocs build

- http://lotto645.lge.com:8088/cheoljoo.lee/code/problemSolving/2022/docstring/site/my_page/

### 1st trial - dictionay version
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


### 2nd trial - numpy version
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


### memory difference with big N
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



## 색종이
- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=712&sca=2060#n
- jungol에서는 numpy와 같은 추가적인듈을 사용하면 안된다.

- cd 2022
- make 2

