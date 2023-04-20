# Given the root of a binary tree, invert the tree, and return its root.
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

def invertTree(self, root):
    if root == None:
        return root

    #recursively call the invertTree function on the left and right subtrees, which will invert the left and right subtrees
    self.invertTree(root.left)
    self.invertTree(root.right)
    #swap the left and right child nodes of the current nodes
    root.left, root.right = root.right, root.left

    return root

root = [4,2,7,1,3,6,9]
##########
