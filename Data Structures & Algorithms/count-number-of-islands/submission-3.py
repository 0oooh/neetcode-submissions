class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols, rows = len(grid[0]), len(grid)
        visited = set()
        island = 0

        def dfs(y, x):
            if (y < 0 or y >= rows or x < 0 or x >= cols or grid[y][x] == "0" or (y, x) in visited):
                return
            visited.add((y, x))

            for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(y + dy, x + dx)

        for y in range(rows):
            for x in range(cols):
                if (y, x) not in visited and grid[y][x] == "1":
                    dfs(y, x)
                    island += 1
        return island