class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        # If size <= 2 no need to change order
        size = len(barcodes)
        if size <= 2:
            return barcodes
        
    
        # Make sorted array order by # of the value desc.
        # e.g. [1,2,2,3,3,3] -> [3,3,3,2,2,1,1] 
        # because # of 3 is top and # of 1 is bottom
        c = collections.Counter(barcodes)
        sorted_by_cnt = [ ]
        for k, cnt in c.most_common():
            sorted_by_cnt.extend([k] * cnt)
        
        new_barcodes = [0] * size
        
        j = 0 # use index
        
        # new_barcodes [3, *, 3, *, 3, *] fill even indices first, if depleted, use odd ones
        for i in range(0, size, 2):
            new_barcodes[i] = sorted_by_cnt[j]
            j += 1
            
        # new_barcodes [3, 2, 3, 2, 3, *]
        # new_barcodes [3, 2, 3, 2, 3, 1]
        for i in range(1, size, 2):
            new_barcodes[i] = sorted_by_cnt[j]
            j += 1
        
        return new_barcodes
    
  #  Time: O(nlogn), space: O(n), where n = barcodes.length
