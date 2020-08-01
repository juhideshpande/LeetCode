class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pc = Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            if i == 0:
                ps = Counter(s[:len(p)])
            else:
                ps[s[i-1]] -= 1
                if ps[s[i-1]] == 0:
                    del ps[s[i-1]]
                ps[s[i+len(p)-1]] += 1
            
            if ps == pc:
                res += [i]
        return res       
        
