class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        A=s+"*"+s[::-1] #https://www.youtube.com/watch?v=c4akpqTwE5g
        cont=[0] #kmp table
        for i in range(1,len(A)):
            index=cont[i-1]
            while(index>0 and A[index]!=A[i]):#match proper suffix and proper pefix
                index=cont[index-1]
            if A[index]==A[i]:    
                cont.append(index+1)
            else: 
                cont.append(index+0)
                
        return s[cont[-1]:][::-1]+s
