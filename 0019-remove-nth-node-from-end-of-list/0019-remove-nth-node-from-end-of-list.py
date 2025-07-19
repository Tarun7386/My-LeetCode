# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        # cnt=0
        # temp=head
        # p=head  
        # while(temp!=None):
        #     cnt+=1
        #     temp=temp.next
        # K=cnt-n
        # if K==0:
        #     return head.next
        # l=0
        # while(p!=None):
        #     l+=1
        #     d=p
        #     p=p.next
        #     if l==K:
        #         d.next=d.next.next
        # if head==None:
        #     return None
        # return head





class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        slow=head
        while(fast.next!=None):
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head

        
        





          




        

        

        
        