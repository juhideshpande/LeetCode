class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == N:
                    ans.append(path + [n])
                else:
                    paths.append(path + [n])
        return ans
