# Programming Assignment #5
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=97
# the key idea is to solving TSP by reducing to SCC
# https://class.coursera.org/algo2-002/forum/thread?thread_id=428


import math
import sys
import random

infinity = sys.maxint

def euclidean_distance(point1, point2):
	return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def build_edges(file_name):
	""" file -> dictionary
	"""

	input_file = open(file_name, 'r')
	city_n = int(input_file.readline().strip())
	cities = []
	for line in input_file:
		x, y = [float(x) for x in line.strip().split()]
		cities.append((x, y))
	
	edges_distance = {}	
	for v in xrange(city_n):
		for v2 in xrange(city_n):
				distance = euclidean_distance(cities[v], cities[v2])
				edges_distance[(v, v2)] = distance

	return city_n, edges_distance


def probe_insert_by_smallest_increment(nodes, edge_path, edges_distance):
	edges_to_add = None
	edges_to_remove = None
	# print nodes
	for i in xrange(2, len(nodes)):
		node_to_add = nodes[i]
		min_increment = infinity
		for edge in edge_path:
			node1, node2 = edge[0], edge[1]
			increment = (edges_distance[(node1, node_to_add)] + 
						edges_distance[(node_to_add, node2)] - edges_distance[(node1, node2)])

			if increment < min_increment:
				# print 'increment', increment
				min_increment = increment
				edges_to_add = [(node1, node_to_add), (node_to_add, node2)]
				edges_to_remove = (node1, node2)

		edge_path.add(edges_to_add[0])
		edge_path.add(edges_to_add[1])
		edge_path.remove(edges_to_remove)
	# print 'edge_path->', edge_path

	res = 0
	for edge in edge_path:
		res += edges_distance[edge]

	return res



def main():
	n, edges_distance = build_edges('tsp.txt')
	nodes = [x for x in xrange(n)]

	res = infinity
	for i in xrange(100):
		# print 'i->', i
		random.shuffle(nodes)
		edge_path = set()
		edge_path.add((nodes[0], nodes[1]))
		edge_path.add((nodes[1], nodes[0]))
		
		temp_res = probe_insert_by_smallest_increment(nodes, edge_path, edges_distance)
		res = min(res, temp_res)

	print res

if __name__ == '__main__':
	main()







