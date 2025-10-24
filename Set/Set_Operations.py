# Perform common set operations: union, intersection, difference.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

if __name__ == '__main__':
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference (a - b):", a - b)
    print("Symmetric difference:", a ^ b)