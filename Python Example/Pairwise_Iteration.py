# Iterate pairwise over a list.

def pairwise(iterable):
    it = iter(iterable)
    prev = next(it, None)
    for curr in it:
        yield prev, curr
        prev = curr

if __name__ == '__main__':
    print(list(pairwise([1,2,3,4])))