from __future__ import print_function
import os
import operator
def lgs(seq, op=operator.lt):
    L = [0] * len(seq)
    P = [None] * len(seq)

    max_length = 0
    for i in range(len(seq)):
        it = ((L[j] + 1 if op(seq[j], seq[i]) else 1) for j in range(i + 1))
        P[i], L[i] = max(enumerate(it, 0), key=operator.itemgetter(1))
        if L[i] == 1:
            P[i] = -1
        if L[i] >= max_length:
            pos, max_length = i, L[i]

    ls = []
    while pos > -1:
        ls.append(seq[pos])
        pos = P[pos]

    return ls[::-1]

def lgis(seq):
    return lgs(seq, op=operator.lt)

def lgds(seq):
    return lgs(seq, op=operator.gt)


if __name__ == "__main__":
    with open(os.path.join('/Users/Mcfoofa/Downloads/rosalind_lgis-6.txt')) as dataset:
        n = int(dataset.readline().strip())
        p = [int(r) for r in dataset.readline().strip().split()]

    print(*lgis(p))
    print(*lgds(p))
