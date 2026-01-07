import numpy as np

# Data
X = np.array([500, 1000, 1500])
y = np.array([10, 20, 30])

# Initial values
m = 0
c = 0
learning_rate = 0.00001
n = len(X)

# Training loop
for i in range(1000):
    y_pred = m * X + c
    dm = (-2/n) * sum(X * (y - y_pred))
    dc = (-2/n) * sum(y - y_pred)
    m = m - learning_rate * dm
    c = c - learning_rate * dc

print("Slope (m):", m)
print("Intercept (c):", c)
