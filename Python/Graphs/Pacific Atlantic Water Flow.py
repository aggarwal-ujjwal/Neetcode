class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []

        if not heights:
            return ans
        m, n = len(heights) , len(heights[0])

        self.directions = [(1,0),(0,1),(-1,0),(0,-1)]

        pacific_visited = [[False for col in range(n)] for row in range(m)]
        atlantic_visited = [[False for col in range(n)] for row in range(m)]

        for i in range(m):
            self.dfs(heights, i, 0, pacific_visited, m, n)
            self.dfs(heights, i, n-1, atlantic_visited, m, n)

        for j in range(n):
            self.dfs(heights, 0, j, pacific_visited, m, n)
            self.dfs(heights, m-1, j, atlantic_visited, m, n)

        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append([i,j])

        return ans

    def dfs(self, heights, i, j, visited, m, n):
        visited[i][j] = True

        for dir in self.directions:
            x, y = i+dir[0], j+dir[1]
            if x<0 or x>=m or y<0 or y>=n or visited[x][y] or heights[x][y] < heights[i][j]:
                continue
            self.dfs(heights,x,y,visited,m,n)




# the trick is to see whether water can flow towards the next cell, start with corners cells and track visited for both oceans.
#Combined visted cells will give you the value