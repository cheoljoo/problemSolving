# 1310. XOR Queries of a Subarray
# https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=problem-list-v2&envId=mbbj9re1

from typing import List

class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
      # 중간의 A,B 라고하면 그 것을 항시 계산을 해야한다.
      # 그러므로 , 이것은 한번만 계산하면 될 것으로 생각한다.
      # 
      # 0 ~ A  까지 xor 한 값을 저장한다.
      # A ~ 끝 까지 xor한 값을 저장한다.
      #  [10:100] (10 ~ 99 까지) 경우이면 0~9 까지의 xor 값을 xor하면 0~9까지 한 값을 빼는 것과 같다.
      # 100 ~ 끝까지를 xor한 값을 다시 xor해주면 원래 값이 되게 된다.
      lxor = []
      p = 0
      for a in arr:
          p ^=  a
          lxor.append(p)
      totalxor = lxor[-1]
      p = 0
      rxor = []
      for a in reversed(arr):
          p ^= a
          rxor.append(p)
      rxor = list(reversed(rxor))
      # print(lxor)
      # print(rxor)
      ans = []
      for l,r in queries:
          # print(l-1,r+1)
          s = totalxor
          if l-1 >= 0:
              s ^= lxor[l-1]
          if r+1 < len(arr):
              s ^= rxor[r+1]
          ans.append(s)
      return ans

if __name__ == "__main__":
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3]]
    s = Solution()
    print(s.xorQueries(arr,queries))