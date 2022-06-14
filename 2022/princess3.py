from re import X
import sys
from collections import defaultdict
  
  
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
calendar = defaultdict(int)
for x in info:
    a = x[0]*100 + x[1]
    if(calendar[a] < x[2]*100 + x[3]):
        calendar[a] = x[2]*100 + x[3]
print(calendar)
ed = 300
i = 101
while i < 301:
    if(calendar[i] > ed):
        ed = calendar[i]
    if(i%100 == 31):
        i = i//100*100 + 100
    i += 1
if(ed > 301):
    sol += 1
    while ed <= 1130:
        tmp  = ed
        while i <= ed:
            if(calendar[i] > tmp):
                tmp = calendar[i]
            if(i%100 == 31):
                i = i//100*100 + 100
            i += 1
        if(tmp == ed):
            sol = -1
            break
        elif(tmp > ed):
            sol += 1
            ed = tmp
 
sol += 1
# 출력하는 부분
print(sol)