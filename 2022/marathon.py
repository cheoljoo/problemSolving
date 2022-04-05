import sys
 
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int,readl().split())) for _ in range(N)]
    return N, pos

# 입력 받는 부분
N, pos = input_data()
 
# 여기서부터 작성
 
# 출력하는 부분
#print(pos)
sum = abs(pos[0][0]-pos[1][0]) + abs(pos[0][1]-pos[1][1])
maxMove = 0
for i in range(1,N-1):
    move = abs(pos[i-1][0]-pos[i][0]) + abs(pos[i-1][1]-pos[i][1]) + abs(pos[i][0]-pos[i+1][0]) + abs(pos[i][1]-pos[i+1][1]) - ( abs(pos[i-1][0]-pos[i+1][0]) + abs(pos[i-1][1]-pos[i+1][1]) )
    if maxMove < move:
        maxMove = move
    sum += abs(pos[i][0]-pos[i+1][0]) + abs(pos[i][1]-pos[i+1][1])
    #print(move,maxMove,sum)

sol = sum - maxMove
print(sol)
