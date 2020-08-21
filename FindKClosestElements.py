class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # arr.sort(key = lambda i: (abs(i - x), i))
        # return sorted(arr[:k])
    
        low,high = 0,len(arr)-k
        while low < high:
            mid = (low+high)//2
            if x - arr[mid] > arr[mid+k] - x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]
    
    #Time Complexity : O(logn) Space Complexity: O(1)
