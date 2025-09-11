# import libraries
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y1 = np.sin(x)  # sine function
y2 = y1**2  # sine squared
y3 = np.cos(x)  # cosine function
y4 = y3**2  # cosine squared

fig, ax = plt.subplots(2, 1 , sharex=True)

ax[0].plot(x, y1, label='sin(x)', color='blue')
ax[0].plot(x, y2, label='sin^2(x)', color='blue', ls='--')  # dashed line for squared functions

ax[1].plot(x, y3, label='cos(x)', color='red')
ax[1].plot(x, y4, label='cos^2(x)', color='red', ls='--')

ax[0].set_ylabel('y')
ax[1].set_ylabel('y')
#ax[1].set_xlabel('x')
fig.supxlabel("x")  # add common x label

ax[0].legend(loc='upper right')
ax[1].legend(loc='upper right')
ax[0].grid()
ax[1].grid()

plt.savefig("output/sine_cosine_plots.png", transparent = None, dpi=300)  # save figure
plt.show()