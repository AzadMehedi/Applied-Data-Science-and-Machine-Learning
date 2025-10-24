# Simple split-based date parsing.

s = '2025-10-17'
y,m,d = s.split('-')

if __name__ == '__main__':
    print(y, m, d)