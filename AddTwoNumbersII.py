# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1,v2='',''
        
        while l1:
            v1+=str(l1.val)
            l1=l1.next
            
        while l2:
            v2+=str(l2.val)
            l2=l2.next 
            
        v3=str(int(v1)+int(v2))
        
        curr=result=ListNode(0)
        for i in range(len(v3)):
            curr.next=ListNode(v3[i])
            curr=curr.next
            
        return result.next    
            
        
