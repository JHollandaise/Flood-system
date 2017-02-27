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

    return sorted_by_key([(station,curve_dist(p,station.coord)) for station in stations],1)

def stations_within_radius(stations, centre, r):
    """Returns all stations from given list of stations within
    radius r(km) of point centre(lat,long)."""

    return [station for station in stations if curve_dist(station.coord,centre)<r]

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
    """Returns a list of the N rivers with the
    greatest number of monitoring stations"""

    stations_b_r = stations_by_river(stations)


    number_of_stations = sorted_by_key([(river,len(stations)) for river, stations in stations_b_r.items()],1,True)

    print_nos = number_of_stations[:N]
    i = N+1
    while True:
        if print_nos[-1][1] == number_of_stations[i][1]:
            print_nos.append(number_of_stations[i])
            i+=1
        else:
            break

    return print_nos
