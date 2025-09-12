#a1886573 Aidan Matkovic last edited 12/9/25 11:26pm : ADSA ASSIGNMENT 2 : AVL TREES

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
    
    #gets the height, if node is not None then returns 0
    def tree_Height(self,node):
        return node.height if node else 0
    
    #this parameter determines whether the tree needs balancing, based on the difference in height of the left and right subtree
    def balance(self,node):
        if not node:
            return 0
        return self.tree_Height(node.leftNode) - self.tree_Height(node.rightNode)
        
    #the following function performs a left rotate, where a node n1 moves down to the left and node n2 becomes the new root, moving anticlockwise
    def left_rotate(self, n1):
        #node 2 is the right child of n1
        n2 = n1.rightNode
        tempNode = n2.leftNode
        
        #then node 1 is moved to the left and now becomes the left child of node 2, n2
        n2.leftNode = n1
        n1.rightNode = tempNode

        #calculates the tree height by traversing down each subtree and taking the max (+1 to accomodate for the root)
        n1.height = 1 + max(self.tree_Height(n1.leftNode), self.tree_Height(n1.rightNode))
        n2.height = 1 + max(self.tree_Height(n2.leftNode), self.tree_Height(n2.rightNode))

        return n2

    #the right rotate shifts the tree clockwise and moves a node, n2 to the right, where then n1 becomes the new root of the subtree
    def right_rotate(self, n2):
        n1 = n2.leftNode
        tempNode = n1.rightNode
        
        #node 2 is now the right child of n1
        n1.rightNode = n2
        n2.leftNode = tempNode

        n2.height = 1 + max(self.tree_Height(n2.leftNode), self.tree_Height(n2.rightNode))
        n1.height = 1 + max(self.tree_Height(n1.leftNode), self.tree_Height(n1.rightNode))

        return n1
    
    
    #insert function
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
        root.height = 1 + max(self.tree_Height(root.leftNode), self.tree_Height(root.rightNode))
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

    
    #to get the max, the right nodes will be traversed until the bottom of the tree is reached, as the max number is always to the right
    def getMax(self, node):
        current = node
        while current.rightNode:
            current = current.rightNode
        return current
    
    #delete function
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
                return root.rightNode
            #node is replaced with with right child
            elif not root.rightNode:
                #or replaced with left
                return root.leftNode
                #for when both children exist
                #to delete, swaps with the right most element at the bottom of the tree, then deletes
                #get the predecessor
            else:
                temp = self.getMax(root.leftNode)
                root.key = temp.key
                root.leftNode = self.delete(root.leftNode, temp.key)
        
        #reevalutes tree height and calculates balance for later recorrection if needed
        root.height = 1 + max(self.tree_Height(root.leftNode), self.tree_Height(root.rightNode))
        balance  = self.balance(root)
        
        #repeat rotations, as done in insert function but as key is deleted will refer to the balance function output
        # Left left rotation
        if balance > 1 and self.balance(root.leftNode) >= 0:
            return self.right_rotate(root)
        
        # Left right rotation
        if balance > 1 and self.balance(root.leftNode) < 0:
            root.leftNode = self.left_rotate(root.leftNode)
            return self.right_rotate(root)
        
        # Right right rotation
        if balance < -1 and self.balance(root.rightNode) <= 0:
            return self.left_rotate(root)
        
        #Right left rotation
        if balance < -1 and self.balance(root.rightNode) > 0:
            root.rightNode = self.right_rotate(root.rightNode)
            return self.left_rotate(root)
        
        return root
    
    #preorder defined as root->left->right, so calls and prints in that order
    def preorder(self, root):
        if root: 
            print(root.key, end=" ")
            self.preorder(root.leftNode)
            self.preorder(root.rightNode)

    #postorder defined as left->right->root
    def postorder(self, root):
        if root:
            self.postorder(root.leftNode)
            self.postorder(root.rightNode)
            print(root.key, end=" ")

    #inorder, left->root->right
    def inorder(self, root):
        if root:
            self.inorder(root.leftNode)
            print(root.key, end=" ")
            self.inorder(root.rightNode) 

#main function to process the inputs
def main():
    #firstly need to split up the command line and disect each of the tree modifications and order than it will be printed in
    commandLine = input().lstrip()
    parts = commandLine.split()
    #as the order is last in line, => -1
    printingOrder = parts[-1]
    treeModifications = parts[:-1]

    tree = AVL_Tree()
    root = None

    for move in treeModifications:
        #first character either A or D
        modification = move[0]
        #then follows the number
        number = int(move[1:])

        if modification == 'A':
            #if A then inserts
            root = tree.insert(root, number)
        elif modification == 'D':
            #if D then deletes
            root = tree.delete(root, number)
    
    #determines which order to print tree in 
    if not root:
        print("EMPTY")
    elif printingOrder == "POST":
        tree.postorder(root)
        print()
    elif printingOrder == "PRE":
        tree.preorder(root)
        print()
    elif printingOrder == "IN":
        tree.inorder(root)
        print()
#call main
if __name__ == "__main__":
    main()






    


        

  