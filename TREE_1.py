def problem(n, edges):
    return n - len(edges) - 1

if __name__ == '__main__':
    import doctest
    import fileinput

    doctest.testmod()

    dataset = open("/Users/Mcfoofa/Downloads/rosalind_tree-3.txt").readlines()
    n = int(dataset[0])
    edges = []
    for i in range(1, len(dataset)):
        edges.append(map(int, dataset[i].split()))
    print edges
    print problem(n, edges)