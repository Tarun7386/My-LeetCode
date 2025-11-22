class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n=len(grid)
        m=len(grid[0])
        visited=[[False for _ in range(m)] for _ in range(n) ]
        q=deque()
        time=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,time))
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            i,j,time=q.popleft()
            visited[i][j]=True

            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    q.append((ni,nj,time+1))
                    visited[ni][nj]=True
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return time

            