class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        result=[]
        temp=None
        for i in range(len(prices)):                
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    temp=prices[i]-prices[j]
                    result.append(temp)
                    temp=0
                    break
            else:
                result.append(prices[i])
        return result            
                
        
