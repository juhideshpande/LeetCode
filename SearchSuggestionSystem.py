class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        res=[]
        products=sorted(products)
        for i in range(len(searchWord)):
            temp=[]
            for j in range(len(products)):
                #print(products[j])
                if searchWord[:i+1]==products[j][:i+1] and len(temp)<3:
                    #print(products[j])
                    temp.append(products[j])
            res.append(temp)
            
        return res     
            
        
