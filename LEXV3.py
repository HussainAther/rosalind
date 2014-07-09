def alpha_combs(alphabet, n, acc='', res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc + c)
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


def result(s):
    bits = s.split()
    alphabet = bits[:-1]
    length = int(bits[-1])
    return alpha_combs(alphabet, length)


if __name__ == "__main__":

    small_dataset = "M U V T O K A C Q L\n3"
    large_dataset = open('/Users/Mcfoofa/Downloads/rosalind_lexv.txt').read().strip()

    print "\n".join(result(large_dataset))