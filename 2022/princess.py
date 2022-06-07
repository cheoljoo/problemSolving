import sys
import math
 
 
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    info.sort()
    # check empty slot
    d = []
    mx = info[0][0]*1000 + info[0][1] 
    for i in range(N):
        f = info[i][0]*1000 + info[i][1] 
        e = info[i][2]*1000 + info[i][3] 
        if f < 12*1000 + 1 and e > 3*1000 + 1 : 
            d.append([f, e - 1])
            if f > mx :
                print("empty",0)
                quit()
            else :
                if mx < e:
                    mx = e
    if mx <= 11*1000 + 30 :
        print("end",0)
        quit()
    return N, d
 
 
sol = 0
# 입력받는 부분
N, d = input_data()
d.sort() 
# 여기서부터 작성
end = -math.inf
if d[0][0] > 3*1000 + 1:
    print(sol)
    quit()

print(d)
for i in range(len(d)):
    print(end,i,sol,d)
    if d[i][0] > end :
        sol += 1
        end = d[i][1]
    if end > d[i][1]:
        end = d[i][1]
    
 
# 출력하는 부분
print(sol)


# 6
# 1 1 2 28
# 12 1 12 15
# 1 1 4 31
# 1 1 5 31
# 6 1 8 31
# 6 10 12 10
# => empty 0

# 6
# 1 1 2 28
# 12 1 12 15
# 1 1 5 31
# 1 1 6 1
# 6 1 8 31
# 6 10 11 30
# => end 0

# 6
# 1 1 2 28
# 12 1 12 15
# 1 1 5 31
# 1 1 6 1
# 6 1 8 31
# 6 10 12 10
# => 2