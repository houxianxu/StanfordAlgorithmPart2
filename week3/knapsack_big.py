# Programming Assignment #2
# knapsack problem
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=85
# Question 2
import sys
sys.setrecursionlimit(10000)

def build_items(file_name):
	new_file = open(file_name, 'r')
	WEIGHT, n = [int(x) for x in new_file.readline().split()]

	items = [[int(x) for x in new_file.readline().split()] for i in range(n)]

	return WEIGHT, items

def knapsack_top_down(weight, items): # use recursive
	n = len(items)
	print 'n-> ', n
	DP = {} # memoization
	def knapsack_dic(i, w):
		if (i, w) in DP:
			return DP[(i, w)]
		if i == 0:
			return 0
		else:
			vi, wi = items[i][0], items[i][1]
			if wi > w:
				res = knapsack_dic(i-1, w)
				DP[(i, w)] = res

			else:
				res = max(knapsack_dic(i-1, w), knapsack_dic(i-1, w-wi) + vi)
				DP[(i, w)] = res

			return res
	return knapsack_dic(n-1, weight)

def main():
	WEIGHT, items = build_items('knapsack_big.txt')
	res = knapsack_top_down(WEIGHT, items)
	print res

if __name__ == '__main__':
	main()
			
