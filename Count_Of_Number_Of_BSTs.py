## Method Definition
## Concept - Number of Binary Search Tree for given n is equal to Catalan Number 
## Catalan Number Series - C_n = summation(C_i-1 * C_n-i)
## Time Complexity - O(N * N!) 
def uniqueNumberBST(n):
    n1, n2, sum = 0, 0, 0
    if n == 0 or n == 1:
        return 1
    
    for i in range(1, n+1):
        ## Recursive Function Calls for calculating catalan series
        n1 = uniqueNumberBST(i-1)
        n2 = uniqueNumberBST(n-i)
        sum += n1 * n2
    return sum

## Driver code
n = 9
print("Count of Unique Number of BST given value of n as",n,"is",uniqueNumberBST(n))