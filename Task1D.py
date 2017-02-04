from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for task1D"""

    stations = build_station_list()

    rivers_w_station = rivers_with_station(stations)
    stations_by_rivers = stations_by_river(stations)


    print("Number of rivers with station(s): {}".format(len(rivers_w_station)) )
    print("First 10 rivers with stations:\n",sorted(rivers_w_station)[:10],"\n")

    print("Stations by 'River Aire':\n",sorted(stations_by_rivers['River Aire'],),"\n")
    print("Stations by 'River Cam':\n",sorted(stations_by_rivers['River Cam'],),"\n")
    print("Stations by 'Thames':\n",sorted(stations_by_rivers['Thames'],),"\n")



if __name__=="__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1D
    run()
