import networkx as nx
import os
import random

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        path = "/Users/maddieblaauw/Downloads/HW2-BFS-main/data"
        os.chdir(path)
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
  
        
    def Random_Start_End(self):
        num_nodes = nx.number_of_nodes(self.graph)
        start_node = random.choice(list(self.graph.nodes))
        end_node = random.choice(list(self.graph.nodes))
        print(f"Start Node: {start_node}, End Node: {end_node}")
        return start_node, end_node
        
 
    def listNodes(self):
        theList = "Nodes: "
        for i in self.graph:
            theList += str(i)
            theList += " "
        return theList
        
        

        
  
# a modified version of BFS that stores predecessor
    def BfsSortPath(self, start, v,  dest=None):

        v=int(v)
        queue = []
        visited = []
        queue.append(start)

    # standard BFS algorithm
        while len(queue) != 0:
            u = queue.pop()
            visited.append(u)
            neighbors=nx.all_neighbors(self.graph, u)
            for neighbor in neighbors:
                if neighbor not in visited:
                    if neighbor not in queue:
                        queue.append(neighbor)
                
        print(f"Visited: {visited}")
        print(len(visited))
        if dest !=None:
            if dest in visited:
                return visited
        if dest == None:
            return ("No end point designated, list of nodes provided")

        
      
        
  
        

    
    def ShortestPath(self, start, v, dest=None):
        paths_traveled = [[start]]  
 #       v = int(v)
        queue = []
        visited = []
        queue.append(start)
        #if start exists
        if start not in self.listNodes():
            return ('Start point does not exist')
        if dest != None:
            if str(dest) not in self.listNodes():
               return ('End point does not exist on graph') 
            
        #if end exists
        #running bfs traversal on an empty graph (check if start is in graph, else hault)
        #running bfs search for an end node that does not exist in the graph 
        #print(graph_instance.listNodes())

    # standard BFS algorithm
        while len(queue) != 0:
            u = queue.pop(0)  
            current_path = paths_traveled[-1]
            visited.append(u)
            neighbors = list(nx.all_neighbors(self.graph, u))  
            for neighbor in neighbors:
                if neighbor not in visited:
                     if neighbor not in queue:
                        queue.append(neighbor)
                        new_path = current_path.copy()  
                        new_path.append(neighbor)
                        paths_traveled.append(new_path)
                        if neighbor == dest:
                            return paths_traveled[-1], len(paths_traveled[-1])

        print(f"Visited: {visited}")
        print(len(visited))
        if dest in visited:
            return True

            return paths_traveled[-1] if dest in paths_traveled[-1] else None
        
        #prints None if no path exists
        return ("None")

        
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
    




filename = "citation_network.adjlist"
graph_instance = Graph(filename)
print(nx.number_of_nodes(graph_instance.graph))
verticies=nx.number_of_nodes(graph_instance.graph)
#print(graph_instance.listNodes())
#Graph.Random_Start_End(graph_instance.val)
start_end=Graph.Random_Start_End(graph_instance)
#print(start_node)
#Graph.BfsSortPath(graph_instance, start_end[0], verticies, start_end[1])
Graph.BfsSortPath(graph_instance, start_end[0], verticies)


Graph.ShortestPath(graph_instance, start_end[0], verticies, "ngrnriu")

#Graph.ShortestPath(graph_instance, "ngrnriu", start_end[1], verticies)
#Graph.ShortestPath(graph_instance, "ngrnriu", start_end[1], verticies)


#pseudocode for shortest path
#use BfsSortPath
#start at designated start
#keep list of paths traveled
#do this by 
    #at beginning of node pull path traveled that starts with start, ending with current
    #then with each round, go back and clone that specific one and add on whatever neighbors exist
    #optional: can keep round count going; in theory, should match length of path traveled from beginning to end at the end
#at end of each round check if end was reached
    #can confirm that correct path was pulled by searching list of paths for items that begin with start and end with end 
    
    



