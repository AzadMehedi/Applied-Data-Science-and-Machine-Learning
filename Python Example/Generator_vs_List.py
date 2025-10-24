# Compare memory use briefly (demonstration only).

def make_list(n):
    return [i for i in range(n)]

def make_gen(n):
    for i in range(n):
        yield i 

if __name__ == '__main__':
    print('First 5 from gen: ', [x for x in make_gen(5)])
    print('List 5: ', make_list(5)[:5])