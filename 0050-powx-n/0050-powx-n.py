class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans=1.0
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        if x==0:
            return 0
        if x==-1 and  n%2==0:
            return 1
        if x==-1 and  n%2!=0:
            return -1

        while n>0:
            if n%2==1:
                ans=ans*x
            x=x*x
            n=n//2
        return ans
        