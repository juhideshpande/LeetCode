class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
         # idea, use sliding window, move end and obtain the freq of each letter. get the max_cnt, if end-start+1-max_cnt > k, need to reduce count of start by 1, and move start forward. update the max_len. Time O(n), Space O(1).
        # only 26 letters, can use array; other case, can use Counter
        
        
        windowStart=maxCharCount=answer=0
        charsCount=collections.Counter()
        
        for windowEnd in range(len(s)):
            charsCount[s[windowEnd]]+=1 #count each character in sliding window
            maxCharCount=max(maxCharCount,charsCount[s[windowEnd]]) #Compare the maxcount of that letter in the window
            
            while windowEnd-windowStart+1-maxCharCount>k: #if the current window contains letters that need to be changed greater than k we need to pop the letters from front of the window ie reduce the count of the start letter
                charsCount[s[windowStart]]-=1
                windowStart+=1 # move the start pointer
                
            answer=max(answer,windowEnd-windowStart+1)    
            
        return answer  
    
    #Time Complexity and Space Complexity: O(26N)
                
                
            
            
            
