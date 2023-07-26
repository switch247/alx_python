def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), end= " " if j !=len(matrix[i])-1 else '\n')

if __name__ == "__main__":
    print_matrix_integer(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 )