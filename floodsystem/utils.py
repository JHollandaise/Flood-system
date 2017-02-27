"""This module contains utility functions.

"""

import math

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)



def rad_conv(coord):
    """Converts coordinates from degrees into radians"""
    return (coord[0]*math.pi/180, coord[1]*math.pi/180)

def curve_dist(coord1,coord2,radians=False):
    """uses the haversine formula to calculate the distance between two sets of coordinates"""

    if radians==False:
        coord1 = rad_conv(coord1)
        coord2  =rad_conv(coord2)

    # R equals radius of earth in km
    R = 6371.0088

    return 2*R*math.asin(math.sqrt(math.sin((coord2[0]-coord1[0])/2)**2 + \
    math.cos(coord1[0])*math.cos(coord2[0])*math.sin((coord2[1] - coord1[1])/2)**2))
