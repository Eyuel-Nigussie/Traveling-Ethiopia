class Graph:
    def __init__(self, connections, heuristics):
        self.graph = {}
        self.heuristics = heuristics
        for city, edges in connections.items():
            self.graph[city] = edges

    def get_neighbors(self, city):
        return self.graph.get(city, [])

    def get_heuristic(self, city):
        return self.heuristics.get(city, float('inf'))

    def get_cost(self, from_city, to_city):
        for neighbor, cost in self.graph.get(from_city, []):
            if neighbor == to_city:
                return cost
        return float('inf')
