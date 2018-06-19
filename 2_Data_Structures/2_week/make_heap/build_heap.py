# python3
import math

class HeapBuilder:
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		n = int(input())
		self.n = n
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
			print(swap[0], swap[1])

	def parent(self, i):
		return math.floor((i-1)/2)

	def left_child(self, i):
		return 2*i+1

	def right_child(self, i):
		return 2*i+2

	def sift_down(self, i):
		min_i = i
		l = self.left_child(i)
		if l <= self.n - 1 and self._data[l] < self._data[min_i]:
			min_i = l
		r = self.right_child(i)
		if r <= self.n - 1 and self._data[r] < self._data[min_i]:
			min_i = r

		if i != min_i:
			self._data[i], self._data[min_i] = self._data[min_i], self._data[i]
			self._swaps.append([i, min_i])
			self.sift_down(min_i)
		else:
			return

	def GenerateSwaps(self):
		for i in reversed(range(math.floor((self.n-1)/2))):
			self.sift_down(i)

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
		heap_builder = HeapBuilder()
		heap_builder.Solve()
