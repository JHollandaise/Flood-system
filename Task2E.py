from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    stations = build_station_list()
    dt = 2
    dates, levels = fetch_measure_levels(stations[0].measure_id,\
        dt=datetime.timedelta(days=dt))

    plot_water_levels(stations[0],dates,levels)

if __name__=="__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    # Run Task2E
    run()
