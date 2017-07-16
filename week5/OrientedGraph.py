class OrientedGraph:
	'''
	Implementation of oriented graph. All of the nodes have unique values.

	Fields:
		nodes: set of Nodes, all nodes of the graph
	'''
	def __init__(self):
		self.nodes = set()

	def add(self, value, parent_value = None):
		'''
		Adds new Node to the OrientedGraph or updates existing ones.

		Args:
			value: str
			parent_value: str
		'''
		node = None
		parent = None
		for inode in self.nodes:
			if inode.value == value:
				node = inode
			if inode.value == parent_value:
				parent = inode

		if parent_value:
			if not node:
				node = Node(value)
				self.nodes.add(node)
			node.parents = node.parents.union({parent})
			parent.children = parent.children.union({node})
		else:
			if not node:
				node = Node(value)
				self.nodes.add(node)


class Node:
	'''
	Element of OrientedGraph.

	Fields:
		value: str
		parents: set of Nodes, from which Node has incoming edges
		children: set of Nodes, to which Node has outcoming edges
	'''
	def __init__(self, value = None, parents = set(), children = set()):
		self.value = value
		self.parents = parents
		self.children = children