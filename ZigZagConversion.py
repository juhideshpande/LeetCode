class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>len(s): #numRows is greater len(s) all chars would be filled in individual buckets so saves space 
            return s
        
        row=0
        direction=-1 #initialize to -1 because initially we need to go down 
        result= [''] * numRows #create buckets
        
        for c in s:
            result[row]+=c
            if row==0 or row==numRows-1: #change direction as we are on top or bottom
                direction *=-1
            row+=direction
            
        return "".join(result)    
            
       #Time and Space Complexity : O(N) n is number of chars in string
