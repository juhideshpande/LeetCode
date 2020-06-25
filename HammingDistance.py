class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hd=0
        xbin='{0:0032b}'.format(x)
        ybin='{0:0032b}'.format(y)
        for i in range(len(xbin)):
            if xbin[i]!=ybin[i]:
                hd+=1
        return hd        
