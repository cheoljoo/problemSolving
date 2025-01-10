# timeout

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sl = list(s)
        for s,e,d in shifts:
            for i in range(s,e+1):
                if d == 1:
                    if sl[i] == 'z':
                        sl[i] = 'a'
                    else:
                        sl[i] = chr(ord(sl[i])+1)
                else:
                    if sl[i] == 'a':
                        sl[i] = 'z'
                    else:
                        sl[i] = chr(ord(sl[i])-1)
        return ''.join(sl)