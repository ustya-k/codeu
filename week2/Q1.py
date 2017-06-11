from btree import BinaryTree


def get_ancestors(tree, key):
	'''Returns ancestors of one key (not including itself).

	Args:
		tree: BinaryTree, search is conducted on it 
		key: element of a tree (type not specified), which ancestors algorithm is looking for
	
	Returns:
		list, ancestors of the key, beginning from the closest
		None, if the key is not present in the tree'''
	if tree.root == key:
		return []
	else:
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