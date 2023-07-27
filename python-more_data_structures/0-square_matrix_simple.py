def square(num):
    def helper(x):
       return x ** 2
    return list (map(helper,num))

def square_matrix_simple(matrix=[]):
    modified= list( map(square,matrix) )
    return modified
if __name__ == "__main__":
    print(square_matrix_simple([[1,2,3],[1,2]]) )

# map(function,input) -> performs function for each item of input