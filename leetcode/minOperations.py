class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        lstack = []
        rstack = []
        sol = []
        t = 0
        ans = 0
        endFlag = True
        print(nums,x)
        for v in nums:
            if t + v <= x:
                lstack.append(v)
                t += v
                ans += 1
                if t == x:
                    sol.append(ans)
                    print("x == " , x,"ans:",ans, "sol:",sol,"l:",lstack)
                    endFlag = False
                    break
            else :
                print(t, "<" , x , "v:",v,"ans:",ans, "sol:",sol,"l:",lstack)
                endFlag = False
                break
        if endFlag == True:
            return -1
        for v in reversed(nums):
            sm = 0
            if t+v <= x :
                rstack.append(v)
            else:
                while lstack and sm < v:
                    sm += lstack[-1]
                    t -= lstack[-1]
                    lstack.pop()
                rstack.append(v)
            t += v
            print("t:",t, "x:" , x , "v:",v,"sol:",sol,"l:",lstack,"r:",rstack)
            if t == x:
                sol.append(len(rstack) + len(lstack))
            if v >= x:
                break
        if sol : 
            return min(sol)
        else :
            return -1
            
# [1,1,4,2,3]
# 5
# [2,2,2,2,1,20,3,6]
# 9
# [2,2,2,2,1,7,20,3,6]
# 18
# [5,6,7,8,9]
# 4
# [3,2,20,1,1,3]
# 10
# [5,2,3,1,1]
# 5
# [2,2,2,2,1,7,20,3,6]
# 30

# [6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119]
# 31841
# 6016 11499 12040 16365 24514 28029 35894
# 9119 16945 19801 20408
