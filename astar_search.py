
import heapq

class AStarSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (0 + self.graph.get_heuristic(start), 0, start, [start]))
        closed_list = set()

        while open_list:
            _, cost, current, path = heapq.heappop(open_list)
            
            if current in closed_list:
                continue

            if current == goal:
                return path, cost

            closed_list.add(current)

            for neighbor, step_cost in self.graph.get_neighbors(current):
                if neighbor in closed_list:
                    continue

                new_cost = cost + step_cost
                heapq.heappush(open_list, (new_cost + self.graph.get_heuristic(neighbor), new_cost, neighbor, path + [neighbor]))

        return None, float('inf')
