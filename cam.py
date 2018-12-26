import matplotlib.pyplot as plt
import numpy as np



def horner(coeffs, s, x):
    res = 0.0
    for i in reversed(range(s - 1)):
        res = res * x + coeffs[i]
    return res

coeffs = [294.569975726124,148.608451179358,-12.8584962393538, 28.8889327437629,6.33883105861485,-0.89043629163529, 12.3786448516946, 0.165754338732521, -7.71927140996498, 0.995360127219927, 3.74959014924028, 1.01240838118284]

def f(x):
    return horner(coeffs,len(coeffs),x)
    
theta = np.arange(0, np.pi/2, 0.01)
y = []
for i in theta:
    y.append(f(i))




ax = plt.subplot(111)
ax.plot(theta, y)
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()


