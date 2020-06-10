class Solution(object):  
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        x=set(arr)
        L=[]
        for i in x:
            if i+1 in arr:
                item_count=arr.count(i)
                L.append(item_count)
        return sum(L)        
        
        
x=Solution()
print(x.countElements([1,1,2,3,3,5,5,6,6,7]))     
