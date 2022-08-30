class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # not work
        R, C = len(grid), len(grid[0])

        if (not 1 in grid):
            return 0
        
        max_area = 0
        area_count = 0

        def dfs(r, c):
            if (grid[r,c]==0):
                if (r>=1):
                    area_count = 0
                    dfs(r-1, c)
                if (r+1<R):
                    area_count = 0
                    dfs(r+1, c)
                if (c>=1):
                    area_count = 0
                    dfs(r, c-1)
                if (c+1<C):
                    area_count = 0
                    dfs(r, c+1)
            else:
                area_count += 1
                if (r>=1):
                    max_area = max(area_count, max_area)
                    dfs(r-1, c)
                if (r+1<R):
                    max_area = max(area_count, max_area)
                    dfs(r+1, c)
                if (c>=1):
                    max_area = max(area_count, max_area)
                    dfs(r, c-1)
                if (c+1<C):
                    max_area = max(area_count, max_area)
                    dfs(r, c+1)
        
        dfs(R, C)

        return max_area


        # dfs - recursive
        # Time Complexity: O(R*C), where RR is the number of rows in the given grid, and CC is the number of columns. We visit every square once.
        # Space complexity: O(R*C), the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.


        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

        #  replace the 1s with 0s to prevent "finding" the same land twice
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0

        
        # dfs - iterative
        # using a stack based, (or "iterative") depth-first search
        # seen will represent squares that have either been visited or are added to our list of squares to visit (stack).
        # For every starting land square that hasn't been visited, we will explore 4-directionally around it,
        # adding land squares that haven't been added to seen to our stack
        # Time Complexity: O(R*C), where RR is the number of rows in the given grid, and CC is the number of columns. We visit every square once.
        # Space complexity: O(R*C), the space used by seen to keep track of visited squares, and the space used by stack.
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans