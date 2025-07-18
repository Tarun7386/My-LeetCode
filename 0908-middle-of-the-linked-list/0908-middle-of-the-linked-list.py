# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cnt=0
        
        temp=head
        while(temp!=None):
            cnt+=1
            print(head.val)
            temp=temp.next
        mid=cnt//2
        temp=head
        while mid>0:
            temp=temp.next
            mid=mid-1
        dummy_node=ListNode(-1)
        new_tail=dummy_node
        while(temp is not None):
            
            new_node=ListNode(temp.val)
            new_tail.next=new_node
            new_tail=new_node
            temp=temp.next

        
        return dummy_node.next



