#!/usr/bin/python3
# file: __init__.py.py
# Created by Guang at 19-9-17
# description:

# *-* coding:utf8 *-*

# 随机游走
# import matplotlib.pyplot as plt
# import random
# position = 0
# walk = [position]
# steps = 200
# for i in range(steps):
#   step = 1 if random.randint(0, 1) else -1
#   position += step
#   walk.append(position)
# fig = plt.figure()
# plt.title("www.jb51.net")
# ax = fig.add_subplot(111)
# ax.plot(walk)
# plt.show()


# # 随机游走
# import matplotlib.pyplot as plt
# import numpy as np
# nsteps = 200
# draws = np.random.randint(0, 2, size=nsteps)
# steps = np.where(draws > 0, 1, -1)
# walk = steps.cumsum()
# fig = plt.figure()
# plt.title("www.jb51.net")
# ax = fig.add_subplot(111)
# ax.plot(walk)
# plt.show()

# 随机游走
import matplotlib.pyplot as plt
import numpy as np
nwalks = 5
nsteps = 200
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
fig = plt.figure()
plt.title("www.jb51.net")
ax = fig.add_subplot(111)
for i in range(nwalks):
  ax.plot(walks[i])
plt.show()
