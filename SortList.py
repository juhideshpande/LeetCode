# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None:
            return head
        
        temp=head
        slow=head
        fast=head
        
        while fast!=None and fast.next!=None:
            temp=slow
            slow=slow.next
            fast=fast.next.next
            
        temp.next=None  
        left=self.sortList(head)
        right=self.sortList(slow)
        #head=start of first list
        #temp= end of first list
        #slow=start of second list
        #fast= end of second list
        
        return self.merge(left, right)
    
    def merge(self,l1, l2):
        sortedTemp=ListNode(0)
        curr=sortedTemp #l1 =left siide list, l2=right side list
        
        while (l1!=None and l2!=None):
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
                
            curr=curr.next
            
        if l1!=None: #if l2==None
            curr.next=l1
            l1=l1.next

        if l2!=None: #if l1==None
            curr.next=l2
            l2=l2.next    
                
        return sortedTemp.next        
                
                
    
        
        
