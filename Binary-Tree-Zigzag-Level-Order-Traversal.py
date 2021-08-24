# Given the root of a binary tree, return the zigzag level order traversal of its nodes values. 
# (i.e., from left to right, then right to left for the next level and alternate between).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def zigzagOrder(root):
    ret = []
    level_list = deque()
    if root is None:
        return []
        
    queue = deque([root, None])
    is_order_left = True

    while len(queue) > 0:
        curr_node = queue.popleft()

        if curr_node:
            if is_order_left:
                level_list.append(curr_node.val)
            else:
                level_list.appendleft(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        else:
            # we finish one level
            ret.append(level_list)
                
            if len(queue) > 0:
                queue.append(None)

            level_list = deque()
            is_order_left = not is_order_left
    for i in range(len(ret)):
        print(ret[i], end=' ')
    return ret

# Driver code
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
zigzagOrder(root)