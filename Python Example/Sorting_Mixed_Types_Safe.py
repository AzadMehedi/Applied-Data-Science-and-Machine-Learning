# Sort numbers and strings separately and combine.

items = [3, "apple", 1, "banana", 2]

nums = sorted(x for x in items if isinstance(x, int))
strs = sorted(x for x in items if isinstance(x, str))
combined = nums + strs

if __name__ == '__main__':
    print("Combined sorted:", combined)