class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m >= 1:
            n = len(matrix[0])
        else:
            return []

        total_size = m * n

        res = []
        if m <= 1:
            # print(m, res)
            return matrix[0]
        if n <= 1:
            for i in range(m):
                res.append(matrix[i][0])
            # print(n, res)
            return res

        if m == 2:
            return matrix[0] + matrix[1][::-1]

        while m > 2:
            # outer
            res = matrix[0]
            for i in range(1, m - 1):
                res.append(matrix[i][-1])

            res = res + matrix[-1][::-1]
            for i in range(m - 2, 0, -1):
                res.append(matrix[i][0])

            # print(res)
            if len(res) == total_size:
                # print(res)
                return res
            # matrix = matrix[1:m][1:n]
            # print(matrix)
            # inner mat
            next_mat = []
            for i in range(1, m - 1):
                next_mat_row = matrix[i][1:n - 1]
                next_mat.append(next_mat_row)
            # print(next_mat)

            if len(next_mat) == 1:
                next = next_mat[0]
                # print(res + next)
                return res + next

            m, n = len(next_mat), len(next_mat[0])
            next = self.spiralOrder(next_mat)
            # print(next)
            res = res + next

            if len(res) == total_size:
                print(res)
                return res

            # print(res, m, n)

        return res

    # 模拟
    # 初始位置是矩阵的左上角，初始方向是向右，当路径超出界限或者进入之前访问过的位置时，
    # 顺时针旋转，进入下一个方向。
    # 判断路径是否进入之前访问过的位置需要使用一个与输入矩阵大小相同的辅助矩阵 visited
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/spiral-matrix/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 按层模拟
    # 第 k 层是到最近边界距离为 k 的所有顶点
    # 对于每层，从左上方开始以顺时针的顺序遍历所有元素
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/spiral-matrix/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。