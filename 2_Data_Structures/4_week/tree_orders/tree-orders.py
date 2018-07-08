# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		self.tree = []
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.tree.append({
				'key' : a,
				'left' : b,
				'right' : c
			})
	def inOrder(self):
		self.result = []
		def in_traversal(i):
			if self.tree[i]['left'] == -1 and self.tree[i]['right'] == -1:
				self.result.append(self.tree[i]['key'])
				return
			if self.tree[i]['left'] != -1:
				in_traversal(self.tree[i]['left'])
			self.result.append(self.tree[i]['key'])
			if self.tree[i]['right'] != -1:
				in_traversal(self.tree[i]['right'])
			return
		in_traversal(0)
		return self.result

	def preOrder(self):
		self.result = []
		def pre_traversal(i):
			if self.tree[i]['left'] == -1 and self.tree[i]['right'] == -1:
				self.result.append(self.tree[i]['key'])
				return
			self.result.append(self.tree[i]['key'])
			if self.tree[i]['left'] != -1:
				pre_traversal(self.tree[i]['left'])
			if self.tree[i]['right'] != -1:
				pre_traversal(self.tree[i]['right'])
			return
		pre_traversal(0)
		return self.result

	def postOrder(self):
		self.result = []
		def post_traversal(i):
			if self.tree[i]['left'] == -1 and self.tree[i]['right'] == -1:
				self.result.append(self.tree[i]['key'])
				return
			if self.tree[i]['left'] != -1:
				post_traversal(self.tree[i]['left'])
			if self.tree[i]['right'] != -1:
				post_traversal(self.tree[i]['right'])
			self.result.append(self.tree[i]['key'])
			return		
		post_traversal(0)
		return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
