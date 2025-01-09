# 3376. Minimum Time to Break Locks I : Runtime 6837 ms Beats 15.81%

class Solution:
    def go(self,index,remainCount,timeCount ,energy,x,txt):
        '''
        level:
        remainCount : 건너뛴 것 , 건너뛴 것은 뒤에서 처리할때는 모두 1번으로 처리되고 그 만큼 x 값도 증가하면 된다.
        timeCount : 지금까지의 흐른 시간
        '''
        print(txt,'go in','i',index,'e',energy,'x',x,'k',self.k,'t',timeCount,'r',remainCount,'ans',self.ans)
        if timeCount >= self.ans:
            return
         
        skipRemainCount = remainCount + 1
        skipTimeCount = timeCount
        skipEnergy = energy
        skipX = x
 
        # select and go
        if self.strength[index] <= energy :
            print(txt,'go case1','i',index,'e',energy,'x',x,'k',self.k,'t',timeCount,'r',remainCount)
            timeCount += remainCount + 1
            x += self.k
            x += remainCount * self.k
            energy = x
        else:
            print(txt,'go case2','i',index,'e',energy,'x',x,'k',self.k,'t',timeCount,'r',remainCount)
            t = self.strength[index] - energy
            if energy:
                timeCount += 1   # 앞의 1은 초기 energy 만큼 쓴 것
            print('t',t,'tC',timeCount,'x',x)
            timeCount += t//x + 1   # 뒤의 1은 나머지가 있는 경우를 고려
            print('t',t,'tC',timeCount,'x',x,t%x)
            if t%x == 0:
                timeCount -= 1  # 나머지가 없는 경우
            x += self.k
            print('t',t,'tC',timeCount,'r',remainCount,'x',x)
            timeCount += remainCount
            x += remainCount * self.k
            print('t',t,'tC',timeCount,'x',x)
            energy = x
        print(txt,'go end','i',index,'e',energy,'x',x,'k',self.k,'t',timeCount,'r',remainCount,'ans',self.ans)
        if index == self.S-1:
            if timeCount < self.ans:
                self.ans = timeCount
                print('set ans',self.ans)
            return
        else:
            self.go(index+1,0,timeCount,energy,x,'selected')
             
        # not select and go
        if index != self.S-1 :  # 마지막 index는 무조건 선택해야 한다. 선택 안하면 다음이 없다.
            self.go(index+1,skipRemainCount,skipTimeCount,skipEnergy,skipX,'skip')
         
 
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        # use permutation
        ans = math.inf
        for permutation in permutations(strength):
            # print(permutation)
            time = 0
            x = 1
            energy = 0
            for node in permutation:
                if energy < node: # nothing
                    if energy:
                        time += 1  # energy 1번 사용
                    t = node - energy
                    time += t//x +1   # 나머지 있는 것으로 가정
                    if t%x == 0:
                        time -= 1  # 나머지가 없을 경우
                else:
                    time += 1
                x += k
                energy = x
                # print('per',permutation,'node',node,'e',energy,'x',x,'k',k,'t',time,'ans',ans)
            if time < ans:
                ans = time
        return ans
 
        strength.sort()
        time = 0
        energy = 0
        x = 1
        i = 0
        self.strength = strength
        self.S = len(strength)
        self.k = k
        self.ans = math.inf
        # new : all cases  1 <= n <= 8
        print('s',strength,'i',i,'e',energy,'x',x,'k',k,'t',time)
        self.go(0,0,0,0,1,'start')
        return self.ans
 
 
 
        # old
        # [3, 6, 7, 18, 22, 50]  > 뽑는 순서 3 , 7, 6, 50 , 18
        # if 첫번째 값 <= x 일때는 무조건 처리
        # else [18,50] x17 일때이므로 이때는 다음이 x20이 될 것이다. x17일때 2,3 / x21일때 1,3으로 3이 같으므로 3자리가 처리가 될때까지 처리하고 다음을 한다.
        # n <= 8 이므로 모든 경우를 다 조사를 해야 한다.
        while strength:
            if energy < strength[0]: # nothing
                t = strength[0] - energy
                if t % x == 0:
                    print('case1','s',strength,'i',i,'e',energy,'x',x,'k',k,'t',time)
                    energey = strength[0]
                    print('e',energy,strength[0])
                    time += t // x
                else:
                    print('case2','s',strength,'i',i,'e',energy,'x',x,'k',k,'t',time)
                    energy += ((t // x) + 1 ) * x
                    time += t // x + 1
            else:
                if energy >= strength[-1]:
                    print('case3','s',strength,'i',i,'e',energy,'x',x,'k',k,'t',time)
                    i = len(strength)-1
                else:
                    print('case4','s',strength,'i',i,'e',energy,'x',x,'k',k,'t',time)
                    i = bisect_left(strength,energy)
                    if strength[i] != energy:
                        i = i - 1
                strength.pop(i)
                x += k
                energy = x
                if not strength:
                    return time
                time += 1
            print('s',strength,'i',i,'e',energy,'x',x,'k',k,'t',time)
        return time