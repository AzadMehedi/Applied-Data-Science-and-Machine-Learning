# Simulate parsing simple command-line args from list.

args = ["--name","Alice","--age","30"]
it = iter(args)
parsed = {}
for a in it:
    if a.startswith("--"):
        parsed[a.lstrip("-")] = next(it, None)

if __name__ == '__main__':
    print(parsed)