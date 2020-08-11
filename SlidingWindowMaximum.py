class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q=collections.deque()
        res=[]
        
        for index, val in enumerate(nums):
            if q and q[0]<=index-k: # if index not needed discard
                q.popleft()
                #print(q)
                
            while q and nums[q[-1]]<val: # if the last index value is less then max pop it
                q.pop() # pop from rear
                
            q.append(index) # append every index to queue to check for max
            
            if index+1>=k: 
                res.append(nums[q[0]])
                
        return res         
                
        
  #Front of the queue keeps track of index which had maximum val at that index
 # rear of the queue keeps track of the index with max value
                
            
            
