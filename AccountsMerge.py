class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emailName={}
        graph=defaultdict(set)
        for acc in accounts:
            name=acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email) #Draw an edge between two emails if they occur in the same account. 
                graph[email].add(acc[1])
                emailName[email]=name
       
        seen=set()
        answer=[]
        
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack=[email]
                allMails=[]
                while stack:
                    node = stack.pop()
                    allMails.append(node)                
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                answer.append([emailName[email]]+sorted(allMails)) 
        return answer        
                        
                
                
