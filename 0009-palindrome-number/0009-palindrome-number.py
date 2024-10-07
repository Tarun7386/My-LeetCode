class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        o_num=x
        rev=0
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        return o_num==rev
        