class Solution:
    #     def exist(self, board: List[List[str]], word: str) -> bool:
    #         m, n = len(board), len(board[0])
    #         pos = 0

    #         if m * n < len(word):
    #             return False

    #         if m == 1:
    #             return False if word not in "".join(board[0]) else True
    #         if n == 1:
    #             return False if word not in "".join(board[i][0] for i in range(m)) else True

    #         for i in range(m):
    #             for j in range(n):
    #                 if board[i][j] == word[pos]:
    #                     cur_i, cur_j, cur_pos = i, j, pos
    #                     cur_pos += 1
    #                     while cur_pos < len(word) and cur_i < m and cur_j < n:
    #                         # print(cur_pos, word[cur_pos])
    #                         if cur_i == 0:
    #                             if cur_j == 0:
    #                                 if board[cur_i + 1][cur_j] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_i += 1
    #                                 elif board[cur_i][cur_j + 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j += 1
    #                                 else:
    #                                     break
    #                             elif cur_j == n - 1:
    #                                 if board[cur_i + 1][cur_j] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_i += 1
    #                                 elif board[cur_i][cur_j - 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j -= 1
    #                                 else:
    #                                     break
    #                             else:
    #                                 if board[cur_i + 1][cur_j] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_i += 1
    #                                 elif board[cur_i][cur_j - 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j -= 1
    #                                 elif board[cur_i][cur_j + 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j += 1
    #                                 else:
    #                                     break
    #                         elif cur_i == m - 1:
    #                             if cur_j == 0:
    #                                 if board[cur_i - 1][cur_j] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_i -= 1
    #                                 elif board[cur_i][cur_j + 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j += 1
    #                                 else:
    #                                     break
    #                             elif cur_j == n - 1:
    #                                 if board[cur_i - 1][cur_j] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_i += 1
    #                                 elif board[cur_i][cur_j - 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j -= 1
    #                                 else:
    #                                     break
    #                             else:
    #                                 if board[cur_i - 1][cur_j] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_i += 1
    #                                 elif board[cur_i][cur_j - 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j -= 1
    #                                 elif board[cur_i][cur_j + 1] == word[cur_pos]:
    #                                     cur_pos += 1
    #                                     cur_j += 1
    #                                 else:
    #                                     break
    #                         elif cur_j == 0:
    #                             if board[cur_i - 1][cur_j] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_i -= 1
    #                             elif board[cur_i + 1][cur_j] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_i += 1
    #                             elif board[cur_i][cur_j + 1] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_j += 1
    #                             else:
    #                                 break
    #                         elif cur_j == n - 1:
    #                             if board[cur_i - 1][cur_j] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_i -= 1
    #                             elif board[cur_i + 1][cur_j] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_i += 1
    #                             elif board[cur_i][cur_j - 1] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_j -= 1
    #                             else:
    #                                 break
    #                         else:
    #                             if board[cur_i - 1][cur_j] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_i -= 1
    #                             elif board[cur_i + 1][cur_j] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_i += 1
    #                             elif board[cur_i][cur_j + 1] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_j += 1
    #                             elif board[cur_i][cur_j - 1] == word[cur_pos]:
    #                                 cur_pos += 1
    #                                 cur_j -= 1
    #                             else:
    #                                 break
    #                     print(cur_pos)
    #                     if cur_pos == len(word):
    #                         return True
    #         return False

    # 回溯
    # 对每一个位置 (i,j) 都调用函数 check 进行检查
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/word-search/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。