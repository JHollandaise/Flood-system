"""Unit test for the station module"""

import pytest
from floodsystem.station import *


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():

    # Create stations
    a = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(-2.3, 3.4445),"River 1","Town 1")

    b = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(5, -2),"River 1","Town 1")

    c = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),None,"River 1","Town 1")

    d = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(45, 100),"River 1","Town 1")

    e = MonitoringStation("test-s-id1","test-m-id2","some station1",\
    (-2.0, 4.0),(6, 0),"River 1","Town 1")

    test_stations = [a,b,c,d,e]

    assert inconsistent_typical_range_stations\
    (test_stations)==[b,c,e]
