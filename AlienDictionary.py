class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        #if graph is cyclic return ""
         ## The important thing is to determine the character which made, the word1 < word2 (lexiographically)
        ## so we just have to build graph with that one distinguishing character nodes, and break, donot go further for other characters after you found the distinguishing character
            
        
        graph=defaultdict(set)
        inDegree=({c:0 for word in words for c in word})
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            
            for j in range(min(len(word1), len(word2))):
                c = word1[j]
                d = word2[j]                
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        inDegree[d]+=1
                    break
                    
                if j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2): # if all chars are same while x is longer than y eg. ["abc", "ab"] return ""
                        return ""
                    
        output=[]   
        
        queue = deque([c for c in inDegree if inDegree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in graph[c]:
                inDegree[d] -= 1
                if inDegree[d] == 0:
                    queue.append(d)
                    
        if len(output)<len(inDegree): # If not all letters are in output, that means there was a cycle and so valid ordering. Return "" as per the problem description. 
            return ""
        else:
            return "".join(output)
