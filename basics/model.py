# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Model(metaclass=ABCMeta):

	def __init__(self, lr=0.003):
		self.lr = lr

	@abstractmethod
	def compute_loss(self):
		pass

	@abstractmethod
	def compute_gradient(self):
		pass

	@abstractmethod
	def train(self):
		pass

	def show(self):
		pass
