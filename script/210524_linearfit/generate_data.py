#!/usr/bin/env python

import os
import numpy as np

datadir = 'data/210524_linearfit'
cmd = 'rm -rf %s; mkdir -p %s' % (datadir,datadir)
print(cmd);os.system(cmd)

xmin = 1
xmax = 2**10
num_of_points = 30
a = 1.0
b = 2.0
noise_scale = 50.0 
x = np.random.randint(xmin,xmax,num_of_points)
noise = np.random.normal(loc=0.0,scale=noise_scale,size=num_of_points)
y = a * x + b + noise

f = open('%s/random_data.csv' % datadir,'w')
for i in range(num_of_points):
	f.write('%d,%.5f,%.1f\n' % (x[i],y[i],noise_scale))
f.close()

