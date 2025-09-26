class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==0 or n==1:
            return 0
        cnt=0
        b=[True]*n
        b[0]=False
        b[1]=False
        for i in range(2,n): 
            if b[i]:
                for j in range(2*i,n,i):
                    b[j]=False
        for primes in range(len(b)):
            if b[primes]:
                cnt+=1
        return cnt

        