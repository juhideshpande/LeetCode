class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[[]]
        
        for num in nums:
            for i in range(len(output)):
                output+=[output[i]+[num]]
                #print(output)
        return output
        
