class Solution:
    # low memory
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row
        for i in range(9):
            num_dict = {}
            for j in range(9):
                cur_num = board[i][j]
                if cur_num != ".":
                    if cur_num in num_dict:
                        print("row false")
                        return False
                    else:
                        num_dict[cur_num] = 1

        # col
        for j in range(9):
            num_dict = {}
            for i in range(9):
                cur_num = board[i][j]
                if cur_num != ".":
                    if cur_num in num_dict:
                        print("col false")
                        return False
                    else:
                        num_dict[cur_num] = 1

        # grid
        for n in range(9):
            num_dict = {}
            for i in range(3):
                for j in range(3):
                    cur_num = board[n // 3 * 3 + i][n % 3 * 3 + j]
                    # print(n, " ", i, " ", j, " ", cur_num)
                    if cur_num != ".":
                        if cur_num in num_dict:
                            print("grid false")
                            return False
                        else:
                            num_dict[cur_num] = 1

        return True

    # lower performance in time; low performance in memory but better than prev.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = [[0] * 9] * 9
        # cols = [[0] * 9] * 9
        # subboxes = [[[0] * 9] * 3] * 3
        # print(rows, cols, subboxes)
        # print(subboxes)
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                cur_num = board[i][j]
                if cur_num != ".":
                    cur_num = int(cur_num) - 1
                    rows[i][cur_num] += 1
                    cols[j][cur_num] += 1
                    subboxes[int(i / 3)][int(j / 3)][cur_num] += 1

                    if rows[i][cur_num] > 1 or cols[j][cur_num] > 1 or subboxes[int(i / 3)][int(j / 3)][cur_num] > 1:
                        return False

        return True