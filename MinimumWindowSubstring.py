class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        length = len(s) + 1
        ans = ''
        counter_t = collections.Counter(t)
        i, required, find =0, len(counter_t), 0
        counter = collections.Counter()
        
        for j in range(len(s)):
            counter[s[j]] += 1
            if s[j] in counter_t and counter[s[j]] == counter_t[s[j]]:
                find += 1
            while i <= j and find == required:
                if length > j - i + 1:
                    ans = s[i: j+1]
                    length = j - i + 1
                counter[s[i]] -= 1
                if s[i] in counter_t and counter[s[i]] < counter_t[s[i]]:
                    find -= 1
                i += 1

        return ans
    
    
   # Time Complexity :O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T.
#Space Complexity : O(∣S∣+∣T∣)

