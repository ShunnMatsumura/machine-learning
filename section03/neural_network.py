import numpy as np
import matplotlib.pylab as plt

class NewralNetwork:
    def step_function(x: np.ndarray) -> np.ndarray:
        return np.array(x > 0, dtype=np.int_)
    
    def sigmoid(x: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-x))
    
    def relu(x: np.ndarray) -> np.ndarray:
        return np.maximum(0, x)
    

instance = NewralNetwork
x = np.arange(-5.0, 5.0, 0.1)
y = instance.step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.savefig('section03/images/step_function.png')

y = instance.sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.savefig('section03/images/sigmoid.png')

# 行列の内積
X = np.array([1,2])
W = np.array([[1,3,5], [2,4,6]])
Y = np.dot(X, W)
print(Y)