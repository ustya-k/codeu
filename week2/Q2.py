from btree import BinaryTree
from Q1 import get_ancestors


def _find_common_ancestor(ancestors1, ancestors2):
	'''Finds lowest common ancestors given two lists of ancestors.

	Args:
		ancestors1: list, the ancestors of first given key (including the key)
		ancestors2: list, the ancestors of second given key (including the key)

	Returns:
		element of a tree (type not specified)
		None, if at least one of the keys is not present in the tree'''
	pos1 = len(ancestors1) - 1
	pos2 = len(ancestors2) - 1
	lowest = None
	while pos1 >= 0 and pos2 >= 0 and ancestors1[pos1] == ancestors2[pos2]:
		lowest = ancestors1[pos1]
		pos1 -= 1
		pos2 -= 1
	return lowest


def get_common_ancestor(tree, key1, key2):
	'''Returns lowest common ancestor of two keys.

	Args:
		tree: BinaryTree, search is conducted on it 
		key1: element of a tree (type not specified), first given key
		key2: element of a tree (type not specified), second given key

	Returns:
		element of a tree (type not specified)
		None, if  at least one of the keys is not present in the tree
	'''
	ancestors1 = get_ancestors(tree, key1)
	ancestors2 = get_ancestors(tree, key2)
	if ancestors1:
		ancestors1 = [key1] + ancestors1
	else:
		ancestors1 = [key1]
	if ancestors2:
		ancestors2 = [key2] + ancestors2
	else:
		ancestors2 = [key2]
	return _find_common_ancestor(ancestors1, ancestors2)