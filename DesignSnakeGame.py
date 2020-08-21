class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.height=height
        self.width=width
        self.food=food
        self.q=collections.deque([(0,0)]) # Data Structure for snake starts from top left
        self.score=0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        headRow, headCol=self.q[-1] # points to tail of the snake game
        if direction=="U":
            headRow-=1
        elif direction=="L":
            headCol-=1   
        elif direction=="R":
            headCol+=1 
        elif direction=="D":
            headRow+=1   
            
        if headRow<0 or  headCol<0 or headRow>self.height-1 or headCol>self.width-1:
            return -1
        
        if self.food and [headRow, headCol]==self.food[0]: # if food is found
            self.food.pop(0) # earlier food will be popped
            self.q.append([headRow, headCol]) # append to tail of queue
            self.score+=1
        else:
            self.q.popleft() #when the snake moves the tail also moves hence tail is popped
            
            if [headRow, headCol] in self.q: #snake collides with its own body
                return -1
            else:
                self.q.append([headRow, headCol])
        return self.score        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
