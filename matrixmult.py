def dot(L, K):
    result = 0
    for i in range(len(L)):
        result += L[i] * K[i]
    return result

def columnvector(matrix, column):
    vector = []
    for i in range(len(matrix)):
        vector += [matrix[i][column]]
    return vector

def matrixmult(m1, m2):
    final = [[0]*len(m1) for l in range(len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            final[i][j] = dot(m1[i], columnvector(m2, j))
    return final

def main():
    #  m1    m2
    # |1 2| |5 6|
    # |3 4| |7 8|
    m1 = [[1,2],[3,4]]
    m2 = [[5,6],[7,8]]

    print(matrixmult(m1,m2))

if __name__ == "__main__":
    main()