#!/usr/bin/env python

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from iminuit import Minuit
from probfit import Chi2Regression, linear

xmin = 1
xmax = 2**10
#num_of_points = 30
a = 1.0
b = 2.0
#noise_scale = 100

df = pd.read_csv('data/210524_linearfit/random_data.csv',
	names=['x','y','ye'])

fig, axs = plt.subplots(2,1, figsize=(10,8),
	sharex=True, gridspec_kw={'hspace': 0})

gs = gridspec.GridSpec(2,1,height_ratios=[4,1])
gs.update(hspace=0.0) 
axs0 = plt.subplot(gs[0])
axs0.errorbar(df['x'],df['y'],yerr=df['ye'],
	fmt='o',markersize=4.0)
axs0.set_ylabel('Y')

x2r = Chi2Regression(linear, 
	np.array(df['x']), np.array(df['y']),
	np.array(df['ye']))
fit = Minuit(x2r, m=a, c=b)
fit.migrad()
fit.minos() 
print(fit.print_param())
print(fit.values)
print(fit.errors)

a_fit = fit.values[0]
b_fit = fit.values[1]
print(a_fit,b_fit)

x_fit = np.linspace(xmin,xmax)
y_fit = a_fit * x_fit + b_fit
axs0.plot(x_fit,y_fit,'--r')

df['y_model'] = a_fit * df['x'] + b_fit
residual_fit = df['y'] - df['y_model'] 
resratio_fit = residual_fit/df['y_model']*100.0
resratio_err = df['ye']/df['y_model']*100
axs1 = plt.subplot(gs[1])
axs1.errorbar(df['x'],resratio_fit,yerr=resratio_err,
	fmt='o',markersize=4.0)
axs1.axhline(0,linestyle='--',color='r')
axs1.set_ylabel('Residual (%)\n(y-model)/model')
axs1.set_xlabel('X')
axs1.set_ylim(-90,90)
fig.align_ylabels([axs0,axs1])
fig.savefig('linear_fit.pdf') 

