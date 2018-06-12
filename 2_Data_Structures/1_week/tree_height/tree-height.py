# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
	def __init__(self):
		self.children = []
	def addChild(self, node):
		self.children.append(node)

class TreeHeight:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))

	def build_tree(self):
		self.nodes = []
		for i in range(self.n):
			self.nodes.append(Node())
		for ch_ind in range(self.n):
			par_ind = self.parent[ch_ind]
			if par_ind == -1:
				self.root = ch_ind
			else:
				self.nodes[par_ind].addChild(ch_ind)

	def compute_height(self):
		if not self.nodes[self.root].children:
			return 1
		else:
			maxHeight = -float("inf")
			for child in self.nodes[self.root].children:
				self.root = child
				height = self.compute_height()
				if height > maxHeight:
					maxHeight = height
			return 1 + maxHeight

def main():
	tree = TreeHeight()
	tree.read()
	tree.build_tree()
	print(tree.compute_height())

threading.Thread(target=main).start()
