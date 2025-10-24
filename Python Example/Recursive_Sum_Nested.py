# Sum numbers in nested lists/tuples recursively.

def recursive_sum(x):
    total = 0
    for item in x:
        if isinstance(item, (list, tuple)):
            total += recursive_sum(item)
        elif isinstance(item, (int, float)):
            total += item
    return total

if __name__ == '__main__':
    print(recursive_sum([1, (2,3), [4, [5]]]))