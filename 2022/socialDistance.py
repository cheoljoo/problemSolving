from re import X
import sys
from collections import defaultdict
  
  
def input_data():
    readl = sys.stdin.readline
    N , M = list(map(int, readl().split()))
    info = [list(map(int, readl().split())) for _ in range(M)]
    return N, M , info
  
  
sol = -1
# 입력받는 부분
N, M , info = input_data()

  
# 여기서부터 작성
info.sort()
maxP = info[M-1][1]
print(N,M,info,maxP)

def check(d):
    i = 0
    c = 1 # cow
    p = info[0][0] # position
    while i < M and c < N:
        c += 1
        p += d
        if p <= info[i][1]:
            print("-",N,M,c,i,p)
            continue
        else :   # p > info[i][1]:
            i += 1
            while i < M:
                if p <= info[i][1]:
                    break
                i += 1
            if i >= M:
                return False
            if p < info[i][0]:
                p = info[i][0]        
        print("e",N,M,c,i,p)
    if c >= N:
            return True
    return False

s = 1
e = maxP // N + 1
mx = 0
while s <= e:
    mid = (s + e) // 2
    print("check:",s,mid,e)
    d = check(mid)
    if d :
        s = mid + 1
        mx = max(mx,mid)
    else :
        e = mid -1
print(mx)
# print("2",check(2))
# print("1",check(1))
# print("3",check(3))
# print("4",check(4))