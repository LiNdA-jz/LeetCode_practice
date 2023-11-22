class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = []
        for i in range(n):
            new_row = []
            for j in range(n):
                new_row.append(matrix[j][i])
            new_matrix.append(new_row)

        for i in range(n):
            matrix[i] = new_matrix[i][::-1]

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/rotate-image/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 原地旋转
    # 用一个临时变量 temp 暂存 matrix[col][n−row−1] 的值，这样虽然 matrix[col][n−row−1] 被覆盖了，我们还是可以通过 temp 获取它原来的值
    # temp = matrix[col][n - row - 1]
    # matrix[col][n - row - 1] = matrix[row][col]
    # row = col
    # col = n - row - 1
    # matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
    # 会覆盖掉 matrix[n−row−1][n−col−1]原来的值
    # temp = matrix[n - row - 1][n - col - 1]
    # matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
    # row = n - row - 1
    # col = n - col - 1
    # matrix[col][n - row - 1] = matrix[row][col]
    # matrix[n - col - 1][row] = matrix[n - row - 1][n - row - 1]
    # temp = matrix[n - col - 1][row]
    # matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1]
    # matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
    # matrix[col][n - row - 1] = matrix[row][col]
    # row = n - col - 1
    # col = row
    # matrix[row][col] = matrix[n - col - 1][row]
    # -> temp = matrix[row][col]
    # -> matrix[row][col] = matrix[n - col - 1][row]
    # -> matric[n - col - 1][row] = matrix[n - row - 1][n - col - 1]
    # -> matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
    # -> matrix[col][n - row - 1] = temp
    # 当 n 为偶数时，我们需要枚举 n^2/4=(n/2)×(n/2)个位置
    # 当 n 为奇数时，由于中心的位置经过旋转后位置不变，我们需要枚举 (n^2−1)/4=((n−1)/2)×((n+1)/2)个位置

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/rotate-image/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 翻转代替旋转
    # 水平翻转 + 主对角线翻转
    # 水平：matrix[row][col] = matrix[n - row - 1][col]
    # 主对角线：matrix[row][col] = matrix[col][row]
    # -> matrix[col][n - row - 1]
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/rotate-image/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。