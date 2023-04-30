class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # not work -> only work for m = 3
        # m, n = len(matrix), len(matrix[0])
        # # first row
        # res = matrix[0]

        # # last_row = list(reversed(matrix[-1]))
        # # print(last_row)

        # # right column
        # for row in range(1, m):
        #     res.append(matrix[row][-1])

        # # print(res)

        # # # last row
        # # res.extend(list(reversed(matrix[-1][:-1])))

        # # # left column
        # # for row in range(m-1, 0, -1):
        # #     res.append(matrix[row][0])

        # i = m - 1
        # rev = 1
        # while i > 0:
        #     if rev == -1:
        #         res.extend(matrix[i][:-1])
        #     else:
        #         res.extend(list(reversed(matrix[i][:-1])))
        #     # print(res)
        #     rev *= -1
        #     i -= 1

        # # print(res)

        # return res

        if not matrix or not matrix[0]:
            return list()

        # m, n
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        # result
        order = [0] * total

        # right, down, left, up
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            # next according to the dirction
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            # need to change to the next direction
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            # get new row & col
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。