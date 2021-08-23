# Given the root of a binary tree, check whether it is a mirror of itself 
# (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Input: root = [1,2,2,null,3,null,3]
# Output: false
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def isSymmetric(root):
    if root is None:
        return True
    else:
        return isMirror(root.left, root.right)
    
def isMirror(left, right):
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return isMirror(left.left, right.right) and isMirror(left.right, right.left)

# Driver code
# Sample Test Case 1
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
if isSymmetric(root) == True:
    print("Symmetric Tree")
else:
    print("Not Symmetric Tree")
# Sample Test Case 2
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(3)
root.right.right = Node(3)
if isSymmetric(root) == True:
    print("Symmetric Tree")
else:
    print("Not Symmetric Tree")