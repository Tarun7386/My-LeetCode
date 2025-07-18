# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry=0
        t1=l1
        t2=l2
        dummy_node=ListNode(-1)
        current_pointer=dummy_node
        while (t1!=None or t2!=None):
            s=carry
            if t1!=None:
                s=s+t1.val
            if t2!=None:
                s=s+t2.val
            newnode=ListNode(s%10)
            carry=s//10
            current_pointer.next=newnode
            current_pointer=current_pointer.next
            if t1:
                t1=t1.next
                
            if t2:
                t2=t2.next
                
        if carry:
            carry_node=ListNode(carry)
            current_pointer.next=carry_node
        return dummy_node.next
        
        

            
            



        