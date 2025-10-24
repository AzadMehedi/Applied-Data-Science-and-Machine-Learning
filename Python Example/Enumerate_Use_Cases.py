# Use enumerate to iterate with indices.

colors = ["red","green","blue"]

if __name__ == '__main__':
    for idx, color in enumerate(colors, start=1):
        print(idx, color)