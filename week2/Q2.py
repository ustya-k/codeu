from btree import BinaryTree
from Q1 import get_common_ancestor


def find_common_ancestor(ancestors1, ancestors2):
	'''Finds lowest common ancestors given two lists of ancestors.

    Args:
        ancestors1: list, the ancestors of first given key (including the key)
        ancestors2: list, the ancestors of second given key (including the key)

    Returns:
        element of a tree (type not specified)
        None, if at least one of the keys is not present in the tree'''
	counter = 0
	len1 = len(ancestors1) - 1
	len2 = len(ancestors2) - 1
	lowest = None
	while counter < len1 and counter < len2 and ancestors1[len1 - counter] == ancestors2[len2 - counter]:
		lowest = ancestors1[len1 - counter]
		counter += 1
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
	ancestors1 = [key1] + get_ancestors(tree, key1)
	ancestors2 = [key2] + get_ancestors(tree, key2)
	return find_common_ancestor(ancestors1, ancestors2)