# Partition list into two lists by predicate.

def partition(lst, pred):
    tr, fl = [], []
    for x in lst:
        (tr if pred(x) else fl).append(x)
    return tr, fl

if __name__ == '__main__':
    print(partition(range(10), lambda x: x%2==0))