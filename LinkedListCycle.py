# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = {}
        while head != None:
            if head in nodes:
                return True            
            nodes[head] = head
            head = head.next                
        return False                
        
