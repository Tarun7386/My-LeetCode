class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(n+1):
            a=bin(i)[2:] 
            cnt=a.count('1')
            ans.append(cnt)
        return ans