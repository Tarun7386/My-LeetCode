# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        stack=[]
        pre=[]
        stack.append(root)
        while(stack):
            top=stack.pop()
            pre.append(top.val)
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
        return pre
        