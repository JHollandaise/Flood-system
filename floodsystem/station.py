"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        # Coordinates are in form (latitude, longitude)
        self.coord = coord

        # Typical range in the form (low,high)
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Returns True if typical range data consistent for object.
        False for insconsistent or unavailable data
        """

        if self.typical_range==None:
            return False
        elif self.typical_range[0]-self.typical_range[1]>0:
            return False

        return True


    def relative_water_level(self):
        """Returns a ratio of latest water level compared to typical ranges
        where 1 => max of typical range
              0 => min of typical range
        """

        if not self.typical_range_consistent():
            return None

        try:
             return (self.latest_level-self.typical_range[0])/\
             (self.typical_range[1]-self.typical_range[0])

        except:
            return None


def inconsistent_typical_range_stations(stations):
        """Returns a list of stations whose typical range data is inconsistent"""

        return [station for station in stations\
        if not station.typical_range_consistent()]