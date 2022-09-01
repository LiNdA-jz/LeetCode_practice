class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # not minimum
        rows, cols = len(grid), len(grid[0])

        rot_count = 0

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j]==2):
                    if (i>0):
                        if (grid[i-1][j] == 1):
                            grid[i-1][j] = 2
                            rot_count += 1
                    if (j>0):
                        if (grid[i][j-1] == 1):
                            grid[i][j-1] = 2
                            rot_count += 1
        
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j]==2):
                    if (i<rows-1):
                        if (grid[i+1][j] == 1):
                            grid[i+1][j] = 2
                            rot_count += 1
                    if (j<cols-1):
                        if (grid[i][j+1] == 1):
                            grid[i][j+1] = 2
                            rot_count += 1

        return rot_count if 1 not in grid else -1


        # bfs
        # Time complexity: O(rows * cols) -> each cell is visited at least once
        # Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1
        
        # number of columns
        cols = len(grid[0])
        
        # keep track of fresh oranges
        fresh_cnt = 0
        
        # queue with rotten oranges (for BFS)
        rotten = deque()
        
        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1
        
        # keep track of minutes passed.
        minutes_passed = 0
        
        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1
            
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    fresh_cnt -= 1
                    
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        
        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1


        # bfs
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer


        # Usually, if we need to find the distances, we use bfs
        # time complexity is O(mn), because we first traverse our grid to fill queue and found number of fresh oranges. 
        # Then we use classical bfs, so each node will be added and removed from queue at most 1 time. 
        # Space complexity is also can be O(mn), we can have for example O(mn) rotten oranges in the very beginnig.
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i,j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i,j))
            if grid[i][j] == 1: fresh += 1
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        levels = 0
        
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
                        
        return -1 if fresh != 0 else max(levels-1, 0)