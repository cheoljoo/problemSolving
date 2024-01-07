class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        mx = score
        while len(tokens) > 0:
            # print(tokens,score,power,mx)
            mn = tokens[0]
            if power >= mn:
                score += 1
                power -= mn
                mx = max(mx,score)
                tokens.pop(0)
            else:
                if score > 0 and len(tokens) > 0:
                    last = tokens.pop()
                    score -= 1
                    power += last
                else:
                    return mx
        return mx