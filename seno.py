import numpy as np
import matplotlib.pylab as plt

t = np.linspace(0,2*np.pi,2000)

y = np.cos(t)

plt.figure()
plt.plot(t,y)
plt.xlabel("t")
plt.ylabel("cos(t)")
plt.savefig("coseno")

