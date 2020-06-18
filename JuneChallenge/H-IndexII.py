class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations.count(0)==len(citations):
            return 0
        low = 0
        n=len(citations)
        high=n-1
        while(low<=high):
            mid = low+(high-low)/2
            
            if citations[mid]==(n-mid):
                return citations[mid]
            elif citations[mid]>(n-mid):
                high=mid-1
            else:
                low=mid+1
                
        return n-low        
        
