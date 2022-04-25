import sys

class Solution:
    def do(self,histo):
        # 여기서부터 작성
        data = []
        count = 1
        start = 0
        for i in range(1,len(histo)):
            if histo[i-1] == histo[i]:
                count += 1
            else :
                data.append([histo[i-1],start,count])
                start = i
                count = 1
        data.append([histo[-1],start,count])
        print(histo)
        print(data)

        data.sort(reverse=True)
        print(data)
        

        mx = 0
        for i in range(len(data)):
            v = data[i][0]
            c = data[i][1]
            count = c
            for j1 in reversed(range(1,i)):
                if data[j1][0] >= v:
                    count += data[j1][1]
                else : 
                    break
            for j1 in range(i+1,len(data)):
                if data[j1][0] >= v:
                    count += data[j1][1]
                else : 
                    break
            mx = max(mx,v*count)
        #print(data)
        print(mx)

        # 출력하는 부분
 
def input_data():
    readl = sys.stdin.readline
    histo = []
    N = int(readl())
    for _ in range(N):
        cnt = int(readl())
        histo.append(list(map(int,readl().split())))
    return N, histo

# 입력 받는 부분
N, histo = input_data()
#print(N,histo)
 

for i in range(N):
    A = Solution()
    A.do(histo[i])
 
