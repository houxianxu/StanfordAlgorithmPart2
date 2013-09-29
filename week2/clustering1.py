# Programming Assignment #2
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=79

# Question 1
# computing a max-spacing k-clustering, 
# which is similar to Kruskals MST Algorithm.
# file describes an undirected graph with integer edge costs.
# It has the format:
# [number_of_nodes]
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]

# Your task in this problem is to run the clustering algorithm 
# from lecture on this data set, where the target number k of 
# clusters is set to 4, and compute the maximum spacing.

def build_adjacent_graph (file_name):
	""" file -> list of tuple

	Return a list of tuple which represent the edges for a node,
	a edges is represented by a tuple which contains three number,
	the first two are vertex, the last one is the weight. i.e. (vertex, vertex, weight)

	example: [(0, 2, 100), (0, 6, 1000), (1, 5, 100)]
	"""

	input_file = open(file_name, 'r')
	num_vertex = int(input_file.readline())

	edges = []

	for data in input_file:
		vertex1, vertex2, weight = [int(i) for i in data.strip().split()]
		edge = (vertex1 - 1, vertex2 - 1, weight)
		edges.append(edge)

	input_file.close()
	return num_vertex, edges

# # unit test
# if __name__ == '__main__':
# 	print build_adjacent_graph('clustering1.txt')
# # unit test


def merge_cluster(leader1, leader2, clusters_to_leader, clusters_leader_to_elements):
	"""
		merge two clusters into one cluster.
		specifically move all vertex in the smaller cluster into the larger one,
		and delete the samller one.
	"""
	# find the vertex whose leader is leader1
	elements1 = clusters_leader_to_elements[leader1]
	num_elements1 = len(elements1)

	# find the vertex whose leader is leader2
	elements2 = clusters_leader_to_elements[leader2]
	num_elements2 = len(elements2)

	# merge to cluster in to one by setting the same leader,
	# change the smaller group


	if num_elements1 < num_elements2:
		for vertex in elements1:
			clusters_to_leader[vertex] = leader2
			clusters_leader_to_elements[leader2].append(vertex)

		clusters_leader_to_elements.pop(leader1)

	else:
		for vertex in elements2:
			clusters_to_leader[vertex] = leader1
			clusters_leader_to_elements[leader1].append(vertex)

		clusters_leader_to_elements.pop(leader2)


def k_cluster(k, n, edges):
	# initiate each vertex in a single cluster, 
	# and the value is the same vertex id, which is the leader of the cluster.
	clusters_to_leader = {}
	for vertex in range(n):
		clusters_to_leader[vertex] = vertex

	# initiate the number of elements in each cluster,
	# the key is the leader and the value is a list of vertex.
	clusters_leader_to_elements = {}
	for leader in range(n):
		clusters_leader_to_elements[leader] = [leader]



	# sort the edges by the cost
	edges = sorted(edges, key=lambda edge : edge[2])
	
	# main loop: merge clusters until getting k clusters
	for i in xrange(len(edges)):
		if len(clusters_leader_to_elements) == k:
			break

		else:
			edge = edges[i]
			v1, v2 = edge[0], edge[1]
			leader1 = clusters_to_leader[v1]
			leader2 = clusters_to_leader[v2]

			if leader1 != leader2:
				merge_cluster(leader1, leader2, clusters_to_leader, clusters_leader_to_elements)

	# find the min spacing between the cluster
	spacing = None
	# print i
	while not spacing:
		edge = edges[i]
		v1, v2 = edge[0], edge[1]
		leader1 = clusters_to_leader[v1]
		leader2 = clusters_to_leader[v2]

		if leader1 != leader2:
			spacing = edge[2]
			break
		else:
			i += 1

	return spacing
		

if __name__ == '__main__':
	n, edges = build_adjacent_graph('clustering1.txt')
	k = 4

	ans = k_cluster(k, n, edges)
	print "max-spacing is ", ans









