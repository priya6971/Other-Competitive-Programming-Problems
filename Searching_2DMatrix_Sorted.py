## Search an element in a matrix where rows and columns are in a sorted order.
## Method definition of searching
def search_matrix(mat, n, ele):
    i = 0
    j = n - 1
    # Only one loop is required to search an element
    # Time Complexity -
    while i < n and j >= 0:
        if mat[i][j] == ele:
            print("Element Found and is at location",i,",",j)
            return
        elif mat[i][j] > ele:
            j = j - 1
        else:
            i = i + 1

## Driver code for searching an element in 2D matrix.
mat = [[10, 20, 30, 40], [12, 22, 33, 45], [14, 25, 44, 47], [16, 26, 46, 50]]
search_matrix(mat, 4, 25)