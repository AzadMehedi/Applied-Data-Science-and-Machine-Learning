# Use collections.defaultdict to group items.

from collections import defaultdict

pairs = [("a",1), ("b",2), ("a",3), ("b",4)]
grouped = defaultdict(list)
for k,v in pairs:
    grouped[k].append(v)

if __name__ == '__main__':
    print("Grouped:", dict(grouped))