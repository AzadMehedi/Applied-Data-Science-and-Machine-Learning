# Simulate path joining and name extraction using pathlib.Path

from pathlib import Path

p = Path("/home/user/docs/report.txt")
print_parent = p.parent
print_name = p.name
print_suffix = p.suffix

if __name__ == '__main__':
    print("Parent:", print_parent)
    print("Name:", print_name)
    print("Suffix:", print_suffix)