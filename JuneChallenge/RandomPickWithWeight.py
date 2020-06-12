class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sum=[]
        prefix_sum=0
        for weight in w:
            prefix_sum+=weight
            self.prefix_sum.append(prefix_sum)
        self.total=prefix_sum    
            
        

    def pickIndex(self):
        """
        :rtype: int
        """
        random_num=self.total*random.random()
        low,high=0,len(self.prefix_sum)
        while(low<high):
            mid=low+(high-low)//2
            if random_num>self.prefix_sum[mid]:
                low=mid+1
            else:
                high=mid
        return low         


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
