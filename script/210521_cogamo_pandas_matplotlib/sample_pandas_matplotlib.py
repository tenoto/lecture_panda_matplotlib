#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('data/210521_cogamo/37_20210521_20210522.csv')
#print(df)
#print(df.columns.tolist())
#print(df['time'])
#print(type(df['time']))

df['time'] = pd.to_datetime(df['time'])
#print(df['time'])
#print(df['time']+pd.DateOffset(1))

"""
fig = plt.figure(figsize=(10,4),tight_layout=True)
plt.plot(df['time'],df['pressure'],'o-',markersize=4.0,label='pressure')
plt.legend(loc='lower left')
plt.xlabel('Date')
plt.ylabel('Pressure (hPa)')
fig.savefig('curve.pdf')
"""

fig, axs = plt.subplots(2,1, figsize=(10,8),
	sharex=True, gridspec_kw={'hspace': 0})
axs[0].plot(df['time'],df['pressure'],'o-',markersize=4.0,label='pressure')
axs[0].set_ylabel('Pressure (hPa)')
axs[1].plot(df['time'],df['temp'],'o-',markersize=4.0)
axs[1].set_ylabel('Temperature (C)')
axs[1].set_xlabel('Date')
#axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d\n%H:%M:%S"))
axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%m/%d\n%H:%M"))
fig.align_ylabels(axs)
fig.savefig('curve.pdf')