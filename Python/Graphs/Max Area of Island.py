class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    max_area = max(max_area,self.dfs(grid,i,j))

        return max_area

    def dfs(self,grid, i, j) -> int:
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
            return 0
        grid[i][j]=0
        area=1
        area += self.dfs(grid, i+1, j)
        area += self.dfs(grid, i, j+1)
        area += self.dfs(grid, i-1, j)
        area += self.dfs(grid, i, j-1)
        print(i,j,area)
        return area


