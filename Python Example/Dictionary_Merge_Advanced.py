# Merge dictionaries and sum numeric values for duplicate keys.

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

def merge_sum(a, b):
    res = dict(a)
    for k, v in b.items():
        if k in res and isinstance(res[k], (int, float)) and isinstance(v, (int, float)):
            res[k] += v
        else:
            res[k] = v
    return res

if __name__ == '__main__':
    print("Merged:", merge_sum(a, b))