class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # tri_ls = [[1], [1, 1]]

        # if rowIndex <= 1:
        #     return tri_ls[rowIndex]

        # for i in range(1, rowIndex):
        #     new_row = [1, 1]

        #     for j in range(1, len(tri_ls[-1])):
        #         new_row.insert(j, tri_ls[-1][j] + tri_ls[-1][j-1])
        #     tri_ls.append(new_row)

        # return tri_ls[-1]

        # res=[]
        # for i in range(rowIndex+1):
        #     res.append([])
        #     for j in range(i+1):
        #         if j == 0 or j == i:
        #             res[i].append(1)
        #         else:
        #             res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        # return res[rowIndex]

        # recursion
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex - 1)
        currentRow = [1]
        for i in range(len(prevRow) - 1):
            currentRow.append(prevRow[i] + prevRow[i + 1])
        currentRow.append(1)
        return currentRow