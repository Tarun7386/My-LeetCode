class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        
        for idx in range(len(nums)):
            req=target-nums[idx]
            if req in seen:
                return [seen[req],idx]
            seen[nums[idx]]=idx
                
        