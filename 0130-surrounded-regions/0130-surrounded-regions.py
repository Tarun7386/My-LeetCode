class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        

        def dfs(i,j):
            if i<0 or i>=n or j>=m or j<0:
                return 
            if  board[i][j]!="O" :
                return

            board[i][j] = "T"
            
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i+1,j)    

        for i in range(n):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][m-1]=="O":
                dfs(i,m-1)
        for j in range(m):
            if board[0][j]=="O":
                dfs(0,j)
            if board[n-1][j]=="O":
                dfs(n-1,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"

            

        