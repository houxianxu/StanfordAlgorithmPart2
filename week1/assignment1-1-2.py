# Programming Assignment #1
# Greedy jobs scheduling
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=75

# Question 1
#  In this programming problem and the next you'll code up
#  the greedy algorithms from lecture for minimizing the 
#  weighted sum of completion times.. Download the text file here. 
# This file describes a set of jobs with positive and integral weights a
#  nd lengths. It has the format
# [number_of_jobs]
# [job_1_weight] [job_1_length]
# [job_2_weight] [job_2_length]
# ...
#  For example, the third line of the file is "74 59",
#  indicating that the second job has weight 74 and length 59. 
#  You should NOT assume that edge weights or lengths are distinct. 
# Your task in this problem is to run the greedy algorithm 
# that schedules jobs in decreasing order of the difference (weight - length). 
# Recall from lecture that this algorithm is not always optimal. IMPORTANT:
# if two jobs have equal difference (weight - length), you should schedule
# the job with higher weight first. Beware: if you break ties in a different way,
# you are likely to get the wrong answer. 


# Question 2
# schedules jobs (optimally) in decreasing order of the ratio (weight/length)

# Question1 and Question2
def build_jobs(file_name):
	""" file -> list 

	Return a list of tuples which contains (weight, length)
	"""

	input_file = open(file_name, 'r')
	n = int(input_file.readline().strip())

	jobs = []
	for data in input_file:
		weight, length = [int(x) for x in data.strip().split()]
		jobs.append((weight, length))
		
	input_file.close()

	return jobs

# # test
# if __name__ == '__main__':
# 	print build_jobs('jobs.txt')


def minimum_sum(jobs, compare_function):
	"""file, function - > number

	Return the minimum of weighted sum of completion times
	"""

	# more of list.sort() -> http://docs.python.org/2/library/stdtypes.html#mutable-sequence-types
	# sort in decreasing order by weight
	jobs.sort(reverse = True) 

	# sort by compare_function in decreasing order
	jobs.sort(key = compare_function, reverse = True)

	# computer the weighted sum
	sum_jobs = 0 
	schedule_time = 0
	for job in jobs:
		weight, length = job
		schedule_time += length
		sum_jobs += schedule_time * weight

	return sum_jobs

if __name__ == '__main__':
	jobs = build_jobs('jobs.txt')

	compare_function1 = lambda (weight, length): weight - length # his algorithm is not always optimal
	compare_function2 = lambda (weight, length): float(weight) / length

	# Question1
	print "using (weight-length): ", minimum_sum(jobs, compare_function1)

	# Question2
	print "using (weight/length): ", minimum_sum(jobs, compare_function2)




