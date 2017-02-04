from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for task1C"""

    # Build list of stations
    stations = build_station_list()

    # Create list of all stations within 10km of Cambridge city centre
    stations_in_rad = stations_within_radius(stations,(52.2053,0.1218),10)

    print(sorted([station.name for station in stations_in_rad]))

if __name__=="__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Run Task1C
    run()
