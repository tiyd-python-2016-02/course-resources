### Import All The Things

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

%matplotlib inline
```

### Load our Data

```python
data = np.array([
    [2, 1, 2, 5, 7, 2, 3, 6, 1, 2, 5, 4, 6, 5],
    [2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7]
])
```

### Setup our Labels

```python
labels = np.array([0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1])
```

### Plot the Data

```python
colormap = np.array(['r', 'k'])
plt.scatter(data[0], data[1], c=colormap[labels], s=40)
```

### Create a Perceptron


```python
# rotate the data 180 degrees
d90 = np.rot90(data)
d90 = np.rot90(d90)
d90 = np.rot90(d90)

# Create the model
net = Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(d90, labels)

# Print the results
print("Prediction " + str(net.predict(d90)))
print("Actual     " + str(labels))
print("Accuracy   " + str(net.score(d90, labels)*100) + "%")
```

### Plot Decision Boundary

```python
# Plot the original data
plt.scatter(data[0], data[1], c=colormap[labels], s=40)

# Output the values
print("Coefficient 0 " + str(net.coef_[0, 0]))
print("Coefficient 1 " + str(net.coef_[0, 1]))
print("Bias " + str(net.intercept_))

# Calc the hyperplane (decision boundary)
ymin, ymax = plt.ylim()
w = net.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(ymin, ymax)
yy = a * xx - (net.intercept_[0]) / w[1]

# Plot the line
plt.plot(yy, xx, 'k-')
```
