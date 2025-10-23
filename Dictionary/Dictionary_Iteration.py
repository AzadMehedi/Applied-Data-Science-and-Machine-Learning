# Show different ways to iterate through a dictionary.

student = {'name':'Mehedi', 'age':29, 'grade':'A'}

if __name__ == '__main__':
    print("Keys:")
    for key in student:
        print(key)
    print("\nValues:")
    for value in student.values():
        print(value)
    print("\nItems:")
    for key, value in student.items():
        print(f"{key} => {value}")