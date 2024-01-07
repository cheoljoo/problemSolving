class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0
        while cnt < len(data):
            cb = self.countBytes(cnt,data)
            if cb == -1:
                return False
            cnt += cb
            if cnt > len(data):
                return False
        return True
    def countBytes(self,cnt,data):
        if data[cnt] // 2**7 == 0:
            return 1
        elif data[cnt] // 2**5 == 6:
            if cnt+1 >= len(data):
                return -1
            if data[cnt+1] // 2**6 == 2:
                return 2
            else :
                return -1
        elif data[cnt] // 2**4 == 14:
            if cnt+2 >= len(data):
                return -1
            if data[cnt+1] // 2**6 == 2 and data[cnt+2] // 2**6 == 2 :
                return 3
            else:
                return -1
        elif data[cnt] // 2**3 == 30:
            if cnt+3 >= len(data):
                return -1
            if data[cnt+1] // 2**6 == 2 and data[cnt+2] // 2**6 == 2 and data[cnt+3] // 2**6 == 2 :
                return 4
            else:
                return -1
        return -1