class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result=0
        left_max=0
        right_max=0
        L=0
        R=len(height)-1
        
        while L<R:
            left_max=max(left_max,height[L])
            right_max=max(right_max,height[R])
            
            if left_max<=right_max:          #Formula: water+=min(left_max, right_max)-height[current]
                result+=left_max-height[L]
                L+=1
                
            else:
                result+=right_max-height[R]
                R-=1
                
        return result        
