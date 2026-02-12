class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        n=len(haystack)
        m=len(needle)

        if m == 0:
            return 0

        for i in range(n-m+1):
            p1=i
            p2=0

            while p2<m and haystack[p1]==needle[p2]:
                p1+=1
                p2+=1
            if p2==m:
                return i
        return -1
        
            

        
        