from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    stations = build_station_list()

    stations_by_dist = stations_by_distance(stations,(52.2053,0.1218))

    printlist = [(item[0].name,item[0].town,item[1]) for item in stations_by_dist]


    print(printlist[:10])
    print(printlist[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IB Flood Warning System ***")

    # Run Task1B
    run()
