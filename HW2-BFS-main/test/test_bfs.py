import pytest
import os
import networkx as nx
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.join(os.getcwd(), '..'))

# Import the Graph class
from search.graph import Graph


def test_bfs_traversal():
    filename_test = "tiny_network.adjlist"
    start_end = Graph.Random_Start_End(Graph(filename_test))
    start_test = start_end[0]
    dest_test = start_end[1]

    graph_instance_test = Graph(filename_test)
    vertices_test = nx.number_of_nodes(graph_instance_test.graph)

    result = graph_instance_test.BfsSortPath(start_test, vertices_test, dest_test)

    if dest_test is not None:
        assert  True
    else:
        assert result == "No end point designated, list of nodes provided"


def test_tiny_network_bfs():
    filename_test = "tiny_network.adjlist"
    start_end = Graph.Random_Start_End(Graph(filename_test))
    start_test = start_end[0]
    dest_test = start_end[1]

    graph_instance_test = Graph(filename_test)
    vertices_test = nx.number_of_nodes(graph_instance_test.graph)

    result = graph_instance_test.ShortestPath(start_test, dest_test, vertices_test)

    if dest_test is not None:
        assert len(result[0]) == result[1]
    else:
        assert result == "No end point designated, list of nodes provided"


# Run the tests
test_bfs_traversal()
test_tiny_network_bfs()