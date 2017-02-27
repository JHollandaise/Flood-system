import numpy as np
import matplotlib as mpl

def polyfit(dates, levels, p):

    d0  = mpl.dates.date2num(dates[0])
    x = np.array(mpl.dates.date2num(dates)) - d0
    y = levels

    p_coeff = np.polyfit(x, y, p)

    poly = np.poly1d(p_coeff)

    return poly, d0

def flood_warn(stations):
    for station in stations:
        if station.relative_water_level() >= 10 or station.relative_water_level() <=-10:
            continue
        elif station.relative_water_level() >= 2.5:
            station.warning_level = 4
        elif station.relative_water_level() >= 2.1:
            station.warning_level = 3
        elif station.relative_water_level() >= 1.7:
            station.warning_level = 2
        elif station.relative_water_level() >= 1.3:
            station.warning_level = 1
        else:
            station.warning_level = 0


    return stations
