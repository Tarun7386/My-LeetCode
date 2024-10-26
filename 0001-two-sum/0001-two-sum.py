class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
          found=False
          for j in range(len(nums)):
              if i!=j:
                  s=nums[i]+nums[j]
              
                  if s==target:
                      a=[i,j]
                      found=True
          if found==True:
              return a
              break

        

        