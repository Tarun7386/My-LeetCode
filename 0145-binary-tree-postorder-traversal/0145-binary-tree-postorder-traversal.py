# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """               
        if not root:
            return []
        stack1=[root]
        stack2=[]       
        res=[]
        while stack1 :
            pointer=stack1.pop()
            stack2.append(pointer)                       
            if pointer.left:                
                stack1.append(pointer.left)
            if pointer.right:
                stack1.append(pointer.right)
        while stack2:
            res.append(stack2.pop().val)       
        return res
        














        