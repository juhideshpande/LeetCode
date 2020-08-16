class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
#         opening=0
#         temp=""  #temp result
#         result=""
        
#         for i in range(len(s)):
#             if s[i]=="(":
#                 opening+=1
#             elif s[i]==")":
#                 if opening==0: # extra ) bracket that should not be append to s so skip the append statement 
#                     continue 
#                 opening-=1   
#             temp+=s[i]
            
#         #print(s)    
#         for i in range(len(temp)-1,-1,-1): # if there are more opening brackets we use this for loop
#             if temp[i]=="(" and opening>0:
#                 opening-=1
#                 continue
#             else:
#                 result+=temp[i] # now the string is in the reversed form
                
#         return result[::-1]        


        opn, close = [], []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                opn.append(i)
            elif c == ")":
                if opn: 
                    opn.pop()
                else: 
                    close.append(i)
        print(close,opn,s)            
        for i in reversed(close+opn):
            s = s[:i]+s[i+1:]
            
        return s
