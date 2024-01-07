from unittest import TestCase


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        sign = 1 # 1 is plus (positive)
        table = []
        for i in range(32):
            table.append(1 << i)
        if dividend < 0 and divisor < 0 :
            dividend *= -1
            divisor *= -1
            sign = 1
        elif dividend < 0 and divisor > 0 :
            dividend *= -1
            sign = -1
        elif dividend > 0 and divisor < 0 :
            divisor *= -1
            sign = -1
            
        for i in reversed(range(32)):
            divisorShift = divisor << i
            if dividend < divisorShift:
                continue
            while dividend >= divisorShift:
                quotient += 1 << i
                dividend -= divisorShift
            if dividend < divisor:
                break
        if quotient > 2**31:
            quotient =  2**31
        if sign == -1:
            return quotient * (-1)
        elif quotient >  2**31 -1:
            quotient =  2**31 -1
        return quotient

# TestCase
# 10
# 3
# 7
# -3
# -7
# -3
# 2147483647
# 1
# -2147483648
# 1
# 2147483647
# -1
# -2147483648
# -1
# 2147483647
# 2
# 2147483647
# -3