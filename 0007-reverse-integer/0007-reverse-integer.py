class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        n = abs(x)
        rev = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while n != 0:
            digit = n % 10
            n //= 10
            
            if rev > (INT_MAX - digit) // 10:
                return 0

            rev = rev * 10 + digit

        rev *= sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev