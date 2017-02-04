"""Unit test for the geo module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.geo import *

# Create a global list of test stations
a = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(0.0,0.0),(-2.3, 3.4445),"River 1","Town 1")

b = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-1.0,0.0),(5, -2),"River 742","Town 1")

c = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(43.0,20),None,"River fhu","Town 1")

d = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(100.654654, 100.6541),(45, 100),"65464","Town 1")

e = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-2.0, -1.0),(6, 0),"65464","Town 1")

test_stations = [a,b,c,d,e]

def test_stations_by_distance():

    test_res = stations_by_distance(test_stations,(0.0,0.0))

    assert [i[0] for i in test_res] == [a,b,e,c,d]

def test_stations_within_radius():


    test_res = stations_within_radius(test_stations,(0.0,0.0),1000)

    assert test_res == [a,b,e]

def test_rivers_with_station():

    test_res = rivers_with_station(test_stations)

    assert test_res == set([a.river,b.river,c.river,d.river])

def test_stations_by_river():

    test_res = stations_by_river(test_stations)

    assert test_res == {a.river:[a.name],b.river:[b.name],\
    c.river:[c.name],d.river:[d.name,e.name]}

def test_rivers_by_station_number():

    test_res = rivers_by_station_number(test_stations,1)
    assert test_res == [(d.river,2)]

    ###### I would do another test for this function but the results for
    ###### multiple rivers with same number of stations can be unpredictable
