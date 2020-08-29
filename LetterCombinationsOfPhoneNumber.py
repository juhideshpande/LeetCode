class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        output=[""] if digits else []
                
        phone={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs", "8": "tuv", "9":"wxyz"}
        
        for num in digits:
            curr=[]
            #print("now in num",num)
            letters=phone[num]
            for l in letters: 
                for prev in output:
                    curr.append(prev+l)
                    # print(curr,"curr")
                    # print("op",output)
            output=curr        
        
        return output
                
            
            
