class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        empty=0
        queue=collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):                
                if rooms[i][j]==0:
                    queue.append((i,j,0))
                    
       
        
        while queue:
            direction=[[0,1],[1,0],[0,-1],[-1,0]]
            
            x,y,d=queue.popleft()
            
            for x1, y1 in direction:
                if 0<=x+x1<len(rooms) and 0<=y+y1<len(rooms[0]) and rooms[x+x1][y+y1]==2147483647:
                    
                    rooms[x+x1][y+y1]=d+1
                    queue.append((x+x1,y+y1,d+1)) 
                    
       #Time and Space Complexity : O(mn)             
        
