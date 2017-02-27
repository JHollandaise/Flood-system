"""Unit test for the station module"""

import pytest
from floodsystem.station import *

def test_inconsistent_typical_range_stations():

    # Create stations
    a = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(-2.3, 3.4445),"River 1","Town 1")
    a.latest_level=3.4445

    b = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(5, -2),"River 1","Town 1")
    b.latest_level=2

    c = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),None,"River 1","Town 1")
    c.latest_level=4

    d = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(45, 100),"River 1","Town 1")
    d.latest_level=50

    e = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(6, 0),"River 1","Town 1")
    e.latest_level=2

    test_stations = [a,b,c,d,e]

    assert inconsistent_typical_range_stations\
    (test_stations)==[b,c,e]

    assert a.relative_water_level()==1
    assert b.relative_water_level()==None
    assert c.relative_water_level()==None
    assert d.relative_water_level()==1/11
    assert e.relative_water_level()==None
