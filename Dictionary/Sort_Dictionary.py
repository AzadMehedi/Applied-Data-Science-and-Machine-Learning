# Sort a dictionary by keys and values.

data = {"b": 3, "a": 5, "c": 1}

sorted_by_key = dict(sorted(data.items()))
sorted_by_value = dict(sorted(data.items(), key=lambda x: x[1]))

if __name__ == '__main__':
    print("Original:", data)
    print("Sorted by key:", sorted_by_key)
    print("Sorted by value:", sorted_by_value)