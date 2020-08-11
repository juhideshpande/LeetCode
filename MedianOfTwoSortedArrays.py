class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m > n):
            return self.findMedianSortedArrays(nums2, nums1)
        
        half = (m + n) / 2
        lo, hi = 0, m
        
        while lo <= hi:  
            i = lo + (hi - lo) / 2
            j = half - i
            if i > lo and nums1[i - 1] > nums2[j]:
                hi = i - 1
            elif i < hi and nums2[j - 1] > nums1[i]:
                lo = i + 1
            else:
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums2[j], nums1[i])

                if (m + n) % 2 != 0:  # If there are odd elements.
                    return minRight
                
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])
                
                return (maxLeft + minRight) * 0.5
            
  #    Time Complexity O(log(min(m,n)))   Space Complexity: O(1)   
        
            
        
