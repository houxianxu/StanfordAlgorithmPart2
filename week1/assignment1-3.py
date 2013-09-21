# Programming Assignment #1-3
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=75

# Prim's minimum spanning tree algorithm -- MST
# file describes an undirected graph with integer edge costs.
# It has the format 
# [number_of_nodes] [number_of_edges]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# The task is to run Prim's minimum spanning tree algorithm on this graph. 
# You should report the overall cost of a minimum spanning tree.

# Question 3

# it is the naive algrithm which is not use heap data strcture
# the running time is O(m*n)
import random

def build_adjacent_graph (file_name):
	""" file -> list of list

	Return a list of list which represent the edges for a node
	a edges is represented by a tuple which contains three number,
	the first two are vertex, the last one is the weight. i.e. (vertex, vertex, weight)

	example: [[(0, 2, 100), (0, 6, 1000) ...], [(1, 5, 100), (1, 7, 1000)...] ...]
	"""

	input_file = open (file_name, 'r')
	num_vertex, num_edges = [int(i) for i in input_file.readline().strip().split()]

	graph = [[] for i in range(num_vertex)]

	for data in input_file:
		vertex1, vertex2, weight = [int(i) for i in data.strip().split()]
		edge = (vertex1 - 1, vertex2 - 1, weight)
		edge_reverse = (vertex2 - 1, vertex1 - 1, weight)
		graph[vertex1 - 1].append(edge)
		graph[vertex2 - 1].append(edge_reverse) # be cautious to this line, because it is an undirected graph
												#  we should add reversed edge to the vertex
												# it takes me more than an hour to debug
	input_file.close()
	return graph

## test
# if __name__ == '__main__':
# 	print build_adjacent_graph('edges.txt')
## test
VERTEX2 = 1
WEIGHT = 2
infinity = 99999999999
def prim_MST(graph):
	""" list -> list

	Return a list of edges which form the minimum spannig tree of graph
	Using prim algorithm
	"""

	n = len(graph)
	s = random.randint(0, n - 1)
	MST = set()
	visited = set() # store visited vertex
	visited.add(s)

	while len(visited) < n:
		min_edge = (None, None, infinity)
		# print 'visited-> ', visited
		for vertex in visited:
			for edge in graph[vertex]:
				if (edge[VERTEX2] not in visited) and (edge[WEIGHT] < min_edge[WEIGHT]):
					min_edge = edge

		visited.add(min_edge[VERTEX2])
		MST.add(min_edge)

	return MST

if __name__ == '__main__':

	graph = build_adjacent_graph('edges.txt')
	MST = prim_MST(graph)

	sum_MST = sum([weight for (vertex1, vertex2, weight) in MST])

	print sum_MST




