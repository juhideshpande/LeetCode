class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        w=[]
        q=[]
        ans=[]
        for i in range(len(words)):
            temp=min(words[i])
            c=words[i].count(temp)
            w.append(c)
        w=sorted(w) 
       # print(w)
        
        for i in range(len(queries)):
            temp=min(queries[i])
            c=queries[i].count(temp)
            q.append(c)
        #q=sorted(q)  
        #print(q)
        
        for i in q:
            for j in w:
                if i<j:
                    #print(i,j)
                    index=len(w)-w.index(j)
                    #print(index)
                    ans.append(index)
                    break
            else:
                ans.append(0)
                    #break
        return ans             
 
