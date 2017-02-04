from floodsystem.stationdata import *
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task2C"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for e in stations_highest_rel_level(stations,10):
        print("{} {}".format(e.name,e.relative_water_level()))

if __name__=="__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    # Run Task2C
    run()
