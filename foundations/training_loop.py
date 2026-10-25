import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def train(self, X: NDArray[np.float64], y: NDArray[np.float64], epochs: int, lr: float) -> Tuple[NDArray[np.float64], float]:
        # X: (n_samples, n_features)
        # y: (n_samples,) targets
        # epochs: number of training iterations
        # lr: learning rate
        
        x = np.array(X)
        y = np.array(y)

        # Initialize weights and bias, Initialize w = zeros, b = 0
        # X.shape[1] is because the shape gives us ((x.samples),(x.features)) and we need a weight for each  feature
        w = np.zeros(X.shape[1]) 
        
        b = 0.0

        #this is no of samples we have i.e. number of data samples we have
        n = X.shape[0]

        for _ in range(epochs):
        # Model: y_hat = X @ w + b
            y_hat = X @ w + b

            # Loss: MSE = (1/n) * sum((y_hat - y)^2)
            loss = np.mean((y_hat - y)**2)

            #error
            error = y_hat - y

            #gradient calculations for weights and bias
            dw = (2/n)*(x.T @ error)
            db = (2/n)*(np.sum(error))

            #update the weights and bias
            w -= lr * dw
            b -= lr * db

        # return (np.round(w, 5), round(b, 5))
        return (np.round(w,5),np.round(b,5))
        
