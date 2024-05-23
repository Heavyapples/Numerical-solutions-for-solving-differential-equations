import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 定义微分方程函数
def func(x, y):
    return -y**2 + 2*x**2 + 6

# 定义初值条件
y0 = [1]

# 定义区间
x_range = (0, 3)

# 求解微分方程
sol = solve_ivp(func, x_range, y0, t_eval=np.linspace(0, 3, 100))

# 打印数值解
for x, y in zip(sol.t, sol.y[0]):
    print(f"x: {x}, y: {y}")
    
# 绘制解的图形
plt.plot(sol.t, sol.y[0])
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("Numerical solution of the differential equation")
plt.show()
