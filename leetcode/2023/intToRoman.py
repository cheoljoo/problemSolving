class Solution:
    def intToRoman(self, num: int) -> str:
        self.t = {}
        self.t[1] = 'I'
        self.t[2] = 'II'
        self.t[3] = 'III'
        self.t[4] = 'IV'
        self.t[5] = 'V'
        self.t[6] = 'VI'
        self.t[7] = 'VII'
        self.t[8] = 'VIII'
        self.t[9] = 'IX'
        self.t[10] = 'X'
        self.t[20] = 'XX'
        self.t[30] = 'XXX'
        self.t[40] = 'XL'
        self.t[50] = 'L'
        self.t[60] = 'LX'
        self.t[70] = 'LXX'
        self.t[80] = 'LXXX'
        self.t[90] = 'XC'
        self.t[100] = 'C'
        self.t[200] = 'CC'
        self.t[300] = 'CCC'
        self.t[400] = 'CD'
        self.t[500] = 'D'
        self.t[600] = 'DC'
        self.t[700] = 'DCC'
        self.t[800] = 'DCCC'
        self.t[900] = 'CM'
        self.t[1000] = 'M'
        self.t[2000] = 'MM'
        self.t[3000] = 'MMM'
        ans = ""
        digit = 1
        while num:
            c = num % 10
            c *= digit
            num //= 10
            digit *= 10
            if c != 0:
                ans = self.t[c] + ans
        return ans
                
        
        