class Solution:
    def minimizeResult(self, expression: str) -> str:
        a = expression.split('+')
        # print(a)
        l = int(a[0])
        r = int(a[1])
        ll = [(1,l,1)]
        start = 1
        remain = 1
        origin = l
        while l :
            remain = origin % (10**start)
            l = origin // (10**start)
            if l == 0:
                break
            ll.append((l,remain,0))
            start += 1

        # print(ll)
        rr = [(r,1,1)]
        start = 1
        remain = 1
        origin = r
        while r :
            remain = origin % (10**start)
            r = origin // (10**start)
            start += 1
            if r == 0:
                break
            rr.append((r,remain,0))
        # print(rr)
        mn = math.inf
        s = ""
        for (vll,vlr,lstart) in ll:
            for (vrl,vrr,rstart) in rr:
                n = vll * (vlr + vrl) * vrr
                if mn > n :
                    mn = n
                    s = ""
                    if lstart != 1:
                        s += str(vll)
                    s += "(" + str(vlr) + "+" + str(vrl) + ")"
                    if rstart != 1:
                        s += str(vrr)
        return s