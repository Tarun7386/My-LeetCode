class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        N=len(pushed)
        j=0
        for i in range(N):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return len(stack)==0
        