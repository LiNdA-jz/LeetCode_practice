class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        for i in range(m):
            if target == matrix[i][0] or target == matrix[i][n - 1]:
                return True
            if target > matrix[i][n - 1]:
                continue
            if target < matrix[i][0]:
                return False
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if target == matrix[i][mid]:
                    return True
                if target < matrix[i][mid]:
                    r = mid - 1
                if target > matrix[i][mid]:
                    l = mid + 1

        return False

    # 两次二分查找
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def binarySearchFirstColumn(matrix, target):
            low, high = -1, m - 1

            while low < high:
                mid = (high - low + 1) // 2 + low

                if (matrix[mid][0] <= target):
                    low = mid
                else:
                    high = mid - 1

            return low

        def binarySearchRow(row, target):
            low, high = 0, n - 1

            while (low <= high):
                mid = (high - low) // 2 + low

                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return False

        rowIndex = binarySearchFirstColumn(matrix, target)

        if rowIndex < 0:
            return False

        return binarySearchRow(matrix[rowIndex], target)

    # 一次二分查找
    # 两种方法殊途同归，都利用了二分查找，在二维矩阵上寻找目标值。值得注意的是，若二维数组中的一维数组的元素个数不一，方法二将会失效，而方法一则能正确处理。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        low, high = 0, m * n - 1

        while low <= high:
            mid = (high - low) // 2 + low
            x = matrix[mid // n][mid % n]

            if x < target:
                low = mid + 1

            elif x > target:
                high = mid - 1

            else:
                return True

        return False