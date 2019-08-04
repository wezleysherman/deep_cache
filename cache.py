import math

class CacheSim:
	def __init__(self, path, cache_type):
		self.data_path = path
		self.cache_type = cache_type
		self.blocks = 16
		# 0 - LRU
		# 1 - LFU
		# 2 - RR
		self.replacement = 0 
		self.curr_index = 0
		self.cache = []
		self.comp_misses = 0
		self.cap_misses = 0 
		self.conf_misses = 0
		
		self.replacement_dict = {}

		if cache_type == 0:
			self.type_len = 16
			self.cache = [None] * self.blocks
		elif cache_type == 1:
			self.type_len = 8
			self.len_of_arr = math.floor(self.blocks/8)
			for i in range(self.len_of_arr):
				self.cache.append([None]*8)
		elif cache_type == 2:
			self.type_len = 4
			self.len_of_arr = math.floor(self.blocks/4)
			for i in range(self.len_of_arr):
				self.cache.append([None]*4)
		elif cache_type == 3: 
			self.type_len = 2
			self.len_of_arr = math.floor(self.blocks/2)
			for i in range(self.len_of_arr):
				self.cache.append([None]*2)
		elif cache_type == 4:
			self.type_len = 1
			self.len_of_arr = math.floor(self.blocks)
			for i in range(self.len_of_arr):
				self.cache.append([None])

	def access(self, val):
		if self.cache_type == 0:
			self.direct_mapped(val)
		elif self.cache_type == 4:
			self.fully_associative(val)
		else:
			self.n_way(val)

	def direct_mapped(self, val):
		addr = val % self.type_len
		self.cache[addr] = val
		if self.replacement == 0 or self.replacement == 1:
			if self.replacement_dict[val] == None:
				self.replacement_dict[val] = 0
			self.replacement_dict[val] += 1
		

	def n_way(self, val):
		addr = val % self.type_len
		print(self.cache)
		print(self.blocks)
		print(addr)
		for i in range(self.len_of_arr):
			print(i)
			if self.cache[i][addr] == None:
				self.cache[i][addr] = val
				return
		# Use replacement policy [LRU, MRU, LFU]

	def fully_associative(self, val):
		for i in range(self.len_of_arr):
			if self.cache[i][0] == None:
				self.cache[i][0] = val
				return

# type:
#	0 - direct mapped [24]
#	1 - eight way [8, 8, 8]
#	2 - four way [4, 4, 4, 4, 4, 4]
#	3 - two way [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#	4 - fully associative [24]

cache_sim = CacheSim("", 4)

cache_sim.access(0)
cache_sim.access(1)
cache_sim.access(2)
cache_sim.access(3)

print(cache_sim.cache)
