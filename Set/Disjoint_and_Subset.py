# Demonstrate isdisjoint(), issubset(), and issuperset().

a = {1,2,3}
b ={3,4,5}
c = {1,2}

if __name__ == '__main__':
    print('A and B disjoints? ', a.isdisjoint(b))
    print('C subset of A? ', c.issubset(a))
    print('A superset of C? ', a.issuperset(c))