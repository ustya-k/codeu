class BinaryTree:
	'''Data structure, consists of root and two children which are trees as well (can be empty)
	self.root -- root element value
	self.left -- left child value
	self.right -- right child value
	addRightChild -- adds right child tree
	addLeftChild -- adds left child tree'''
	def __init__(self,key):
		self.left = None
		self.right = None
		self.root = key

	def addRightChild(self,key):
		self.right = BinaryTree(key)
		
	def addLeftChild(self,key):
		self.left = BinaryTree(key)



def get_ancestors(tree, key):
	'''Returns ancestors of one key (not including itself).
	tree -- BinaryTree on which search is conducted
	Returns list of ancestors, beginning from the closest.
	Returns None if the key is not present in the tree.'''
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