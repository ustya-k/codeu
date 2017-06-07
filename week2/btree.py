class BinaryTree:
	'''Data structure, consists of root and two children which are trees as well (can be empty)
		self.root: root element value
		self.left: left child value
		self.right: right child value
		addRightChild: adds right child tree
		addLeftChild: adds left child tree'''
	def __init__(self,key):
		self.left = None
		self.right = None
		self.root = key

	def addRightChild(self,key):
		self.right = BinaryTree(key)
		
	def addLeftChild(self,key):
		self.left = BinaryTree(key)