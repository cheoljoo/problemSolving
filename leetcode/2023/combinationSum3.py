class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.go(k,0,0,n,[])
        return self.ans
    def go(self,k,mn,sm,n,ll):
        if k == 0:
            if sm == n:
                self.ans.append(ll)
            else :
                return
        for i in range(mn+1,9+1):
            l = ll.copy()
            l.append(i)
            self.go(k-1,i,sm+i,n,l)
            
            