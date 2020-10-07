# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        length=1
        last=head
        
        while last.next: #Calculate length and stire last element            
            last=last.next
            length+=1
            
        k = k % length # If k is equal to the length of the list then k == 0
        # Elif k is greater than the length of the list then k = k % length   
        
        last.next=head #make this a circular linked list
        
        temp=head
        for i in range(length-k-1): #find the length-k node to set to None that node would be the end of the list
            temp=temp.next
            
        result=temp.next #the result starts from temo node's next element
        temp.next=None
        
        return result
            
            
            
            
