from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def bfs(self, start):
        visited = set()
        result = []
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
    
    def dfs(self, start):
        visited = set()
        result = []
        def _dfs(node):
            if node in visited: return
            visited.add(node)
            result.append(node)
            for neighbor in self.adj[node]:
                _dfs(neighbor)
        _dfs(start)
        return result
    
    def has_path(self, start, end):
        visited = set()
        def _dfs(node):
            if node == end: return True
            if node in visited: return False
            visited.add(node)
            for neighbor in self.adj[node]:
                if _dfs(neighbor): return True
            return False
        return _dfs(start)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2); g.add_edge(1, 3); g.add_edge(2, 4)
    print(g.bfs(1)); print(g.dfs(1))
