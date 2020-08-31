# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """        
        path = set()
        def dfs(x, y, dx, dy):
            # 1, Clean current
            robot.clean()
            path.add((x, y))

            # 2, Clean next
             # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                if (x + dx, y + dy) not in path and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx #(dx, dy) is direction, for example (0, 1) is up, and by using dx, dy = -dy, dx, (0,1) becomes (-1, 0), which is a left vector in x-y axis plane.

            # 3, Back to previous position and direction
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        dfs(0, 0, 0, 1)
        
