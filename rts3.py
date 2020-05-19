import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from IPython.display import clear_output
n = 8
omega = 1100
N = 256
x = np.zeros(N)
for i in range(1, n+1):
    A = np.random.random()
    phi = np.random.random()
    for t in range(N):
        x[t] += A * np.sin(omega/i * (t + 1) + phi)
plt.figure(figsize=(14, 8))
plt.title("Pseudo-random variable")
plt.plot(range(N), x, "r") # random variable
plt.show()
Fr = np.zeros(N)
Fi = np.zeros(N)
for p in range(N):
    for k in range(N):
        Fr[p] += x[k] * np.cos(2 * np.pi / N * p * k)
        Fi[p] += x[k] * np.sin(2 * np.pi / N * p * k)
Fr = Fr / N
Fi = Fi / N
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(14,14))
ax1.plot(range(N), Fr)
ax2.plot(range(N), Fi)
plt.show()