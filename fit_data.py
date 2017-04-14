"""
Sample script for fitting sinusoidal data.  This script
uses the data file: sample_AD_data.csv

This data was logged on: 2017-03-08 12:40 pm using an arduino
A/D pin and an associated test circuit.

Author: HMokhtarzadeh
Date: April 13, 2017
"""

import pandas as pd
import numpy as np


#
# Load Data
#
path_data = '/home/hamid/Documents/Work/ONav-Hive/talks/2017-04-13-Python-Environments/sample_AD_data.csv'
df = pd.DataFrame.from_csv(path_data)
df.index = df.index*1e-6 #conver from usec to sec
df.index.names = ["time(sec)"]
print("Data loaded from: {:s}".format(path_data))

#
# Caluculate and report data sampling rate.
#
dt_sec = np.median(np.diff(df.index))
print("Data Sampling rate: {:d} Hz".format(int(1./dt_sec)))

#
# Fit to sinusoid.  
#
# This is method is quite sensative to a good initial guess.
# Alternate approach: http://exnumerus.blogspot.com/2010/04/how-to-fit-sine-wave-example-in-python.html
tmax_sec = .5
def func(x, time, data):
    bias, amp, freq_hz, phase_rad = x

    predict = amp * np.cos(2*np.pi*freq_hz*time + phase_rad)

    return predict - data
from scipy.optimize import leastsq # Other optimizers tried: fmin, minimize, least_squares
x0 = [0.7, 1, 60, 0] # good iniital guess
ind = df.index < tmax_sec
xopt = leastsq(func, x0, args=(df.index[ind], df['amplitude'][ind]))

#
# Save initial guess, fit, and print final fit.
#
bias, amp, freq_hz, phase_rad = x0
df['fit x0'] = bias + amp * np.cos(2*np.pi*freq_hz*df.index + phase_rad)

bias, amp, freq_hz, phase_rad = xopt[0]
df['fit xopt'] = bias + amp * np.cos(2*np.pi*freq_hz*df.index + phase_rad)

print("Fitted Sinusoid: {b:.3f} + {a:.3f}*cos(2 PI {f:.2f} + {p:.3f})".format(b=bias, a=amp, f=freq_hz, p=phase_rad))

#
# Visualize
#
from matplotlib import pyplot as plt
fig, [ax0, ax1] = plt.subplots(2,1)
df['amplitude'][df.index < tmax_sec].plot(ax=ax0, label='raw data', linestyle='', marker='.')
df['fit x0'][df.index < tmax_sec].plot(ax=ax0, alpha=.5, color='black', marker='', lw=2)
df['fit xopt'][df.index < tmax_sec].plot(ax=ax0, color='black', marker='', lw=2)
ax0.legend()
df['amplitude'].plot(ax=ax1)
plt.show()