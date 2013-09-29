
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
    n = 0
    for line in input_file:
        n += 1
        node = [x for x in line.strip().split()]
        node = tuple(node)
        if node in nodes:
            # print node
            print 'n-> ', n

        # print node
        nodes.add(node)



    input_file.close()

    return nodes

if __name__ == '__main__':
     build_adjacent_graph('clustering_big.txt')