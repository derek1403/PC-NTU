import numpy as np

# Lorenz '63 參數
sigma = 10.0
beta = 8.0 / 3.0
rho = 24.74

# 評估的基準狀態點
x = 0.0
y = 0.0
z = 0.0

# 定義矩陣 A
A = np.array([[  -sigma, sigma,   0.0],
              [rho - z,   -1.0,    -x],
              [      y,      x, -beta]])

# 計算特徵值 (Eigenvalues)
eigenvalues, eigenvectors = np.linalg.eig(A)
det_A = np.linalg.det(A)
trace_A = np.trace(A)

print("特徵值：", eigenvalues)
print("特徵向量：", eigenvectors)
print("矩陣 A 的行列式為：", det_A)
print("矩陣 A 的跡為：", trace_A)
