class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Triangle property : a +b >c , b+c >a, a+c>b a,b,c sides of triangle
        
        count=0
        nums=sorted(nums)
        for i in range(len(nums)-2):
            k=i+2
            for j in range(i+1,len(nums)-1):                
                while k<len(nums) and nums[i]+nums[j]>nums[k] and nums[i]!=0:
                    k+=1
                count+=max(0,k-j-1)   #if no solution present then should return 0
                #eg [0,1,0,1] without max count is negative with max it returns 0
                
        return count     
    
    #Time Complexity : O(N**2), Space Complexity: O(logn) because sorting takes logn space
