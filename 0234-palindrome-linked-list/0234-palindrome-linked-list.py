# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head):
        if head==None:
            return head
        else:
            prev=None
            temp=head
            while(temp!=None):
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow=head
        fast=head
        while (fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        second_half=self.reverse(slow)
        first=head
        second=second_half
        res=True
        while(second!=None):
            if first.val!=second.val:
                res=False
                break
            first=first.next
            second=second.next
        self.reverse(second_half)
        return res
















        
        

        
        

        