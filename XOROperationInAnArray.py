class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        ans=[]
        xor=0
        for i in range(n):
            temp=start+2*i
            ans.append(temp)
        #print(ans)    
        
        for i in range(len(ans)):
            xor = xor ^ ans[i]
        return xor    
            
