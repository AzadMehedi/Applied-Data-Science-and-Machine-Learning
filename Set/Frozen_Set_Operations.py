# Demonstrate operations between sets and frozensets.

a = {1,2,3,4}
b = frozenset([3,4,5])

if __name__ == '__main__':
    print('Union: ', a|b)
    print('Intersection: ', a&b)
    print('Difference: ', a-b)