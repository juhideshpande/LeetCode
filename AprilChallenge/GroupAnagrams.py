from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        test=defaultdict(list)
        for word in strs:
            test[''.join(sorted(word))].append(word)
        return list(test.values())    
        
