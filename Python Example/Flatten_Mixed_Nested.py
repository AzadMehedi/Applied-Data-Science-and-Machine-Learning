# Flatten nested lists and tuples into a single list.

def flatten(x):
    out = []
    for item in x:
        if isinstance(item, (list, tuple)):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

example = [1, (2,3), [4, [5,6], (7,)], 8]

if __name__ == '__main__':
    print('Flattened: ', flatten(example))