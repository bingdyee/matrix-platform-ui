# -*- coding: utf-8 -*-
from .model import Model


class Classification(Model):

	def __init__(self, lr=0.003):
		super().__init__(lr)

	def compute_loss(self):
		print('loss')

	def compute_gradient(self):
		print('gradient', self.lr)

	def train(self):
		print('train')

	def show(self):
		pass
