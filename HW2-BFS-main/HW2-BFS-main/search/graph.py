import networkx as nx
import os
import random

class Graph:
    def __init__(self, filename: str):
        path = "/Users/maddieblaauw/Downloads/HW2-BFS-main/data"
        #using relative paths yields error [Errno 2] No such file or directory: '/HW2-BFS-main/data'
        #maybe in relation to the missing toml file at the beginning of the project? I honestly don't know
        #but let's use full path files for this assignment due to the issues with relative paths everyone was having
        #on this assignment in particular. 
        os.chdir(path)
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def Random_Start_End(self):
        num_nodes = nx.number_of_nodes(self.graph)
        start_node = random.choice(list(self.graph.nodes))
        end_node = random.choice(list(self.graph.nodes))
        print(f"Start Node: {start_node}, End Node: {end_node}")
        return start_node, end_node

    def listNodes(self):
        return "Nodes: " + " ".join(self.graph.nodes)
    
    def equal(variable):
        return all(i == variable[0] for i in variable)

    def BfsSortPath(self, start, v, dest=None):
        v = int(v)
        queue = [start]
        visited = []
        paths_traveled = []

        while queue:
            u = queue.pop(0)
            visited.append(u)
            neighbors = nx.all_neighbors(self.graph, u)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    paths_traveled.append(u + "->" + neighbor)

        print(f"Visited: {visited}")
        print(len(visited))
        if dest is not None:
            if dest in visited:
                return "destination reachable", paths_traveled
        if dest is not None:
            if dest not in visited:
                return "destination not reachable", paths_traveled
        else:
            return "No end point designated, list of nodes provided", paths_traveled

    def ShortestPath(self, start, v, dest=None):
        v = int(v)
        queue = [start]
        visited = []
        paths_traveled = [[start]]

        while queue:
            u = queue.pop(0)
            current_path = paths_traveled[-1]
            visited.append(u)
            neighbors = nx.all_neighbors(self.graph, u)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    paths_traveled.append(new_path)
                    if neighbor == dest:
                        return paths_traveled, paths_traveled[-1], len(paths_traveled[-1])

        print(f"Visited: {visited}")
        print(len(visited))
        if dest in visited:
            return True

        return paths_traveled[-1] if dest in paths_traveled[-1] else None

# Example usage
filename = "citation_network.adjlist"
graph_instance = Graph(filename)
print(nx.number_of_nodes(graph_instance.graph))
verticies = nx.number_of_nodes(graph_instance.graph)
#print(graph_instance.listNodes())
#Graph.Random_Start_End(graph_instance.val)
start_end = graph_instance.Random_Start_End()
#print(start_node)
#Graph.BfsSortPath(graph_instance, start_end[0], verticies, start_end[1])
#graph_instance.BfsSortPath(start_end[0], verticies)
