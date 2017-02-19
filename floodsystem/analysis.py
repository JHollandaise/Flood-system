import numpy as np
import matplotlib as mpl

def polyfit(dates, levels, p):

    d0  = mpl.dates.date2num(dates[-1])

    x = np.array(mpl.dates.date2num(dates)) - d0
    y = levels

    p_coeff = np.polyfit(x, y, p)

    poly = np.poly1d(p_coeff)

    return poly, d0
