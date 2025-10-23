# Example of returning multiple values using tuples.

def min_max_sum(values):
    return (min(values), max(values), sum(values))

if __name__ == '__main__':
    nums = (5,10,15,20)
    min, max, total = min_max_sum(nums)
    print(f'Min: {min}, Max: {max}, Sum: {total}')