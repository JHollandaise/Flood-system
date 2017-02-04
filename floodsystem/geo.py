"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from .utils import curve_dist

def stations_by_distance(stations, p):
    """Returns a sorted list of tuples of (station, distance) where
    distance(float) is the distance of station from coordinate p.

    List is sorted by increasing distance.
    """

    return sorted_by_key([(station,curve_dist(station.coord,p)) for station \
    in stations],1)


def stations_within_radius(stations, centre, r):
    """Returns all stations from given list of stations within
    radius r(km) of point centre(lat,long)."""

    return [station for station in stations\
    if curve_dist(station.coord,centre)<r]

def rivers_with_station(stations):
    """Returns a set of names of rivers with a station
    from list stations"""

    return set([station.river for station in stations])

def stations_by_river(stations):
    """Returns a dict of river names mapped to list of
    stations on that river"""

    rivers = {}

    for station in stations:
        if station.river in rivers:
            rivers[station.river].append(station.name)
        else:
            rivers[station.river] = [station.name]

    return rivers

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of stations (if there
    are more rivers with the same number of stations as the Nth station, these
    will be included in the result)
    Returns a sorted list of ('river name',number of stations) tuples
    """

    rivers = stations_by_river(stations)

    rivers_by_num = sorted_by_key([(river,len(rivers[river]))\
    for river in rivers],1,True)

    n_rivers_by_num = []

    for e in rivers_by_num:
        if len(n_rivers_by_num)>=N and e[1]!=n_rivers_by_num[-1][1]:
            break
        n_rivers_by_num.append(e)

    return n_rivers_by_num
