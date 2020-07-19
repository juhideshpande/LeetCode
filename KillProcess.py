import collections
class Solution:
  def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]       
        """
        result=[]                          #<---BFS + Dictionary
        tree=collections.defaultdict(list)
        queue=collections.deque()
        
        for i, parent in enumerate(ppid):
            tree[parent].append(pid[i])
            
        queue.append(kill)
        
        while queue:
            parent=queue.popleft()
            result.append(parent)
            
            queue.extend(tree[parent])
            
        return result    
            
x=Solution()
print(x.killProcess(pid =  [1, 3, 10, 5],ppid = [3, 0, 5, 3],kill = 5))
