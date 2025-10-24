# Demonstrate multiple set operations and a helper to compare sets.

A = {1,2,3,4,5}
B = {4,5,6,7}

def compare_sets(a,b):
    return {
        'union': a | b,
        'intersection': a & b,
        'a_minus_b': a - b,
        'b_minus_a': b - a,
        'symmetric_diff': a ^ b
    }

if __name__ == '__main__':
    print("Compare:", compare_sets(A,B))