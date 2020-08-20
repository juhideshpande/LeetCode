# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        slow=fast=head        
        
        while fast and fast.next: #Find the mid -- O(N)
            slow=slow.next
            fast=fast.next.next
            
        
        prev=None
        curr=slow        
        while curr:  #Reverse the second part of the list  --O(N/2)
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            
        first=head  #Merge two lists  --O(N/2)
        second=prev
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
            
            
       # Time Complexity : O(N) Space Complexity: O(1)    

            
            
