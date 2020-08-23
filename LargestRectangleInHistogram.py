class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        elif len(heights)==1:
            return heights[0]
        
        area=0
        stack=[] #as we need to pop recent elements we need stack
        stack.append(0)
        
        for i in range(1,len(heights)):
            curr=heights[i]
            
            if curr>=heights[stack[-1]]: #if array is increasing then the recent height can be extended if the next elem is decreasing then recent one cannot be extended
                stack.append(i)
                
            else: #if array has increasing and decreasing elements
                while len(stack)!=0 and curr<heights[stack[-1]]:
                    temp=heights[stack.pop()]
                    
                    if len(stack)==0:
                        area=max(area,temp*i)
                    else:
                        area=max(area,temp*(i-stack[-1]-1))
                stack.append(i) 
                
        if len(stack)!=0: #all elements are not popped meaning the array is increasing
            j=len(heights)
            while len(stack)!=0:
                    temp=heights[stack.pop()]
                    
                    if len(stack)==0:
                        area=max(area,temp*j)
                    else:
                        area=max(area,temp*(j-stack[-1]-1))
        return area                

    
    #Time and Space Complexity: O(n)
            
            
                
                
