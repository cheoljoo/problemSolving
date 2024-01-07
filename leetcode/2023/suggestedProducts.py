# https://leetcode.com/problems/search-suggestions-system/solution/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        counts = {}
        m = []
        start = 0
        flag = 0
        # print(products,searchWord)
        for i in range(len(products)):
            # print(start,i)
            if start > len(products[i]):
                i -= 1
                break
            if start > 0  and products[i][start-1] != searchWord[start-1]:
                i -= 1
                break
            while start < len(products[i]) and start < len(searchWord) and products[i][start] == searchWord[start]:
                start += 1
            if start not in counts:
                counts[start] = []
            counts[start].append(i)
            m.append(start)
        pl = i
        # for i,v in counts.items():
        #     print(i,v)
        # print("pl:",pl,"m:",m)
        for i in range(pl+1,len(products)):
            while  start >= len(products[i]) or start >= len(searchWord):
                start -= 1
            while start > 0 and products[i][start-1] != searchWord[start-1]:
                start -= 1
            if start not in counts:
                counts[start] = []
            counts[start].append(i)
            m.append(start)
            
        # for i,v in counts.items():
        #     print(i,v)
        # print(m)
        # print(len(m),len(products))

        ans = [ [] for _ in range(len(searchWord))]
        start = 0
        for i in range(1,len(searchWord)+1):
            while start < len(m):
                if m[start] >= i:
                    break
                start += 1
            if start < len(m) and m[start] >= i:
                ans[i-1].append(products[start])
            if start+1 < len(m) and m[start+1] >= i:
                ans[i-1].append(products[start+1])
            if start+2 < len(m) and m[start+2] >= i:
                ans[i-1].append(products[start+2])
            
                
        return ans

    