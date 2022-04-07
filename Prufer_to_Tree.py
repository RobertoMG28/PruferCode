from Graph import Graph

# Indexado en 1
def Prufer_to_Tree(prufer_sequence):
    tree_nodes = len(prufer_sequence) + 2
    output_tree = Graph(tree_nodes)

    for i in range(1, len(prufer_sequence) + 1):
        






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
