class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        first=1
        while first<len(nums):
            if nums[start]!=nums[first]:
                start+=1
                nums[start]=nums[first]

            first+=1
        return start+1               
            


        
        