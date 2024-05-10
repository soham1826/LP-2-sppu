class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u ,v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self , start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v ,end="")

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


g = Graph()
g.add_edge(0,1)
g.add_edge(1,3)
g.add_edge(3,2)
g.add_edge(2,4)
g.add_edge(4,1)

print("\nBreadth First Traversal (BFS):")
g.bfs(3)

