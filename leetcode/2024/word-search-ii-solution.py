from typing import List
from collections import defaultdict

# 이 코드는 LeetCode의 Word Search II 문제에 대한 솔루션을 구현합니다.
# 이 문제는 주어진 문자 배열(board)에서 모든 단어를 찾는 것을 요구합니다.
# 단어는 보드에서 인접한 문자를 연결하여 형성할 수 있으며, 각 문자는 한 번만 사용할 수 있습니다.

# 이 솔루션은 입력 목록에 있는 모든 단어를 저장하기 위해 Trie 데이터 구조를 사용합니다.
# Trie는 문자열을 효율적으로 저장하는 트리와 같은 데이터 구조입니다.
# Trie의 각 노드는 문자를 나타내고 노드를 연결하는 에지는 문자 간의 전환을 나타냅니다.

# 이 알고리즘은 보드를 순회하고 Trie에 있는 모든 단어의 존재 여부를 확인하여 작동합니다.
# 보드의 각 셀에 대해 알고리즘은 깊이 우선 탐색(DFS)을 사용하여 해당 셀에서 시작하는 모든 가능한 경로를 재귀적으로 탐색합니다.
# DFS 중에 알고리즘은 현재 경로가 Trie의 모든 단어의 접두사에 해당하는지 확인합니다.
# 전체 단어가 발견되면 결과 목록에 추가됩니다.
# 셀을 다시 방문하지 않도록 하기 위해 알고리즘은 방문한 각 셀을 '#' 기호로 표시합니다.
# 모든 셀을 처리한 후 알고리즘은 보드에서 발견된 모든 단어 목록을 반환합니다.


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        Trie = lambda: defaultdict(Trie)
        root = Trie()

        def add(s):
            cur = root
            for c in s:
                cur = cur[c]
            cur['$'] = s

        for word in words:
            add(word)
        m, n = len(board), len(board[0])

        def dfs(i, j, root):
            ch = board[i][j]
            cur = root.get(ch)
            if not cur: return

            if '$' in cur:
                res.append(cur['$'])
                del cur['$']

            board[i][j] = '#'
            if i < m - 1: dfs(i + 1, j, cur)
            if i > 0: dfs(i - 1, j, cur)
            if j < n - 1: dfs(i, j + 1, cur)
            if j > 0: dfs(i, j - 1, cur)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res

    def test(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
                 ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        assert self.findWords(board, words) == ["oath", "eat", "rain"]


if __name__ == "__main__":
    s = Solution()
    s.test()
