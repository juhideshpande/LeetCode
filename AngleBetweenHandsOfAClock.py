class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        difference=0
              
        angleHour= (hour*60 + minutes)*0.5
        angleMinutes=minutes*6

        difference=abs(angleHour-angleMinutes)
        difference=min(360-difference, difference)
        
        return difference    
            
