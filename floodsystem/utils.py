"""This module contains utility functions.

"""


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

import math

def conv_to_rads(coord):
    """Converts coordinates from degrees into radians"""
    return (coord[0]*math.pi/180,coord[1]*math.pi/180)

def curve_dist(c1,c2,radians=False):
    """Returns the distance (km) between two coordinates
    along a great circle of a sphere
    """

    if not radians:
        c1 = conv_to_rads(c1)
        c2 = conv_to_rads(c2)

    # Radius of Earth (km)
    r = 6371

    return 2*r*math.asin(( math.sqrt(math.sin((c1[0]-c2[0])/2)**2 + \
    math.cos(c1[0])*math.cos(c2[0])*math.sin((c1[1]-c2[1])/2)**2) ))
