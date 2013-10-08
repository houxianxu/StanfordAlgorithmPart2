# Programming Assignment #4
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=89
# implement algorithm for the all-pairs shortest-path problem
import sys
infinity = sys.maxint
import sys
sys.setrecursionlimit(10000)
def build_graph(file_name):
	new_file = open(file_name, 'r')
	n, m = [int(x) for x in new_file.readline().split()]

	graph = {}
	for line in new_file:
		# u, v, w is the tail, head and the weight of the a edge
		u, v, w = [int(x) for x in line.split()]
		graph[(u, v)] = w

	return n, graph

## unit test
# if __name__ == '__main__':
# 	print build_graph('g1.txt')
## unit test


def floyd_warshall(n, graph):
	# dp[k][i][j] = length of a shortest i-j path with all interal
	# nodes in {0, 1, 2, ..., k-1}
	# because we only need dp[k-1][x][y] to compute dp[k][i][j]
	# we can overwrite previous result
	dp = []
	print 'n->', n
	for x in xrange(2):
		temp1 = []
		for i in xrange(n):
			temp2 = []
			for j in xrange(n):
				if x == 0:
					if i == j:
						temp2.append(0)
					else:
						if (i, j) in graph:
							temp2.append(graph[(i, j)])
						else:
							temp2.append(infinity)
				else:
					temp2.append(None)
			temp1.append(temp2)
		dp.append(temp1)

	for k in xrange(1, n+1):
		print 'k->', k
		for i in xrange(n):
			for j in xrange(n):
				the first k vertex is {0, 1, ..., k-1}
				dp[k%2][i][j] = min(dp[(k-1)%2][i][k-1] + dp[(k-1)%2][k-1][j], dp[(k-1)%2][i][j])
	
	# check the negative cycle
	for i in xrange(n):
		if dp[n%2][i][i] < 0:
			return None
	return dp[n%2]

def main():
	res = infinity
	for i in xrange(1, 4):
		print 'i->', i
		n, graph = build_graph('g%i.txt' %i)
		res_list = floyd_warshall(n, graph)

		if res_list:
			for i in xrange(n):
				for j in xrange(n):
					if res_list[i][j] < res:
						res = res_list[i][j]

	print res

if __name__ == '__main__':
	main()















