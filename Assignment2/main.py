

class AVL_Node:
    def __init__ (self,key):
        self.key = key
        self.leftNode = None
        self.rightNode  = None
        self.height = 1

class AVL_Tree:
    def __init__(self):
        self.root = None
    
    def tree_Height(self,node):
        if node is None:
           return -1
        
        return 1 + max(self.tree_Height(node.leftNode), self.tree_Height(node.rightNode))
    
    def balance(self,node):
        if node is None:
            return 0
        return self.tree_Height(node.leftNode) - self.tree_Height(node.rightNode)
        

    def left_rotate(self, x):
        y = x.right
        node = y.left
        y.left = x
        x.right = node
        y.height = 1 + max(self.tree_Height(y.left), self.tree_Height(y.right))
        x.height = 1 + max(self.tree_Height(x.left), self.tree_Height(x.right))
        return y
       
       

    def right_rotate(self, y):
        x = y.left
        node = x.right
        x.right = y
        y.left = node
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x
    

    def insert(self,root,key):
        if not root:
            return AVL_Node(key)
        elif key < root.key:
            root.leftNode = self.insert(root.leftNode, key)
        elif key > root.key:
            root.rightNode = self.insert(root.rightNode, key)
        else:
            return root
        

        height = self.tree_height(root)
        balance = self.balance(root)
        
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



    def find(self, root, key):

        if not root:
            return None
        if root.key == key:
        # node is found
            return root
        
        #search in left subtree
        if key < root.key:
            return self.find(root.leftNode,key)
        #if greater than search in right subtree
        elif key > root.key:
            return self.find(root.rightNode, key)
        
    def delete();
         

    def preorder():
        
    def postorder():
        
    def inorder():
        

  