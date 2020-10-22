class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result=[]
                
        for i in range(len(asteroids)):
            while result and asteroids[i]<0<result[-1]:
                if result[-1]<-asteroids[i]:
                    result.pop()
                    continue
                    
                elif  result[-1]==-asteroids[i]:
                    result.pop()
                break
            else:    
                result.append(asteroids[i])
            
        return result    
