#!/usr/local/bin/python3

# import matplotlib
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randrange as rand

# X = [590, 540, 740, 130, 810, 300, 320, 230, 470, 620, 770, 250]
# Y = [32, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
# Z = [i for i in range(len(Y))]

X = [j + rand(50) for j in range(100, 5100, 50)]
Y = [i + rand(50) for i in range(100)]
Z = [x + y + rand(50) for x, y in zip(X, Y)]
print('len(x)', len(X))
print('len(y)', len(Y))
print('len(z)', len(Z))

# create a new scatter plot
# X = x values
# Y = y values
# Z = z values
# s = size of point
# c = color of marker
# m = marker type

# ----SINGLE 2d PLOT----
# create a new figure - this is basically a window
fig1 = plt.figure('single 2d plot title')
# create a subplot - this is the actual plot inside the window
ax1 = fig1.add_subplot(111)
# plot the data into that subplot - scatter can be one of several types
ax1.scatter(X, Y, s=60, c='red', marker='^')
# Customize the subplot
# set the title of the subplot
ax1.set_title('subplot title')
# set title for axis
ax1.set_xlabel('x label')
ax1.set_ylabel('y label')
# set the x and y axis limits
ax1.set_xlim(0, 5500)
ax1.set_ylim(0, 150)

# ---MULTIPLE 2d PLOTS---
# create new figure
fig2 = plt.figure('multiple 2d plot title')
# create an axis for each subplot
# add_subplot(<number of rows><number of cols><position in array>)
ax2_1 = fig2.add_subplot(131)
ax2_2 = fig2.add_subplot(132)
ax2_3 = fig2.add_subplot(133)
# adjust subplots to add some margin
fig2.subplots_adjust(left=0.2, wspace=0.8, top=0.8)
# plot data to each axis
ax2_1.plot(X, Y)
ax2_2.plot(X, Z)
ax2_3.plot(Y, Z)
# set titles for each subplot
ax2_1.set_title('title of first subplot')
ax2_2.set_title('title of second subplot')
ax2_3.set_title('title of third subplot')
# set limits for each axis
ax2_1.set_xlim(0, 5500)
ax2_1.set_ylim(0, 150)
ax2_2.set_xlim(0, 5500)
ax2_2.set_ylim(0, 5500)
ax2_3.set_xlim(0, 150)
ax2_3.set_ylim(0, 5500)

# ----3d PLOT----
# create a figure
fig3 = plt.figure('3d plot title')
# create a subplot/axis
ax3 = fig3.add_subplot(111, projection='3d')
# plot data
ax3.scatter(X, Y, zs=Z, zdir='z')

# display plot
plt.show()
