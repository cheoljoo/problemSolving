# 1310. XOR Queries of a Subarray
# https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=problem-list-v2&envId=mbbj9re1

from typing import List

class Solution:
  """
  Given an array arr of integers and a list of queries queries, where each query is a pair of indices [l, r], return an array answer, where answer[i] is the XOR of all elements from arr[l] to arr[r] inclusive.
  
  This function calculates the XOR of elements in a given array for each query.
  
  It uses prefix XOR and suffix XOR to efficiently calculate the XOR of elements in a given range.
  
  1. **Prefix XOR:**
     - Calculates the XOR of elements from the beginning of the array to each index.
     - Stores the prefix XOR values in a list called 'lxor'.
  
  2. **Suffix XOR:**
     - Calculates the XOR of elements from each index to the end of the array.
     - Stores the suffix XOR values in a list called 'rxor'.
  
  3. **Query Processing:**
     - For each query [l, r]:
       - Initializes 's' with the XOR of all elements in the array ('totalxor').
       - If the left index 'l' is not 0, XORs 's' with the prefix XOR value at index 'l-1' to exclude elements before 'l'.
       - If the right index 'r' is not the last index, XORs 's' with the suffix XOR value at index 'r+1' to exclude elements after 'r'.
       - Appends the resulting 's' value to the 'ans' list.
  
  4. **Return Result:**
     - Returns the 'ans' list, which contains the XOR values for each query.
  
  주어진 정수 배열 arr과 각 쿼리가 인덱스 쌍 [l, r]인 쿼리 목록 queries가 주어지면, 
  answer[i]가 arr[l]부터 arr[r]까지의 모든 요소의 XOR인 배열 answer를 반환합니다.

  이 함수는 주어진 쿼리에 대한 배열의 요소 XOR을 계산합니다.

  접두사 XOR과 접미사 XOR을 사용하여 주어진 범위 내 요소의 XOR을 효율적으로 계산합니다.

  1. **접두사 XOR:**
     - 배열의 시작부터 각 인덱스까지 요소의 XOR을 계산합니다.
     - 'lxor'라는 목록에 접두사 XOR 값을 저장합니다.

  2. **접미사 XOR:**
     - 각 인덱스부터 배열의 끝까지 요소의 XOR을 계산합니다.
     - 'rxor'라는 목록에 접미사 XOR 값을 저장합니다.

  3. **쿼리 처리:**
     - 각 쿼리 [l, r]에 대해:
       - 배열의 모든 요소의 XOR인 'totalxor'로 's'를 초기화합니다.
       - 왼쪽 인덱스 'l'이 0이 아니면 'l-1' 인덱스의 접두사 XOR 값을 's'와 XOR하여 'l' 이전 요소를 제외합니다.
       - 오른쪽 인덱스 'r'이 마지막 인덱스가 아니면 'r+1' 인덱스의 접미사 XOR 값을 's'와 XOR하여 'r' 이후 요소를 제외합니다.
       - 결과 's' 값을 'ans' 목록에 추가합니다.

  4. **결과 반환:**
     - 각 쿼리에 대한 XOR 값을 포함하는 'ans' 목록을 반환합니다.
  """
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