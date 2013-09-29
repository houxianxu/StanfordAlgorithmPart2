# Programming Assignment #2
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=79

# Question 2
# computing a max-spacing k-clustering, 
# which is similar to Kruskals MST Algorithm.
# run the clustering algorithm from lecture, but on a MUCH bigger graph
# It has the format:
# [# of nodes] [# of bits for each node's label]
# [first bit of node 1] ... [last bit of node 1]
# [first bit of node 2] ... [last bit of node 2]

# For example, the third line of the file
# "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.
# Your task in this problem is to run the clustering algorithm 
# from lecture on this data set, where the target number k of 
# clusters is set to 4, and compute the maximum spacing.

# The distance between two nodes u and v in this problem is 
# defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. 
# The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? 
# That is, how many clusters are needed to ensure that no pair of nodes with 
# all but 2 bits in common get split into different clusters?

# the key idea is to find the neighbors (the Hamming distance <= 2)of every nodes, then mergeing the neighbors.
# Thus, the remains haver the distace >= 3.

# ------------------------------------- help function ---------------------------------------------------- 
def inverse_bit(bit):

    if bit == '0':
        return ('1',)

    elif bit == '1':
        return ('0',)


def find_neighbor_1_2(bits):
    """ list -> list of tuple 
 
    return a list of string which has huffman distance with original str.
    >>> ('1', '0', '1')
    [('0', '0', '1'), ('1', '1', '1'), ('1', '0', '0'), ('0', '1', '1'), ('0', '0', '0'), ('1', '1', '0')]
    """

    n = len(bits)
     # huffman distance is 1
     # just change one bit in a list 
    
    for i in range(n):

        # print 'bits[:i]-> ', bits[:i]
        # print 'inverse_bit(bits[i])-> ', inverse_bit(bits[i])
        yield bits[:i] + inverse_bit(bits[i]) + bits[i+1 :]
        
        
    # huffman distance is 2
    # iteratively change two bit at the same time
    
    for i in range(n-1):
        for j in range(i+1, n):
            yield bits[:i] + inverse_bit(bits[i]) + bits[i+1: j] + inverse_bit(bits[j]) + bits[j+1:]
           

    

    
# unit test
# if __name__ == '__main__':
#     for i in find_neighbor_1_2(('1', '0', '1', '1', '0')):
#         print i
# unit test

# ------------------------------------- help function ---------------------------------------------------- 


def build_adjacent_graph (file_name):
    """ file -> list of tuple

    Return a list of list which represent the bits for a node,

    example: 
    [('1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1'), 
    ('0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '0', '1')]
    """

    input_file = open(file_name, 'r')
    num_nodes, num_bits = [int(x) for x in input_file.readline().strip().split()]

    nodes = set()
    for line in input_file:
        node = [x for x in line.strip().split()]
        node = tuple(node)
        # print node
        nodes.add(node)

    input_file.close()

    return nodes


def merge_cluster(leader1, leader2, clusters_node_to_leader, nodes_leader_to_node):
    """
        merge two clusters into one cluster.
        specifically move all node in the smaller cluster into the larger one,
        and delete the samller one.
    """
    # find the node whose leader is leader1
    elements1 = nodes_leader_to_node[leader1]
    num_elements1 = len(elements1)

    # find the node whose leader is leader2
    elements2 = nodes_leader_to_node[leader2]
    num_elements2 = len(elements2)

    # merge to cluster in to one by setting the same leader,
    # change the smaller group


    if num_elements1 < num_elements2:
        for node in elements1:
            clusters_node_to_leader[node] = leader2
            nodes_leader_to_node[leader2].append(node)

        nodes_leader_to_node.pop(leader1)

    else:
        for node in elements2:
            clusters_node_to_leader[node] = leader1
            nodes_leader_to_node[leader1].append(node)

        nodes_leader_to_node.pop(leader2)

def cluster(nodes):
    # assign eacho node as a single cluster
    clusters_node_to_leader = {} # the key is node and the value is leader of the cluster which the node belong to.
    nodes_leader_to_node = {} # the key is the leader of a cluster, the value is node in the cluster

    # initialize the two lib.
    for node in nodes:
        clusters_node_to_leader[node] = node
        nodes_leader_to_node[node] = [node]

    # go through each node
    # for each of its neigbours within 2 steps
    # merge their clusters
    for node in nodes:
        # print len(nodes_leader_to_node)
        leader1 = clusters_node_to_leader[node]
    
        for neighbour in find_neighbor_1_2(node):
            if neighbour not in clusters_node_to_leader:
                continue
            leader2 = clusters_node_to_leader[neighbour]

            if (leader1 != leader2) and (leader1 in nodes_leader_to_node) and (leader2 in nodes_leader_to_node):
                # combine the two clusters
                merge_cluster(leader1, leader2, clusters_node_to_leader, nodes_leader_to_node)

     # at the end of the loop, the left is the spacing which is >= 3
    return len(nodes_leader_to_node)

def main():
    nodes = build_adjacent_graph('clustering_big.txt')
    clusters = cluster(nodes)
    print clusters

if __name__ == '__main__':
    main()
    

