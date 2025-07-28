# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        temp1=head
        temp2=head
        while( temp2!=None and temp2.next!= None):
            temp1=temp1.next
            temp2=temp2.next.next
            if temp1==temp2:
                return True
        return False