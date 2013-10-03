# Programming Assignment #2
# knapsack problem
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=85
# Question 1
def build_items(file_name):
	new_file = open(file_name, 'r')
	WEIGHT, n = [int(x) for x in new_file.readline().split()]

	items = [[int(x) for x in new_file.readline().split()] for i in range(n)]

	return WEIGHT, items

def knapsack(weight, items):
	# initialization
	n = len(items)
	DP = {} # memoization
	for w in xrange(weight+1):
		DP[(-1, w)] = 0

	for i in xrange(n):
		for w in xrange(weight+1):
			vi, wi = items[i][0], items[i][1]
			if wi > w:
				DP[(i, w)] = DP[(i-1, w)]
			else:
				DP[(i, w)] = max(DP[(i-1, w)], DP[(i-1, w-wi)] + vi)

		for w in xrange(weight+1):
			DP.pop((i-1, w))


	return DP[(n-1, weight)]
def main():
	WEIGHT, items = build_items('knapsack_big.txt')
	res = knapsack(WEIGHT, items)
	print res

if __name__ == '__main__':
	main()
			
