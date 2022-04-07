from Graph import Graph
import time
import networkx as nx
import matplotlib.pyplot as plt


# G = nx.Graph()
# elist = [(0, 2), (2, 3), (1, 4), (4, 8)]
# G.add_edges_from(elist)
# nx.draw(G, with_labels = True)
# plt.show()


a = nx.algorithms.from_prufer_sequence([3, 3, 3, 4])
nx.draw(a, with_labels = True)
plt.show()

def tree_to_prufer(tree):
    n = tree.number_of_nodes()
    nodes = set(number for number in range(n))

    prufer_code = []


    for i in range(n-2):
        leaves = []
        #if len(nodes) == 1:
            #print(tree.degree()[0])
            #degree_sequence = tree.degree()[0]

        degree_sequence = list(tree.degree()) # Secuencia de Grados

        # PEOR CASO: (n) + (n-1) + (n-2) + ... + (4) + (3)      con n-2 términos (Suma típica; O(n^2))
        for j in range(len(nodes)):
            if degree_sequence[j][1] == 1:
                leaves.append(degree_sequence[j][0])

        x = min(leaves)
        #print(nodes, x)
        nodes = nodes - {x}
        y = list(tree.neighbors(x))[0]
        #print(y)
        tree.remove_edge(x, y)
        prufer_code.append(y)
        #print(prufer_code)
    return prufer_code

    """
    degree_sequence = [1] * n
    for element in prufer_sequence:
        degree_sequence[element] = degree_sequence[element] + 1

    for i in range(n-2):
    """

G = nx.Graph()
list_G = [(0, 3), (1, 3), (2, 3), (3, 4), (4, 5)]
G.add_edges_from(list_G)
ej = tree_to_prufer(G)
print(ej)





# Indexado en 0
def Quadratic_Prufer_to_Tree(prufer_sequence):
    time_first = time.time_ns()

    n = len(prufer_sequence) + 2
    nodes_list = [number for number in range(0, n)]       # Ordered
    output_tree = Graph(nodes_list)

    degree_sequence = [1] * n
    for element in prufer_sequence:
        degree_sequence[element] = degree_sequence[element] + 1

    nodes = nodes_list.copy()
    prufer = prufer_sequence.copy()

    for i in range(0, n-2):
        """
        for j in range(0, n):
            if not nodes_list[j] in prufer_sequence:
                desired_vertex = nodes_list[j]
                break
        """

        j = 0
        while nodes[j] in prufer:
            j = j + 1


        output_tree.add_edge(prufer_sequence[i], nodes[j]) # O(1)
        nodes.remove(nodes[j])
        prufer.pop(0)

        #print(output_tree.print_adj())

    output_tree.add_edge(nodes[0], nodes[1])



    """
        for j in range(0, n):
            if not nodes_list[j] in prufer_sequence:
                desired_vertex = nodes_list[j]
                break
    """



    time_last = time.time_ns()
    total_time = time_last - time_first

    return [output_tree, total_time]


# a = Quadratic_Prufer_to_Tree([1, 2, 3, 3, 2])
# print(a[0].print_adj())
# print(a[1])
# print(); print()

# Indexado en 0
def Linear_Prufer_to_Tree(prufer_sequence):
    time_first = time.time_ns()

    n = len(prufer_sequence) + 2     # tree_nodes_len
    output_tree = Graph([number for number in range(0, n)])
    degree_sequence = [1] * n
    for element in prufer_sequence:
        degree_sequence[element] = degree_sequence[element] + 1


    x = degree_sequence.index(1)
    index = x
    for i in range(0, n-2):
        y = prufer_sequence[i]
        output_tree.add_edge(x, y)
        degree_sequence[y] = degree_sequence[y] - 1
        if y < index and degree_sequence[y] == 1:
            x = y
        else:
            j = index + 1
            while degree_sequence[j] != 1:
                j = j + 1
            x = j
            index = x
    index = index + 1
    output_tree.add_edge(index, x)

    # print(degree_sequence, index, x, y)
    time_last = time.time_ns()
    total_time = time_last - time_first
    return [output_tree, total_time]

# a = Linear_Prufer_to_Tree([1, 2, 3, 3, 2])
# print(a[0].print_adj())
# print(a[1])




"""
    n = len(S)
    L = set(range(1, n + 2 + 1))
    tree_edges = []
    for i in range(n):
        u, v = S[0], min(L - set(S))
        S.pop(0)
        L.remove(v)
        tree_edges.append((u, v))
    tree_edges.append((L.pop(), L.pop()))
    return tree_edges
    
    
    
    :param S: 
    :return: 
"""
