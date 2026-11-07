class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(y, x):
            if (y < 0  
                or y >= rows 
                or x < 0 
                or x >= cols 
                or grid[y][x] == "0"
                or (y, x) in visited
                ):
                return
            
            visited.add((y, x))
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(y + dy, x + dx)
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "1" and (y, x) not in visited:
                    dfs(y, x)
                    islands += 1
        return islands