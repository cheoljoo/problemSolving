# 3311. Construct 2D Grid Matching Graph Layout : Runtime 354ms Beats 44.79%
class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        near = defaultdict(set)
        for a, b in edges:
            near[a].add(b)
            near[b].add(a)
        #print(near)
 
        # linear case
        if len(edges) == n - 1:
            start = 0
            # 시작 노드 찾기 : 주변에 올 수 있는 노드가 1개인 것 (선형)
            for k, v in near.items():
                if len(v) == 1:
                    start = k
                    break
            res = []
            res.append(start)
            res.append(near[start].pop())
            i = 1
            while len(res) < n:
                # 마지막 노드 주변에 올 수 있는 노드에서 마지막 노드 왼쪽에 있는 노드를 제거하여 추가될 노드를 결정
                v = near[res[i]] - {res[i - 1]}
                res.append(v.pop())
                i += 1
 
            return [res]
 
        # NOT linear case
        res = [[]]
        start = 0
        # 시작 노드 찾기 : 주변에 올 수 있는 노드가 2개인 것 (2차원의 꼭지점)
        for k, v in near.items():
            if len(v) == 2:
                start = k
                break
 
        # 처음 4개 사각형 노드 찾기
        res[0].append(start)
        l = list(near[start])
        res[0].append(l[0])
        res.append([l[1]])
        v = near[res[0][1]] & near[res[1][0]] - {res[0][0]}
        res[1].append(v.pop())
        #print(res)
 
        j = 1
        # 꼭지점에 도달 할 때 까지 반복 (처음 2개의 행)
        while not (len(near[res[0][j]]) == 2 or len(near[res[1][j]]) == 2):
            # 가능한 노드에서 왼쪽, 아래쪽 노드를 제거하면 오른쪽 노드만 유일하게 남음
            v = near[res[0][j]] - {res[0][j - 1]} - {res[1][j]}
            res[0].append(v.pop())
 
            v = near[res[0][j + 1]] & near[res[1][j]] - {res[0][j]}
            res[1].append(v.pop())
            j += 1
 
        c = len(res[0]) # 열 개수
        r = int(n / c)  # 행 개수
 
        for i in range(2, r):
            for j in range(c):
                # i행 j 열의 값을 결정하기 위해, i - 1 행 j열의 값 주변에 존재하는 값 중 결정된 값들을 제거하면 i행 j열에 존재해야 하는 값만 남음
                # i - 1 행 j 열 주변에 존재하는 값 중 i - 2 행 j 열의 값 제거 (위쪽 값 제거)
                tmp = near[res[i - 1][j]] - {res[i - 2][j]}
                if j > 0:
                    # 왼쪽 값이 있을 경우 제거
                    tmp = tmp - {res[i - 1][j - 1]}
                if j < c - 1:
                    # 오른쪽 값이 있을 경우 제거
                    tmp = tmp - {res[i - 1][j + 1]}
                if j == 0:
                    # 첫 번째 열 인 경우 새로운 행으로 값을 추가
                    res.append([tmp.pop()])
                else:
                    # 첫 번째 열이 아닌 경우 i행에 값을 추가
                    res[i].append(tmp.pop())
 
        return res