"""This module provides functions relating to the risk of
flooding for rivers using latest lavel data.
"""

from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples (station,relative water level)
    sorted in descending water level for stations with relative
    water levels above the tolerance tol.
    """

    return sorted_by_key([(station,station.relative_water_level())\
    for station in stations if station.relative_water_level()\
    and station.relative_water_level()>tol],1,True)

def stations_highest_rel_level(stations, N):
    """Returns the N stations, sorted in descending order, with the highest
    relative water level
    """

    return sorted([station for station in stations],\
    key=lambda element: element.relative_water_level()\
    if element.relative_water_level() else -100,reverse=True)[:N]
