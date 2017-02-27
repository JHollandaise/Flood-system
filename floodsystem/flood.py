"""This module contains a collection of functions related to
flood data.

"""


from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of stations with a relative
    water level higher than a tolerance value"""

    stations_lot=[]

    for station in stations:
        if station.relative_water_level()==None:
            continue

        elif station.relative_water_level()>tol:
            stations_lot.append((station,station.relative_water_level()))



    return sorted_by_key(stations_lot,1,True)

def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations with the
    greatest relative water level"""

    stations_hrl=[]

    for station in stations:
        if station.relative_water_level()==None:
            continue

        else:
            stations_hrl.append(station)



    highest_relative_level=sorted(stations_hrl,key=lambda element:\
    element.relative_water_level() if element.relative_water_level()\
    else -100,reverse=True)

    print_hrl=highest_relative_level[:N]

    return print_hrl
