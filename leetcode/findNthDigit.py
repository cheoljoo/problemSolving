class Solution:
    def findNthDigit(self, n: int) -> int:

        if n <= 9 :
            return n
        digit = 1
        kk= {}
        for k in range(12):
            kk[k] = k*9*10**(k-1)
        while n:
            if n - kk[digit] < 0:
                break
            n -= kk[digit]
            digit += 1
        
        n -= 1
        k = n // digit
        m = n % digit
        s = 10**(digit-1) + k
        # print(digit,n,k,m,s)
        return str(s)[m]