from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for task1D"""

    # Build list of stations
    stations = build_station_list()

    # Build set of stations using rivers_wint_station function
    rivers_w_station  = rivers_with_station(stations)

    station_b_river = stations_by_river(stations)


    print(len(rivers_w_station))
    print(sorted(rivers_w_station)[:10])
    print(sorted(station_b_river["River Aire"]))
    print(sorted(station_b_river["River Cam"]))
    print(sorted(station_b_river["Thames"]))


if __name__=="__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1D
    run()
