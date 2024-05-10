class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, queue):
        if not queue:
            return
        current_node = queue.pop(0)
        print(current_node, end=' ')
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        self.bfs(queue)

    def bfs_traversal(self, start):
        global visited
        visited = set()
        visited.add(start)
        queue = [start]
        self.bfs(queue)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print("BFS Traversal starting from vertex 0:")
g.bfs_traversal(0)
