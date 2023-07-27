def square(num):
    return num ** 2
def square_matrix_simple(matrix=[]):
    modified= list( map(square,matrix) )
    # print(modified)
    return modified
if __name__ == "__main__":
    print(square_matrix_simple([1,2,3]) )

# map(function,input) -> performs function for each item of input