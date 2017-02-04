from floodsystem.stationdata import *
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task2B"""

    stations = build_station_list()
    update_water_levels(stations)

    for e in stations_level_over_threshold(stations,0.8):
        print("{} {}".format(e[0].name,e[1]))

if __name__=="__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    # Run Task2B
    run()
