# 3311. Construct 2D Grid Matching Graph Layout : Runtime 4598 ms Beats 5.75%
class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        node = defaultdict(set)
        for f,t in edges:
            d[f] += 1
            d[t] += 1
            node[f].add(t)   # remove()
            node[t].add(f)
        count = defaultdict(int)
        cntl = defaultdict(set)
        for n,c in d.items():
            count[c] += 1
            cntl[c].add(n)
        R = 0
        C = 0
        # print('cntl',cntl)
        # print('node',node)
        # print('count',count)
        T = []
        if count[1] != 0:
            R = 1
            C = len(edges)+1
            T = [0] * C
            T[0] , T[-1] = list(cntl[1])
            s = T[0]
            cnt = 1
            # print('node',node,'s',s)
            while node[s]:
                t = node[s].pop()
                T[cnt] = t
                node[t].remove(s)
                # print('node',node,'pop',t,'remove',s,T)
                cnt += 1
                s = t
            T = [ T ]
        elif count[4] == 0:
            # 두 줄로 처리 / 왼쪽에서부터 column 단위로 2줄씩 처리 하는 코드로 변경
            R = 2
            C = (count[3]+count[2]) // 2
            s = cntl[2].pop()
            T = [[-1] * C for _ in range(R)]
            T[0][0] = s
            for ss in node[s]:
                if ss in cntl[2]:
                    T[1][0] = ss
                    node[s].remove(ss)
                    node[ss].remove(s)
                    break
            # print('T',T)
            for c in range(C):
                if T[0][c] != -1:
                    s = T[0][c]
                    continue
                s = T[0][c-1] if c>0 else T[0][0]
                # print('c',c,'s',s,'node-s',node[s],T)
                # print('node',node)
                if c==0 or c==C-1:  #꼭지점
                    for n2 in node[s]:
                        if n2 in cntl[2]:
                            T[0][c] = n2
                            node[s].remove(n2)
                            node[n2].remove(s)
                            # print('case7:',c,s,n2,node,T)
                            s = n2
                            break
                    s = T[1][c-1] if c>0 else T[1][0]
                    for n2 in node[s]:
                        # print(n2,node,s,c,T[0][c])
                        if n2 in cntl[2] and n2 in node[T[0][c]]:
                            T[1][c] = n2
                            node[s].remove(n2)
                            node[n2].remove(s)
                            node[T[0][c]].remove(n2)
                            node[n2].remove(T[0][c])
                            # print('case7.2:',c,s,n2,node,T)
                            s = n2
                            break
                else: #테두리
                    for n2 in node[s]:
                        if n2 in cntl[3]:
                            T[0][c] = n2
                            node[s].remove(n2)
                            node[n2].remove(s)
                            # print('case8:',c,s,n2,node,T)
                            s = n2
                            break
                    s = T[1][c-1] if c>0 else T[1][0]
                    for n2 in node[s]:
                        # print('n2',n2,node,s,c,T)
                        if n2 in cntl[3] and n2 in node[T[0][c]]:
                            T[1][c] = n2
                            node[s].remove(n2)
                            node[n2].remove(s)
                            node[T[0][c]].remove(n2)
                            node[n2].remove(T[0][c])
                            # print('case8.2:',c,s,n2,node,T)
                            s = n2
                            break
        else:
            for i in range(1,count[4]+1):
                if count[4] % i == 0:
                    r = i
                    c = count[4] // i
                    if (r+c)*2 == count[3]:
                        R = r+2
                        C = c+2
            # 끌줄의 경우는 cntl[3]에서 찾고 ,  중간에 대해서는 cntl[4]에서 찾는다
            ##  테두리를 먼저 채우자.
            visited = set()
            T = [[-1] * C for _ in range(R)]
            s = cntl[2].pop()
            T[0][0] = s
            visited.add(s)
            for second in node[s]:
                flag = True
                path = [s,second]
                nxt = second
                for i in range(max(R,C)-2):
                    # print('path',path,'nxt',nxt,'max',max(R,C),'node[second]',node[second])
                    ans = -1
                    for tn in node[nxt]: # temp node
                        if tn in path:
                            continue
                        if i == (max(R,C)-3):
                            if tn in cntl[2]:
                                ans = tn
                                break
                        else:
                            if tn in cntl[3]:
                                ans = tn
                                break
                    if ans == -1:
                        flag = False
                        break
                    nxt = ans
                    path.append(ans)
                    # print('path',path,'ans',ans,'flag',flag)
                if flag:
                    # print('path',path,'ans',ans,'flag',flag,R,C,'second',second)
                    if R > C:
                        T[1][0] = second
                    else :
                        T[0][1] = second
                    node[s].remove(second)
                    node[second].remove(s)
                    break
            visited.add(second)
            # print('T',T,'node',node,R,C)
            for r in range(R):
                s = T[r-1][0] if r>0 else T[0][0]
                for c in range(C):
                    if T[r][c] != -1:
                        s = T[r][c]
                        continue
                    # print(r,c,'s',s,'node-s',node[s],'T',T,'visited',visited)
                    # print('node',node)
                    if (r==0 or r==R-1) and (c==0 or c==C-1):  #꼭지점
                        for n2 in node[s]:
                            if n2 in cntl[2] and n2 not in visited:
                                T[r][c] = n2
                                node[s].remove(n2)
                                node[n2].remove(s)
                                visited.add(n2)
                                # print('case1:',r,c,s,n2,node)
                                s = n2
                                break
                    elif r==0 or c==0 or r==R-1 or c==C-1: #테두리
                        for n2 in node[s]:
                            if r != 0:
                                up = T[r-1][c]
                                if n2 not in node[up]:
                                    continue
                            if n2 not in cntl[4] and n2 not in visited:
                                T[r][c] = n2
                                node[s].remove(n2)
                                node[n2].remove(s)
                                visited.add(n2)
                                # print('case2:',r,c,s,n2,node)
                                s = n2
                                break
                    else:  # 가운데
                        for n2 in node[s]:
                            if r != 0:
                                up = T[r-1][c]
                                if n2 not in node[up]:
                                    continue
                            if n2 in cntl[4] and n2 not in visited:
                                T[r][c] = n2
                                node[s].remove(n2)
                                node[n2].remove(s)
                                visited.add(n2)
                                # print('case3:',r,c,s,n2,node)
                                s = n2
                                break
        return T