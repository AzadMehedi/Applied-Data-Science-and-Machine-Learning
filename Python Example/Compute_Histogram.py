# Build a histogram normalized to probabilities.

from collections import Counter

data = [1,2,2,3,3,3]
c = Counter(data)
total = sum(c.values())
prob = {k: v/total for k,v in c.items()}


if __name__ == '__main__':
    print(prob)