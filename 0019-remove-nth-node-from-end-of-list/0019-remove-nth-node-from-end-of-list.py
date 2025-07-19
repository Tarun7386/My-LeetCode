# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        cnt=0
        temp=head
        p=head  
        while(temp!=None):
            cnt+=1
            temp=temp.next
        K=cnt-n
        if K==0:
            return head.next
        l=0
        while(p!=None):
            l+=1
            d=p
            p=p.next
            if l==K:
                d.next=d.next.next
        if head==None:
            return None
        return head





        

        

        
        