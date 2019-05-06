# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class LinearRegression:

    def __init__(self, data_size=100, epochs=100, lr=.003, thetas=None):
        self.data_size = data_size
        self.epochs = epochs
        self.lr = lr
        self.thetas = [random.uniform(1, 5), random.uniform(1, 5)] if thetas is None else thetas
        self.ln = None
        self.train_thetas = None

    def train_op(self):
        for epoch in range(self.epochs):
            _y = self.X.dot(self.train_thetas)
            gradient = self.lr * (self.Y - _y)
            self.train_thetas[0][0] += gradient.T.dot(self.x_data.reshape(self.data_size, 1))
            self.train_thetas[1][0] += gradient.T.dot(np.ones((100, 1)))
            yield self.x_data, _y
        print('Result:', self.train_thetas.T)

    def update(self, data):
        self.ln.set_data(data[0], data[1])
        return self.ln,

    def __call__(self, *args, **kwargs):
        print('Real Values:', self.thetas)
        self.x_data = np.linspace(0, 2, self.data_size, dtype=np.float32)
        self.y_data = self.thetas[0] * self.x_data + self.thetas[1] + np.random.uniform(-.5, .5, self.data_size)
        fig, ax = plt.subplots(1, 1)
        ax.scatter(self.x_data, self.y_data, c='g')
        self.ln, = plt.plot([], [], 'ro', animated=True)
        self.train_thetas = np.random.rand(2, 1)
        print('Random Init:', self.train_thetas.T)
        self.X = np.vstack((self.x_data, np.ones(self.data_size))).T
        self.Y = self.y_data.reshape((self.data_size, 1))
        a = FuncAnimation(fig, self.update, frames=self.train_op, init_func=lambda: (self.ln,), blit=True,
                          repeat=False)
        plt.show()


class LogisticRegression:
    pass

