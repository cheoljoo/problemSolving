import sys
import heapq
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = -1

# 입력받는 부분
N, info = input_data()

# 여기서부터 작성
print(info)

#binary search
mx = -math.inf
mn = math.inf
for i in range(N):
    if mx < info[i][1]:
        mx = info[i][1]
    if mn > info[i][1]:
        mn = info[i][1]
while True:
    mid = (mx+mn)//2
    if mx - mn <= 2:
        break
stack= []
print(q)
for i in range(len(q)):
    if len(stack) >= 2:
        pass




                                 
# 출력하는 부분
print(sol)
