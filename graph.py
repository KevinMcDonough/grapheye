from collections import deque

class SearchableGraph:
    
    def __init__(self, graph):
        self.graph = graph

    def explore(self, start, end):
        print('RUNNING')
        path = []
        horizon = deque([start])
        explored = dict()
        while horizon:
            current = horizon.popleft()
            for node in self.graph:
                for other_node in self.graph[node]:
                    if other_node not in explored:
                        explored[other_node] = current + 1
                        if other_node == end:
                            self.runback(explored, start, end)
                            return
                        horizon.append(other_node)
                    elif explored[other_node] < explored[current] + 1:
                        explored[other_node] = explored[current] + 1
        print('No path from', start, ' to', end)

    def runback(self, explored, start, end):
        print('RUNNING BACK')
        steps = deque([])
        step = end
        while step != start:
            for neighbor in self.graph[step]:
                print step
                print neighbor
                if exploredexplored[neighbor] < explored[step]:
                        print(neighbor)
                        steps.append('('+neighbor+', '+step+')')
                        step = neighbor
        while steps:
            step = steps.popleft()
            print(step)

def main():
    raw_graph = {
        1: [2, 5],
        2: [3, 4],
        3: [6], 
        4: [5],
        5: [9],
        6: [7, 8],
        8: [9]}
    graph = SearchableGraph(raw_graph)
    graph.explore(1, 5)
if __name__ == "__main__":
    # if you call this script from the command line (the shell) it will
    # run the 'main' function
    main()
