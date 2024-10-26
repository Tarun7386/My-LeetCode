class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        move1=0
        for i in nums:
            if i!=0:
                nums[move1]=i
                move1+=1
        for i in range(move1,len(nums)):
            nums[i]=0
        return nums