# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        curr=self.head
        count=0
        result=None
        while curr:
            count+=1
            if random.randint(1,count)==count:
                result=curr.val
            curr=curr.next
        return result    


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
