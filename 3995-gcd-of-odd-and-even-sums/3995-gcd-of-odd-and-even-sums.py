import math
class Solution(object):
    # def gcd(self,n1,n2):
    #     if n1==0:
    #         return n2
    #     if n2==0:
    #         return n1
    #     if n1==n2:
    #         return n1
    #     if n1>n2:
    #         return self.gcd(n1-n2,n2)
    #     if n2>n1:
    #         return self.gcd(n1,n2-n1)
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        sumOdd=0
        sumEven=0

        for i in range(1,2*n+1):
            if i%2==0:
                sumEven+=i   
            else:
                sumOdd+=i
        return self.gcd(sumOdd, sumEven)
        



        