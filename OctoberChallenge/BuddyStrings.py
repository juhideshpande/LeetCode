class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        diff=[]
        if len(A)!=len(B):
            return False
        
        if A==B and len(set(A))< len(A):
            return True
        
        for i in range(len(A)):
            if A[i]!=B[i]:
                diff.append((A[i],B[i]))
                
        return len(diff)==2 and diff[0]==diff[1][::-1] 
