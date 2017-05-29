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


def find_common_ancestor(ancestors1, ancestors2):
    '''Finds lowest common ancestors given two lists of ancestors.
    ancestors1 -- list of the ancestors of first given key (including the key)
    ancestors2 -- list of the ancestors of second given key (including the key)
    Returns None if at least one of the keys is not present in the tree.'''
	counter = 0
	len1 = len(ancestors1) - 1
	len2 = len(ancestors2) - 1
    lowest = None
	while counter < len1 and counter < len2 and ancestors1[len1 - counter] == ancestors2[len2 - counter]:
		lowest = ancestors1[len1 - counter]
		counter += 1
	return lowest


def get_common_ancestor(tree, key1, key2):
    '''Returns lowest common ancestor of two keys.'''
	ancestors1 = [key1] + get_ancestors(tree, key1)
	ancestors2 = [key2] + get_ancestors(tree, key2)
	return find_common_ancestor(ancestors1, ancestors2)