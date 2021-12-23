#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:15:10 2021

@author: SamR
"""

import numpy as np
import matplotlib.pyplot as plt
import random



## N_tot values past 1000 begin to take awhile to compute
N_tot = int(input("input value for N_total: "))



INTERVAL= 1000

circle_points= 0
square_points= 0

# Total Random numbers generated= possible x
# values* possible y values
#for i in range(INTERVAL**2):
for i in range(N_tot**2):

    # Randomly generated x and y values from a
    # uniform distribution
    # Range of x and y values is -1 to 1
    rand_x= random.uniform(-1, 1)
    rand_y= random.uniform(-1, 1)

    # Distance between (x, y) from the origin
    origin_dist= rand_x**2 + rand_y**2

    # Checking if (x, y) lies inside the circle
    if origin_dist<= 1:
        circle_points+= 1

    square_points+= 1

    # Estimating value of pi,

    pi = 4* circle_points/ square_points

##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
##    print("\n")

print("Final Estimation of Pi=", pi)
