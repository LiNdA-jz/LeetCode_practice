from dis import dis


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # not work
        rows, cols = len(mat), len(mat[0])

        dist = [[0]*cols]*rows
        print(mat, dist)

        for i in range(rows):
            for j in range(cols):
                if (mat[i][j]==1):
                    dist[i][j] = np.inf
                else:
                    dist[i][j]=0
        print(dist)
        for i in range(rows):
            for j in range(cols):
                if (mat[i][j]!=0):
                    if (i>0):
                        dist[i][j] = min(dist[i][j], dist[i-1][j]+1)
                    if (j>0):
                        dist[i][j] = min(dist[i][j], dist[i][j-1]+1)


        for i in range(rows):
            for j in range(cols):
                if (i<rows-1):
                    dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
                if (j<cols-1):
                    dist[i][j] = min(dist[i][j], dist[i][j+1]+1)               

                    
        return dist



        # bfs on zero-cell first
        # Time: O(M * N), where M is number of rows, N is number of columns in the matrix.
        # Space: O(M * N), space for the queue.
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat

        # DP
        # Time: O(M * N), where M is number of rows, N is number of columns in the matrix.
        # Space: O(1)
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat


# brute force
# Time complexity: O((r⋅c)^2) -> Iterating over the entire matrix for each 1 in the matrix.

# Space complexity: O(1) No extra space is required other than the space used to store the output (dist), and the output does not count towards the space complexity.


# class Solution {
# public:
#     vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#         int rows = matrix.size();
#         if (rows == 0)
#             return matrix;
#         int cols = matrix[0].size();
#         vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX));
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 if (matrix[i][j] == 0) {
#                     dist[i][j] = 0;
#                 } else {
#                     for (int k = 0; k < rows; k++) {
#                         for (int l = 0; l < cols; l++) {
#                             if (matrix[k][l] == 0) {
#                                 int dist_01 = abs(k - i) + abs(l - j);
#                                 dist[i][j] = min(dist[i][j], abs(k - i) + abs(l - j));
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#         return dist;
#     }
# };


# bfs
# start the BFS from 0s and thereby, updating the distances of all the 1s in the path
# Intially, distance for each 0 cell is 0 and distance for each 1 is INT_MAX, which is updated during the BFS.
# Pop the cell from queue, and examine its neighbors
# Time complexity: O(r⋅c) Since, the new cells are added to the queue only if their current distance is greater than the calculated distance, 
# cells are not likely to be added multiple times.
# Space complexity: O(r⋅c) An additional O(r⋅c) space is required to maintain the queue.
# class Solution {
# public:
#     vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#         int rows = matrix.size();
#         if (rows == 0)
#             return matrix;
#         int cols = matrix[0].size();
#         vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX));
#         queue<pair<int, int>> q;
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 if (matrix[i][j] == 0) {
#                     dist[i][j] = 0;
#                     q.push({ i, j }); //Put all 0s in the queue.
#                 }
#             }
#         }

#         int dir[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
#         while (!q.empty()) {
#             pair<int, int> curr = q.front();
#             q.pop();
#             for (int i = 0; i < 4; i++) {
#                 int new_r = curr.first + dir[i][0], new_c = curr.second + dir[i][1];
#                 if (new_r >= 0 && new_c >= 0 && new_r < rows && new_c < cols) {
#                     if (dist[new_r][new_c] > dist[curr.first][curr.second] + 1) {
#                         dist[new_r][new_c] = dist[curr.first][curr.second] + 1;
#                         q.push({ new_r, new_c });
#                     }
#                 }
#             }
#         }
#         return dist;
#     }
# };

# dynamic programming
# The distance of a cell from 0 can be calculated if we know the nearest distance for all the neighbors
# In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom directions.
# Time complexity: O(r⋅c) # We perform two passes over the matrix and each pass requires O(r \cdot c)O(r⋅c) time.
# Space complexity: O(1) No extra space is required other than the space used to store the output (dist), and the output does not count towards the space complexity.
# class Solution {
# public:
#     vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#         int rows = matrix.size();
#         if (rows == 0) 
#             return matrix;
#         int cols = matrix[0].size();
#         vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX - 100000));

#         //First pass: check for left and top
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 if (matrix[i][j] == 0) {
#                     dist[i][j] = 0;
#                 } else {
#                     if (i > 0)
#                         dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
#                     if (j > 0)
#                         dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
#                 }
#             }
#         }

#         //Second pass: check for bottom and right
#         for (int i = rows - 1; i >= 0; i--) {
#             for (int j = cols - 1; j >= 0; j--) {
#                 if (i < rows - 1)
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
#                 if (j < cols - 1)
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
#             }
#         }
#         return dist;
#     }
# };