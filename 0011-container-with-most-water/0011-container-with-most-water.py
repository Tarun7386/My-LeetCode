class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_amount=float('-inf')
        left_pointer=0
        right_pointer=len(height)-1
        while (left_pointer<right_pointer):           
            l=min(height[left_pointer],height[right_pointer])
            r=right_pointer-left_pointer
            area=l*r
            if area>max_amount:
                max_amount=area
            if height[left_pointer]<height[right_pointer]:
                left_pointer+=1
            else:
                right_pointer-=1
        return max_amount

        
        