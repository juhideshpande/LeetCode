class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if(len(flowerbed)==1):
            if(flowerbed[0]==1 and n==1):
                 return False
            else:
                return True
        
        for i in range(0,len(flowerbed)-1):
                if(flowerbed[0]==0 and flowerbed[1]==0) and n>0:
                    flowerbed[0]=1
                    n-=1
                elif (flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1) and n>0:
                    print("i",i)
                    flowerbed[i]=1
                    #print(flowerbed)
                    i+=2
                    n-=1
                    
                elif(flowerbed[-1]==0 and flowerbed[-2]==0) and n>0:
                    flowerbed[-1]=1
                    n-=1
        #print(n)           
                
                
        if(n==0):
            return True
        else:
            return False
        
