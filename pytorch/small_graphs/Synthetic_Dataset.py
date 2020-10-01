# Synthetic Dataset class
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim 

import numpy as np

dtype_float = torch.float
dtype_int = torch.int
device = torch.device("cpu")

class Synthetic_Dataset:
	def __init__(self, data_name, num_samples, graph_size):
		self.data_name = data_name
		self.num_samples = num_samples
		self.graph_size = graph_size

		self.adjacencies = np.zeros((self.num_samples, self.graph_size, self.graph_size))
		self.vertex_features = np.zeros((self.num_samples, self.graph_size, 1))

		if self.data_name == 'star':
			for sample in range(self.num_samples):
				center = np.random.randint(0, self.graph_size)
				for vertex in range(self.graph_size):
					if vertex != center:
						self.adjacencies[sample, vertex, center] = 1.0
						self.adjacencies[sample, center, vertex] = 1.0
						self.vertex_features[sample, vertex, 0] += 1
						self.vertex_features[sample, center, 0] += 1

		self.adjacencies = torch.from_numpy(self.adjacencies)
		self.vertex_features = torch.from_numpy(self.vertex_features)