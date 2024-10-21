class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(list) #note

        # for equation, value in zip(equations,values): #imp zip
        #     self.graph[equation[0]].append((equation[1], value))
        # print(self.graph)
        ans = []
        for (u,v), weight in zip(equations, values):
            self.graph[u].append((v, weight))
            self.graph[v].append((u,1/weight))
        print(self.graph)

        for start,end in queries:
            ans.append(self.dfs(start, end, set()))

        return ans

    def dfs(self, start, end, visited) -> float:
        if start not in self.graph or end not in self.graph:
            return -1.0

        if start==end :
            return 1.0

        visited.add(start)

        for v, weight in self.graph[start]:
            if v not in visited:
                res = self.dfs(v, end, visited)
                if res != -1.0:
                    return res*weight
        return -1.0