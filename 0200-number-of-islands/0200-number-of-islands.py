class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m_row=len(grid)
        n_col=len(grid[0])
        visited = [[False for _ in range(n_col)] for _ in range(m_row)]
        def dfs(i,j):
            if (i<0 or j>=n_col or i>=m_row or j<0):
                return 
            if (grid[i][j]=="0" or visited[i][j]):
                return
            visited[i][j]=True
            
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)

                    
        cnt=0
        for i in range(m_row):
            for j in range(n_col):
                if grid[i][j]=="1" and not visited[i][j]:
                    dfs(i,j)
                    cnt+=1

        return cnt