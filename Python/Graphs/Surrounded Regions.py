class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board), len(board[0])
        if not board:
            return
        for i in range(m):
            if board[i][0]=='O':
                self.dfs(board,i,0)

        for j in range(n):
            if board[0][j]=='O':
                self.dfs(board,0,j)

        for i in range(m):
            if board[i][n-1]=='O':
                self.dfs(board,i,n-1)

        for j in range(n):
            if board[m-1][j]=='O':
                self.dfs(board,m-1,j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='Z':
                    board[i][j]='O'


    def dfs(self, board, i, j):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='O':
            return

        board[i][j]='Z'
        self.dfs(board, i+1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j-1)
