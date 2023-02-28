
import matplotlib.pyplot as plt
import numpy as np
import mymodule as mm
x = np.linspace(0, 0.7 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
print("xxxxxxx")

mm.hello()
print("Hello myproject")