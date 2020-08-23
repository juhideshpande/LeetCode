import random
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.d = {}
        self.sum = 0
        for i in range(len(rects)):
            self.sum += (rects[i][2] - rects[i][0]+1)*(rects[i][3]-rects[i][1]+1)
            self.d[self.sum] = i
        

    def pick(self):
        """
        :rtype: List[int]
        """
        area = random.randint(1, self.sum)
        rect = self.getRect(area)
        
        # get a random point from this rectangle
        coordinates = self.rects[rect]
        rand_x = random.randint(coordinates[0], coordinates[2])
        rand_y = random.randint(coordinates[1], coordinates[3])
        return ([rand_x, rand_y])

    def getRect(self, area):
        if area in self.d:
            return self.d[area]
        
        mini = []
        for key in self.d:
            if key > area:
                mini.append(key)
        return self.d[min(mini)]
# can be simply done as return self.d[min(key for key in self.d if key > area)] 


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
