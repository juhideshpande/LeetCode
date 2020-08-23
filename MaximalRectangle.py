class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        maxarea=0
        height=[0]*n        
        for r in range(m):
            for c in range(n):
                if matrix[r][c]=="0":
                    height[c]=0
                else:
                    height[c]+=1
                    
            maxarea=max(maxarea, self.findArea(height))
        return maxarea
    
    def findArea(self,h):  #for each row
        area=0
        stack=[]
        stack.append(0)
        for i in range(1, len(h)):
            curr=h[i]
            if len(stack)==0 or curr>=h[stack[-1]]:
                stack.append(i)
            else:
                while stack and curr<=h[stack[-1]]:
                    temp=h[stack.pop()]
                    
                    if len(stack)==0:
                        area=max(area,temp*i)
                    else:
                        area=max(area,temp*(i-stack[-1]-1))
                stack.append(i)
        
        if len(stack)!=0:
            while stack:   
                i=len(h)
                while stack :
                        temp=h[stack.pop()]

                        if len(stack)==0:
                            area=max(area,temp*i)
                        else:
                            area=max(area,temp*(i-stack[-1]-1))
        return area                    
            
            
      #Time Complexity: O(m*n)  Space COmplexity: O(n) as col array created m=len(matrix)
      #  n=len(matrix[0])           
        
        
