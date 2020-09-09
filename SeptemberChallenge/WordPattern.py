class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        check={}
        reverse={}
        str=str.split(" ")
        if len(pattern)!=len(str):
            return False
        else:
            for i in range(len(str)):
                check[str[i]]=pattern[i]
            #print(check)
            
            for key, value in check.items(): 
                if value not in reverse: 
                    reverse[value] = [key] 
                else: 
                    return False
            #print(reverse)    
            
            for i in range(len(str)):
                if check[str[i]]!=pattern[i]:
                    return False
            #print(check[str[i]],pattern[i])
            return True 
        
