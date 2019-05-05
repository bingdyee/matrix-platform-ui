# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from basics.classification import Classification

def main(argc=None):
	c = Classification()
	c.compute_gradient()


if __name__ == '__main__':
	main()
