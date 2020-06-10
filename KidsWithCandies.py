class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        answer=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies<max(candies)):
                answer.append(False)
            else:
                answer.append(True)
        return answer
