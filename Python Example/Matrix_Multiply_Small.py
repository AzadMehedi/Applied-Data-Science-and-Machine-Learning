# Multiply two matrices (small) using nested loops.

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

if __name__ == '__main__':
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    print(matmul(A,B))