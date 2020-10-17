class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequence=defaultdict(int)
        for i in range(len(s)-9):
            sequence[s[i:i+10]]+=1
        ans=[]
        for i in sequence.keys():
            if sequence[i]>1:
                ans.append(i)
        return ans
