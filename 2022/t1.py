# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

if __name__ == "__main__":
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    print(b)
    r = 0
    for i in range(N-1):
        print("i",i)
        this = b[i]
        cnt = 0
        for j in range(i+1 , N):
            print("j",j)
            if this > b[j] :
                cnt += 1
            else :
                break
        r += cnt

    print(r)

# 답
# N = int(input())
# A = []
# ans = 0
# for _ in range(N):
#     x = int(input())
#     if not A:
#         A.append(x)
#     else:
#         while A and A[-1]<=x:
#             A.pop()
#         ans += len(A)
#         A.append(x)
# print(ans)

# 5 2 4 2 6 1
# 5 in 2 -> 5,2 (1)
# in 4 -> 5 , 4 (1)
# in 2 -> 5,4,2 (2)
# in 6 -> 6 (0)
# in 1 -> 6,1 (1)