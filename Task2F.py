from floodsystem.stationdata import *
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt

def run():

    # Build stations
    stations = build_station_list()

    # Update station data
    update_water_levels(stations)

    # Get top 5 stations
    top_5_stations = stations_highest_rel_level(stations,5)


    # Gather level data for rivers
    all_dates = []
    all_levels = []
    dt = 10

    for station in top_5_stations:
        dates, levels = fetch_measure_levels(station.measure_id,\
        dt=datetime.timedelta(days=dt))

        all_dates.append(dates)
        all_levels.append(levels)

    plot_water_level_with_fit(top_5_stations,all_dates,all_levels,10)
    plt.show()

if __name__=="__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    # Run Task2E
    run()
