#!/usr/bin/env python
import sys
from numpy import log10
from scipy.misc import comb


if __name__ == '__main__':
    n = 45
    log_b = [log10(comb(2*n, i)) + i * log10(0.5) +
             (2*n - i) * log10(0.5) for i in range(n*2 + 1)]
    b = [10 ** x for x in log_b]
    log_cdf = [0 for _ in b]
    for i in range(n*2, -1, -1):
        log_cdf[i] = log10(sum([b[j] for j in range(i, n*2 + 1)]))
    print(' '.join([str(x) for x in log_cdf[1:]]))