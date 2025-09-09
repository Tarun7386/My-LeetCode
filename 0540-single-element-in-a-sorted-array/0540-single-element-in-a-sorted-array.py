class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)-1
        while (start<=end):
            mid=start+(end-start)//2

            if (mid==len(nums)-1) or (mid==0):
                return nums[mid]
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==0:
                if nums[mid-1]==nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            if mid%2!=0:
                if nums[mid-1]==nums[mid]:
                    start=mid+1
                else:
                    end=mid-1
        return -1

        