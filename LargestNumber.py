class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num =[str(n) for n in nums]
        num.sort(cmp=lambda x,y: cmp(y+x,x+y))
        #print(num.sort())
        return "".join(num).lstrip("0") or "0"
