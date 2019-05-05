# -*- coding: utf-8 -*-
from .model import Model


class LinearRegression(Model):
	"""
	Linear Regression Model
	"""
	def __init__(self, lr=0.003):
		super().__init__(lr)

	def compute_loss(self):
		pass

	def compute_gradient(self):
		pass

	def train(self, data=[]):
		pass

	def show(self):
		pass
