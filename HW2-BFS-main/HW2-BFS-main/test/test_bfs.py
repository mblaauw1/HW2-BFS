import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))

import pytest
import networkx as nx
from search.graph import Graph  # Replace with the actual module name

# Set up common resources
filename = "citation_network.adjlist"
graph_instance = Graph(filename)
start_end = graph_instance.Random_Start_End()
start_node = start_end[0]
end_node = start_end[1]

@pytest.fixture
def test_bfs_sort_path():
    vertices = nx.number_of_nodes(graph_instance.graph)

    result = graph_instance.BfsSortPath(start_node, vertices)

    assert nx.number_of_nodes(graph_instance.graph) == len(result[1]) + 1

def test_shortest_path():
    vertices = nx.number_of_nodes(graph_instance.graph)

    result = graph_instance.ShortestPath(start_node, vertices, end_node)
    paths_traveled_tests=result[0]
    assert int(nx.number_of_nodes(graph_instance.graph)) >= int(result[2])
    last_list=result[1]
    assert last_list[-1]==end_node
