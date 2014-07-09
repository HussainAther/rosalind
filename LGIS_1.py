import difflib

def problem(n, pi):
    incr = lcs(pi, sorted(pi))
    decr = lcs(pi, sorted(pi, reverse=True))
    return (incr, decr)


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open("/Users/Mcfoofa/Downloads/data.txt").readlines()
    n, pi = [l.strip() for l in dataset]
    n = int(n)
    pi = map(int, pi.split())

    for seq in problem(n, pi):
        print ' '.join(map(str, seq))