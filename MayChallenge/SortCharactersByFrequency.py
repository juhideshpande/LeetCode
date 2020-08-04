class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = {}
        for char in s: 
            if char not in frequency: 
                frequency[char] = 1 
            else: 
                frequency[char] += 1
                
        sorted_chars = ""
        sorted_frequencies = sorted(frequency, key=frequency.get, reverse=True)
        for k in sorted_frequencies:
                sorted_chars += k * frequency[k]
        return sorted_chars
