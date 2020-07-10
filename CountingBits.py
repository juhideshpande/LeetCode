class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ones_count=[0,1]
        
        for i in range(2,num+1):
            curr=1+ones_count[i&(i-1)]
            ones_count.append(curr)
            
        if num>=2:
            return ones_count
        else:
            return ones_count[:num+1]
        
