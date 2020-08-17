class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores={}
        res=[]
        
        for i in range(len(items)):
            if items[i][0] not in scores:
                scores[items[i][0]]=[items[i][1]]
            else:
                scores[items[i][0]].append(items[i][1])
                
        for sid,score in scores.items():
            score.sort(reverse=True)
            avg=sum(score[0:5])//5
            res.append([sid,avg])
            
        return res     
            
            
