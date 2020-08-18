class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """        
        if N==0:  #edge case
            return range(1,10)
        if N==1:
            return range(10)
        
        res=[i for i in range(1,10) if (i+K<10 or i-K>=0)]
        for j in range(1,N):
            temp=[]
            
            for i in range(len(res)):

                if res[i]%10+K in range(1,10):
                    temp.append(res[i]*10+(res[i]%10 + K))

                if res[i]%10-K in range(0,10):
                    temp.append(res[i]*10+(res[i]%10 - K))  

            res=list(set(temp))   
            
        return sorted(res)    
    
    #This is a DFS with time complexity O(N * 2**N) Space Complexity O( 2**N)
        
