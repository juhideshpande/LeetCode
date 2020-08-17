class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res=[0]*num_people
        give=0 
        
        while candies>0:
            res[give%num_people]+=min(candies, give+1)
            candies-=give+1
            give+=1
            
        return res     
    
    #Time: O(sqrt(candies)), space: O(num_people)
        
        
