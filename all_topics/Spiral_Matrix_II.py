class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1, 2], [4, 3]]

        final_res = []
        # first
        res = [i for i in range(1, n + 1)]
        # print(res)
        final_res.append(res)

        # mid
        mid = self.generateMatrix(n - 2)
        for i in range(n - 2):
            for j in range(n - 2):
                mid[i][j] += 4 * n - 3 - 1

        for i in range(1, n - 1):
            left = 4 * n - 3 - i
            right = n + i
            # print(mid[i - 1])
            final_res.append([left] + mid[i - 1] + [right])

        # last
        res = [2 * n - 1 + i for i in range(n - 1, -1, -1)]
        # print(res)
        final_res.append(res)

        return final_res

    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat

    # 作者：Krahets
    # 链接：https://leetcode.cn/problems/spiral-matrix-ii/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 模拟
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4  # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy

        return matrix

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/spiral-matrix-ii/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 按层模拟
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                matrix[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    matrix[bottom][col] = num
                    num += 1
                for row in range(bottom, top, -1):
                    matrix[row][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/spiral-matrix-ii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。