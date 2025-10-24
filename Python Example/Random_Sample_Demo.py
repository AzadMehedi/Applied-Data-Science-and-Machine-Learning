# Use random.sample to pick items from a list.

import random
items = list(range(10))

if __name__ == '__main__':
    print("Sample 3:", random.sample(items, 3))
    print("Shuffle copy:", random.sample(items, len(items)))