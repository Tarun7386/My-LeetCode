class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        a=1
        b=1
        ans = [1]*n

        for i in range(1, n):
            a = a * nums[i - 1]
            ans[i]=a

        for i in range(n - 2, -1, -1):
            b = b * nums[i + 1]
            ans[i]*=b

       

        return ans
        