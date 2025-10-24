# Use all() and any() with conditions.

nums = [2,4,6,8,9]

if __name__ == '__main__':
    print('All even? ', all(n%2==0 for n in nums))
    print('Any odd? ', any(n%2!=0 for n in nums))