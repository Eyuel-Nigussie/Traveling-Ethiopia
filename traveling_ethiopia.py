from graph import Graph
from astar_search import AStarSearch

class TravelingEthiopia:
    def __init__(self, strategy, connections, heuristics):
        self.graph = Graph(connections, heuristics)
        self.strategy = strategy(self.graph)

    def find_path(self, start, goal):
        return self.strategy.search(start, goal)
