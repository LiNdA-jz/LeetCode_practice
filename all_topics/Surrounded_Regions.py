class Solution:
    # not work
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     m, n = len(board), len(board[0])

    #     if m == 1 or n == 1:
    #         return

    #     flipped = [[False] * n for _ in range(m)]

    #     for i in range(1, m - 1):
    #         for j in range(1, n - 1):
    #             if i == 1 and j == 1:
    #                 if board[i][j] == "O" and not flipped[i][j] and (
    #                     board[i - 1][j] == "X" and
    #                     board[i][j - 1] == "X"
    #                 ):
    #                     board[i][j] = "X"
    #                     flipped[i][j] = True

    #             elif board[i][j] == "O" and not flipped[i][j] and (
    #                 board[i - 1][j] == "X" and
    #                 board[i + 1][j] == "X" and
    #                 board[i][j - 1] == "X" and
    #                 board[i][j + 1] == "X"
    #                 ):
    #                 board[i][j] = "X"
    #                 flipped[i][j] = True

    # 所有的不被包围的 O 都直接或间接与边界上的 O 相连
    # 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O
    # 遍历这个矩阵，对于每一个字母：
    # 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O
    # 如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X
    # 深度优先搜索
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        # m / m - 1???
        # already checked [0][0] & [0][m - 1] & [n - 1][0] & [n - 1][m - 1]
        for i in range(1, m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/surrounded-regions/solutions/369110/bei-wei-rao-de-qu-yu-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 广度优先搜索
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])
        que = collections.deque()
        for i in range(n):
            if board[i][0] == "O":
                que.append((i, 0))
                board[i][0] = "A"
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
                board[i][m - 1] = "A"
        # m / m - 1???
        for i in range(1, m - 1):
            if board[0][i] == "O":
                que.append((0, i))
                board[0][i] = "A"
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
                board[n - 1][i] = "A"

        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))
                    board[mx][my] = "A"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/surrounded-regions/solutions/369110/bei-wei-rao-de-qu-yu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。