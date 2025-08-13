# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack=[]
        inorderList=[]
        pointer=root
        while stack or pointer:
            while pointer !=None:
                stack.append(pointer)
                pointer=pointer.left
            
            pointer=stack.pop()
            inorderList.append(pointer.val)

            pointer=pointer.right
        return inorderList

                
        

        


