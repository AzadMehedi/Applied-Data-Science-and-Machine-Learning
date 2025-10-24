# Use Counter to count items easily.

from collections import Counter

items = ["apple","banana","apple","orange","banana","apple"]
c = Counter(items)

if __name__ == '__main__':
    print("Most common:", c.most_common(2))
    print("Counts:", dict(c))