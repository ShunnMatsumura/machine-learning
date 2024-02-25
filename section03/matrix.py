import numpy as np
import matplotlib.pyplot as plt

# 行列を定義
A = np.array([[1, 2], [3, 4]])

# 原点
origin = np.zeros(2)

# プロット
plt.quiver(*origin, A[0,0], A[1,0], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(*origin, A[0,1], A[1,1], angles='xy', scale_units='xy', scale=1, color='b')

# グラフのスケールを設定
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# グリッドを表示
plt.grid()

# アスペクト比を等しく
plt.gca().set_aspect('equal', adjustable='box')

plt.savefig('section03/images/matrix.png')