class BinaryTree:

    def __init__(self,key):
      self.left = None
      self.right = None
      self.root = key

    def addRightChild(self,key):
        self.right = BinaryTree(key)
        
    def addLeftChild(self,key):
        self.left = BinaryTree(key)



def get_ancestors(tree, key):
    if tree.root != key:
        ancestors = None

        if tree.left == None and tree.right == None:
            return None

        if tree.left != None:
            ancestors = get_ancestors(tree.left, key)
            if ancestors != None:
                ancestors.append(tree.root)
                return ancestors

        if tree.right != None:
            ancestors = get_ancestors(tree.right, key)
            if ancestors != None:
                ancestors.append(tree.root)
            return ancestors
    else:
        return []