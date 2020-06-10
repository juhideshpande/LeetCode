class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_sorted=sorted(people, key= lambda x:(-x[0],x[1]))
        res=[]
        for p in people_sorted:
            res.insert(p[1],p)
        return res                     
                             
        
                             
                             