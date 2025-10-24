# Sort a list of dicts by a key using lambda.

people = [{"name":"A","age":30},{"name":"B","age":25},{"name":"C","age":35}]
sorted_by_age = sorted(people, key=lambda p: p['age'])

if __name__ == '__main__':
    print("Sorted:", sorted_by_age)