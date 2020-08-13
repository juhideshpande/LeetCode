class UndergroundSystem(object):

    def __init__(self):
        self.startJrnData ={}
        self.journeyData = collections.defaultdict(lambda: [0,0])  
        
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.startJrnData[id] = [stationName,t]     

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        
        startStation, startTime = self.startJrnData.pop(id)
        self.journeyData[(startStation,stationName)][0] += float(t-startTime)
        self.journeyData[(startStation,stationName)][1] += 1.0

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        if self.journeyData[(startStation, endStation)][1] == 0 : return (0)
        return( self.journeyData[(startStation,endStation)][0]/         self.journeyData[(startStation, endStation)][1])
    
    #time complexity : O(1) space complexity: O(P+S*2) S=is the number of stations on the network, and P = is the number of passengers making a journey concurrently during peak time.
    


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
