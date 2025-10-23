# Invert keys and values of a dictionary.

mapping = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in mapping.items()}

if __name__ == '__main__':
    print("Original:", mapping)
    print("Inverted:", inverted)