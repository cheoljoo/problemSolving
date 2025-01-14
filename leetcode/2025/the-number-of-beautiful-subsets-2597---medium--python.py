# Runtime 8401 ms Beats 10.36% / Memory 157.14 MB Beats 9.71%
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        subsets = []
        for i in range(2,len(nums) + 1):
            subsets.extend(itertools.combinations(nums, i))
        # print("Subsets:", subsets)
        ans = len(nums)
        for subset in subsets:
            d = set()
            for item in subset:
                if item - k not in d:
                    d.add(item)
                else:
                    break
            else:
                # for 문에서는 break로 빠지지 않는 것은 for else로 처리되게 된다.
                # print(subset,'ans',ans,'k',k)
                ans += 1
        return ans
        d = {}
        N = len(nums)
        ans = N
        total = 2**N - 1
        for n in nums:
            d[n] = 0
        pairs = {}
        for n in nums:
            if n+k in d:
                pairs[n] = n+k
        print('pairs',pairs)
        P = len(pairs)
        if N <= 2:
            total -= P
        else:
            prev = 0
            pCnt = 0
            for p,v in pairs.items():
                if prev == p:
                    pCnt += 1
                # else:
                #     pCnt += 1
                total -= (2**(N-2-pCnt))
                print('total',total,'pCnt',pCnt,'(2**(N-2-pCnt))',(2**(N-2-pCnt)),prev,p,v)
                prev = v
            # ex1) 2,4,6 , (2,4) , (4,6) , (2,4,6)
            # 처음에는 (2,4) 에서 뒤에 올수 있는 것은 null , 6이 올수 있다.
            # 두번째인 (4,6) 에서는 앞의 null , 2가 올수 있는데 , 이 2는 겹치게 되는 것이다.
            # ex2)  2,4,6,10 이라고 하면 
            # 처음의 (2,4) 에 대해서는 6,10으로 만들수 있는 모든 것이 곱해지고
            # 두번째인 (4,6)에 대해서는 2,10으로 된 것이 만들어지나, 2는 첫번째에서 한 것이므로 제외를 해주어얗낟.
            # pairs가 여래 일때 , 첫번째는 빼는 것 없지만, 2번째부터는 앞의 한개씩이 빠지게 되는 것으로 계산을 해주어야 한다. (p)
            #
            # [4,2,5,9,10,3] 일때
            # pairs {2: 3, 3: 4, 4: 5, 9: 10}
            # 앞뒤가 겹치지 않을때는 줄일 필요가 없다.
            #
            # permutation으로 계산을 하면 될 듯...  20! or 2**20 인데 2**20 이 훨씬 작다.
            # 
        return total