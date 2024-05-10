class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self , u , v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def dfs_util(self , v, visited):
        visited.add(v)
        print(v ,end="")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self , start):
        visited = set()
        self.dfs_util(start, visited)

