# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         dummy=ListNode(-1) # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
#         dummy.next=head
        
#         prev=dummy
        
#         while head and head.next:
#             first=head
#             second=head.next
            
#             prev.next=second
#             first.next=second.next
#             second.next=first
            
#             prev=first
#             head=first.next
            
#         return dummy.next   

        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next 
        
        return dummy.next 
       #Time Complexity: O(N) where N is the size of the linked list.
        #Space Complexity: O(1)
