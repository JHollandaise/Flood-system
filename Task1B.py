from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():

    stationdists = stations_by_distance(build_station_list(),(52.2053,0.1218))

    print_list=[(stationdist[0].name,stationdist[0].town,stationdist[1]) \
    for stationdist in stationdists]

    print([:10])
    print([-10:])

if __name__=="__main__":

    # Run Task1B
    run()
