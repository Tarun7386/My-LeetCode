# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def oddEvenList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         dummy_node=ListNode(-1)
#         p=dummy_node      
#         while(odd):
#             p.next=ListNode(odd.val)
#             p=p.next           
#             if odd.next and odd.next.next:
#                 odd = odd.next.next
#             else:
#                 break
#         while(even):
#             p.next=ListNode(even.val)
#             p=p.next           
#             even=even.next.next       
#         return dummy_node.next




class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (head==None or head.next==None):
            return head
        odd=head
        even=head.next
        even_head=even
        while(even and even.next):
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=even_head
        return head
        
        

            

        