# Use dict values as sets to collect unique items per key.

data = [("a",1),("b",2),("a",2),("b",3)]
d = {}
for k,v in data:
    d.setdefault(k, set()).add(v)

if __name__ == '__main__':
    print(d)