class BinaryTree:
	'''
	Data structure, consists of root and two children which are trees as well (can be empty)
		self.root: root element value
		self.left: left child value
		self.right: right child value
	'''
	def __init__(self,key):
		self.left = None
		self.right = None
		self.root = key

	def addRightChild(self,key):
		'''
		Adds right child tree.

		Args:
			key: root of the tree being added (type not specified)

		Returns:
			BinaryTree, 
		'''
		self.right = BinaryTree(key)
		
	def addLeftChild(self,key):
		'''
		Adds left child tree.

		Args:
			key: root of the tree being added (type not specified)

		Returns:
			BinaryTree, 
		'''
		self.left = BinaryTree(key)