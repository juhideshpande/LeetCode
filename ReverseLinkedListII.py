# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
         # Consider linked list as a list A. i.e. A[1]=head.val, A[2]=head.next.val ....
        # Create dummy [D,A[1],A[2],....]   

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode # pre at A[0]

        for i in range(m - 1):
            pre = pre.next  # move pre m-1 times. now pre is at A[M-1]
        
        
        reverse = None   #start reversing from cur=pre.next (A[M]) for n-m+1 nodes
        cur = pre.next
        for i in range(n - m + 1):
            tempNext = cur.next
            cur.next = reverse
            reverse = cur
            cur = tempNext

            
        # now the situation is
        # [dummy .... pre]    [reverse,..., pre.next]   [cur .....]
        # connect pre to reverse, and pre.next to cur


        # careful. pre.next,pre.next.next=reverse,cur gives you an error    
        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
