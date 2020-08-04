class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
       
        indegree, outdegree = collections.defaultdict(set), collections.defaultdict(set)
        for x, y in prerequisites:
            outdegree[y].add(x)
            indegree[x].add(y)
        count = 0
        zero_degree = []
        for i in range(numCourses):
            if not indegree[i]:
                zero_degree.append(i)
                count += 1
        while zero_degree:
            node = zero_degree.pop()
            for x in outdegree[node]:
                indegree[x].remove(node)
                if not indegree[x]:
                    zero_degree.append(x)
                    count += 1
        return count == numCourses
