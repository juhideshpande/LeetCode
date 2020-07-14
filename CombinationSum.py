class Solution(object):            
            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combSum(candidates,target,res,ans,ind):
            if target<0:
                return
            if target==0:
                res.append(ans[:])            
                return
            for i in range(ind,len(candidates)):
                ans.append(candidates[i])
                combSum(candidates,target-candidates[i],res,ans,i)
                ans.pop()
        res = []
        combSum(sorted(candidates),target,res,[],0)
        return res
