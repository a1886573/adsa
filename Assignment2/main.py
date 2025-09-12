#a1886573 Aidan Matkovic last edited 12/9/25 9:39pm : ADSA ASSIGNMENT 2 : AVL TREES

#initialising a base node class, with left and right sub nodes, a key and a height
class AVL_Node:
    def __init__ (self,key):
        self.key = key
        self.leftNode = None
        self.rightNode  = None
        self.height = 1
#initialising an AVL tree class
class AVL_Tree:
    #constructor 
    def __init__(self):
        self.root = None
    #calculates the tree height by traversing down each subtree and taking the max (+1 to accomodate for the root)
    def tree_Height(self,node):
        if node is None:
           return -1
        
        return 1 + max(self.tree_Height(node.leftNode), self.tree_Height(node.rightNode))
    
    #this parameter determines whether the tree needs balancing, based on the difference in height of the left and right subtree
    def balance(self,node):
        if node is None:
            return 0
        return self.tree_Height(node.leftNode) - self.tree_Height(node.rightNode)
        
    #the following function performs a left rotate, where x moves down to the left and y becomes the new root, moving anticlockwise
    def left_rotate(self, x):
        y = x.right
        node = y.left
        y.left = x
        x.right = node
        y.height = 1 + max(self.tree_Height(y.left), self.tree_Height(y.right))
        x.height = 1 + max(self.tree_Height(x.left), self.tree_Height(x.right))
        return y
       
       
    #the right rotate shifts the tree clockwise and moves y down, where then x becomes the new root of the subtree
    def right_rotate(self, y):
        x = y.left
        node = x.right
        x.right = y
        y.left = node
        y.height = 1 + max(self.tree_Height(y.left), self.tree_Height(y.right))
        x.height = 1 + max(self.tree_Height(x.left), self.tree_Height(x.right))
        return x
    

    def insert(self,root,key):
     
        if not root:
            return AVL_Node(key)
        #if the key is less than the root's key then it belongs to the left subtree, and hence is inserted there
        elif key < root.key:
            root.leftNode = self.insert(root.leftNode, key)
        # if greater than, then the new node must be inserted to the right
        elif key > root.key:
            root.rightNode = self.insert(root.rightNode, key)
        else:
            return root
        
        #reevaluate the height and balance parameters
        root.height = self.tree_Height(root)
        balance = self.balance(root)
        
        #based on the difference of height between the left and right subtrees and the key,
        # the following rotates are performed to ensure correct tree balance upon insertion
        # Left left rotation
        if balance > 1 and key < root.leftNode.key:
            return self.right_rotate(root)
        
        # Right right rotation
        if balance < -1 and key > root.rightNode.key:
            return self.left_rotate(root)
        
        # Left right rotation
        if balance > 1 and key > root.leftNode.key:
            root.leftNode = self.left_rotate(root.leftNode)
            return self.right_rotate(root)
        
        #Right left rotation
        if balance < -1 and key < root.rightNode.key:
            root.rightNode = self.right_rotate(root.rightNode)
            return self.left_rotate(root)
        
        return root

    
    #to get the min, the left nodes will be traversed until the bottom of the tree is reached, as the min number is always to the left
    def getMin(self, node):
        current = node
        while current.leftNode:
            current = current.leftNode
        return current
        
    def delete(self, root, key):

        if not root:
            return root
        
        #search left subtree
        if key < root.key:
            root.leftNode = self.delete(root.leftNode, key)
        #search right subtree
        elif key > root.key:
            root.rightNode = self.delete(root.rightNode, key)
        #then node found
        else: 
            if not root.leftNode:
                #node is replaced with with right child
                return root.rightNode
            elif not root.rightNode:
                #or replaced with left
                return root.leftNode
        
        #for when both children exist
        #to delete, swaps with the rightmost element at the bottom of the tree, then deletes
        minNode = self.getMin(root.rightNode)
        root.key = minNode.key
        root.rightNode = self.delete(root.rightNode, minNode.key)
        
        #reevalutes tree height and calculates balance for later recorrection if needed
        root.height = self.tree_Height(root)
        balanced  = self.balance(root)
        
        #repeat rotations, as done in insert function but as key is deleted will refer to the balance function output
        # Left left rotation
        if balanced > 1 and self.balance(root.leftNode) >= 0:
            return self.right_rotate(root)
        
        # Right right rotation
        if balanced < -1 and self.balance(root.rightNode) >= 0:
            return self.left_rotate(root)
        
        # Left right rotation
        if balanced > 1 and self.balance(root.leftNode) < 0:
            root.leftNode = self.left_rotate(root.leftNode)
            return self.right_rotate(root)
        
        #Right left rotation
        if balanced < -1 and self.balance(root.rightNode) > 0:
            root.rightNode = self.right_rotate(root.rightNode)
            return self.left_rotate(root)
        
        return root
    
    #preorder defined as root->left->right, so calls and prints in that order
    def preorder(self, root):
        if root: 
            print(root.key, end = " ")
            self.preorder(root.leftNode)
            self.preorder(root.rightNode)

    #postorder defined as left->right->root
    def postorder(self, root):
        if root:
            self.postorder(root.leftNode)
            self.postorder(root.rightNode)
            print(root.key, end = " ")

    #inorder, left->root->right
    def inorder(self, root):
        if root:
            self.inorder(root.leftNode)
            print(root.key, end = " ")
            self.inorder(root.rightNode) 




        

  