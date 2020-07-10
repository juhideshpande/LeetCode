"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        temp=Node(0)
        temp=head
        stack=[]
        while head:
            if head.child!= None:
                if head.next!=None:
                    stack.append(head.next)
                head.next=head.child
                head.next.prev=head
                head.child=None

            elif(head.next==None and len(stack)!=0):
                head.next=stack.pop()
                head.next.prev=head
                                
            head=head.next
            
        return temp    
