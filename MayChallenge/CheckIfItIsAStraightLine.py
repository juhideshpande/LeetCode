class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if(len(coordinates)==2):
            return True
        else:
            x1=coordinates[0][0]
            y1=coordinates[0][1]
            x2=coordinates[1][0]
            y2=coordinates[1][1]
            #print(x1,y1,x2,y2)
            for x3,y3 in coordinates[2:]:
                if ((y3-y2)*(x2-x1)!=(y2-y1)*(x3-x2)):
                    return False
            return True    
            
