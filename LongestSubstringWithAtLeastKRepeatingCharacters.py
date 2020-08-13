class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
                # split by a least frequent character (because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits
        if k> len(s) or len(s)==0:
            return 0
        if k<=1:
            return len(s)
        
        splitAt=0
        search={}
        for i in range(len(s)):
            if s[i] not in search:
                search[s[i]]=1
            else:
                search[s[i]]+=1                
        
        while splitAt < len(s) and search[s[splitAt]]>=k: # will stop at char having freq less than k
            splitAt+=1
            
        if splitAt >= len(s)-1:
            return splitAt
        
        stringBeforeSplitAt=self.longestSubstring(s[:splitAt],k) # split the string before char with freq less than k
        
        while splitAt < len(s) and search[s[splitAt]]<k: 
            splitAt+=1
            
         # Before making the second call to the string after we removed all the faulty chars,
        # we need to make sure if we have not reached the end, as if we have then the whole
        # string starting after splitAt contains chars whose freq is less than k, but if we 
        # find that our splitAt pointer is valid, make another call as this is also a valid
        # part of the string   
        
        if splitAt < len(s):
            stringAfterSplitAt=self.longestSubstring(s[splitAt:len(s)],k)
        else:
            stringAfterSplitAt= 0 # all faulty chars present
        
        return max(stringBeforeSplitAt,stringAfterSplitAt)
