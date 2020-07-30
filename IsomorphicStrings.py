class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):                  #<---Solution 1
            return False
        
#         check={}
#         reverse={}
#         for i in range(len(t)):
#             check[s[i]]=t[i]
            
#         for index, value in check.items():
#             if value not in reverse:
#                 reverse[value]=[index]
#             else:
#                 return False
            
#         for i in range(len(t)):
#                 if check[s[i]]!=t[i]:
#                     return False
#         return True    


        d1, d2 = {}, {}                    #<---Solution 2
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        print(d1,sorted(d1.values()))    
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        print(d2, sorted(d2.values()))    
        return sorted(d1.values()) == sorted(d2.values())

 
