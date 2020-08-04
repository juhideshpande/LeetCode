class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        partition = defaultdict(int)

        def dfs(a, p=1):
            if partition[a] != 0: return True
            partition[a] = p
            return all(partition[b] != p and dfs(b, -p) for b in graph[a])

        return all(map(dfs, graph))
