#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
g_min = -(2**31)
g_max = (2**31) - 1
def is_bst(tree, i, min_val, max_val):
	data = tree[i][0]
	if data < min_val or data > max_val:
		return False
	if tree[i][1] == -1 and tree[i][2] != -1:
		return is_bst(tree, tree[i][2], data, max_val)
	elif tree[i][2] == -1 and tree[i][1] != -1:
		return is_bst(tree, tree[i][1], min_val, data - 1)
	elif tree[i][1] != -1 and tree[i][2] != -1:
		return (is_bst(tree, tree[i][1], min_val, data - 1)) and (is_bst(tree, tree[i][2], data, max_val))
	else:
		return True

def IsBinarySearchTree(tree):
	if not tree:
		return True
	return is_bst(tree, 0, g_min, g_max)

def main():
	nodes = int(sys.stdin.readline().strip())
	tree = []
	for i in range(nodes):
		tree.append(list(map(int, sys.stdin.readline().strip().split())))
	if IsBinarySearchTree(tree):
		print("CORRECT")
	else:
		print("INCORRECT")

threading.Thread(target=main).start()
