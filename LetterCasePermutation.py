class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        output=[S]
        for i in range(len(S)):
            if S[i].isdigit():
                continue
                
            temp=[]           
            for ch in output:
                temp.append(ch[:i]+ch[i].upper()+ch[i+1:])
                temp.append(ch[:i]+ch[i].lower()+ch[i+1:])
            output=temp
       
        return output       
                
