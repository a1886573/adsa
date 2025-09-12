

class AVL_Node:
    def __init__ (self,key):
        self.key
        self.leftNode = None
        self.rightNode  = None
        self.height = 1

class AVL_Tree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        node = y.left
        y.left = x
        x.right = node
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return y
       
       

    def right_rotate(self, y):
        x = y.left
        node = x.right
        x.right = y
        y.left = node
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x
    

    def insert():

    def delete():

    def find():

    def preorder():
        
    def postorder():
        
    def inorder():
        

  