# Programming Assignment #6
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=93
# the key idea is to solving TSP by heuristic: Greedy + Randomization
# check "https://class.coursera.org/algo2-002/forum/thread?thread_id=379" for details
# the run time is O(n**2), which is awesome!

import sys
import threading

def buildAdjList(file_name):
	""" file -> list of list1, list of list2

	Return two list of lists, which represent two graphs,
	the second one is the reverse version of the first one.

	the index of the list is the number of the vertex
	and the value of the according index is the adjacent vertex

	example: 
			[[2, 3, 4], [6, 3]] -> the 0 vertex has edges to 2, 3, 4 vertex
								   the 1 vertex has edges to 6, 3 vertex

	"""
	input_file = open(file_name, 'r')
	adjList = []
	adjList_reversion = []
	n = input_file.readline()
	
	for line in input_file:
		# calculate the vertex and one adjacent vertex accordingly
		vertexFrom, vertexTo = map(int, line.strip().split())
		maxVertex = max(vertexFrom, vertexTo)

		# construct all the vertex list that less than maxVertex
		length = len(adjList)
		while length < maxVertex:
			adjList.append([])
			length += 1

		# construct all the vertex list that less than maxVertex
		# for reversion which is the same as the last one
		lengthReverse = len(adjList_reversion)
		while lengthReverse < maxVertex:
			adjList_reversion.append([])
			lengthReverse += 1

		# changed for two-SAT problem
		adjList[-(vertexFrom-1)].append(vertexTo-1)
		adjList_reversion[vertexTo-1].append(-(vertexFrom-1))

		adjList[-(vertexTo-1)].append(vertexFrom-1)
		adjList_reversion[vertexFrom-1].append(-(vertexTo-1))


	input_file.close()
	return adjList, adjList_reversion

# test
# print buildAdjList('test.txt')
# test

explored = None
vertexNewOrder = None
order = 0
explored = None
sccSize = 0

def DFS_LOOP_reversed(graphRversed):
	"""
	return the order of the vertices for the next loop.
	"""

	global explored, vertexNewOrder, order
	n = len(graphRversed)

	explored = [False] * n
	vertexNewOrder = [None] * n
	order = 0

	for vertex in reversed(range(n)):
		if not explored[vertex]:
			DFS_reversed(graphRversed, vertex)


def DFS_reversed(graphRversed, vertex):

	global order, explored

	explored[vertex] = True

	for adjVertex in graphRversed[vertex]:
		if not explored[adjVertex]:
			DFS_reversed(graphRversed, adjVertex)

	# calculate new order for every vertex
	vertexNewOrder[order] = vertex
	order += 1


def DFS_LOOP(graph):

	global sccSize, explored, vertexNewOrder

	n = len(graph)
	explored = [False] * n
	sccSizeList = []

	for vertex in reversed(range(n)):
		if not explored[vertexNewOrder[vertex]]:
			sccSize = 0
			DFS(graph, vertexNewOrder[vertex])
			sccSizeList.append(sccSize)

	return sccSizeList

def DFS(graph, vertex):

	global explored, sccSize

	explored[vertex] = True

	for adjVertex in graph[vertex]:
		if not explored[adjVertex]:
			DFS(graph, adjVertex)

	sccSize += 1

def main():


	graph, graphRversed = buildAdjList('2sat1.txt')

	DFS_LOOP_reversed(graphRversed)

	sccSizeList = DFS_LOOP(graph)
	sccSizeList.sort()
	sccSizeList.reverse()
	res = sccSizeList[:5]

	# if res has less than 5 SCC, then add 0 to make up
	if len(res) < 5:
		n = 5 - len(res)

		while n > 0:
			res.append(0)
			n = n-1
	print res




if __name__ == '__main__':
	threading.stack_size(2**27)
	sys.setrecursionlimit(10**9)
	thread = threading.Thread(target = main)
	thread.start()
