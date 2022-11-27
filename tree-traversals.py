
class TreeNode:
    '''represents single node'''
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class TreeTraversal:
    '''This class has all three tree traversals'''
    def preorder_traversal(self, root):
        '''preorder: root -> left node -> right node'''
        if root:
            print(root.val, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def inorder_traversal(self, root):
        '''inorder: left node -> root -> right node'''
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=' ')
            self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        '''postorder: left node -> right node -> root'''
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=' ')


#DRIVERCODE
#Designing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Tree = TreeTraversal()

print("Preorder Traversal :",end=' ')
Tree.preorder_traversal(root)
print('')

print("Inorder Traversal :",end=' ')
Tree.inorder_traversal(root)
print('')

print("Postorder Traversal :",end=' ')
Tree.postorder_traversal(root)
print('')