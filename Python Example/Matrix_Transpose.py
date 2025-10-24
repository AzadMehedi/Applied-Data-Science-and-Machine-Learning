# Transpose a matrix using zip.

matrix =   [[1,2,3],
            [4,5,6],
            [7,8,9]]

def transpose(m):
    return [list(row) for row in zip(*m)]

if __name__ == '__main__':
    print("Transposed:", transpose(matrix))