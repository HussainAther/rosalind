from __future__ import print_function
from math import factorial


def maximum_matchings(seq):
    min_gc, max_gc = sorted([seq.count('G'), seq.count('C')])
    min_au, max_au = sorted([seq.count('A'), seq.count('U')])
    print (factorial(max_gc) // factorial(max_gc - min_gc) *
            factorial(max_au) // factorial(max_au - min_au))

    
maximum_matchings("ACAUACGUGUAGACUACCAGUCGCCAUUUCCACGUAAUUACCGAGCACAAAAUCAUAAAUCCUCGACAUAUGUGCAAACGACUAACCCAG")