class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start=1
        end=len(arr)-2
        while start<=end:
            mid=start+(end-start)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1