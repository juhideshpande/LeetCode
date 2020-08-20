class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[[]]
        nums=sorted(nums)
        for num in nums:
            for i in range(len(output)):
                if output[i]+[num] not in output:
                    output+=[output[i]+[num]]
                #print(output)
        return output
        
        # if not nums:
        #     return [[]]
        # res = [[]]
        # dic = collections.Counter(nums)
        # for key, val in dic.items():
        #     tmp = []
        #     for lst in res:
        #         for i in range(1, val+1):
        #             tmp.append(lst+[key]*i)
        #     res += tmp
        # return res
        
        #Time complexity: O(2^n), space complexity: O(2^n).
