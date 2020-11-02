# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans=[]
        temp=0
        
        while(head!=None):
            ans.append(head.val)
            head=head.next
        print(ans) 
        n=len(ans)
        for i in range(len(ans)-1,-1,-1):
            temp=temp+ans[i]*pow(2,n-i-1)
        return temp    
