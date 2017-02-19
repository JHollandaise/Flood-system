import matplotlib.pyplot as plt
import matplotlib as mpl

from .analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Plots water levels for given station list, dates and levels lists
    """

    if not len(station)==len(dates)==len(levels):
        print("Invalid entry to plot_water_levels function")
        print("variables of different lengths")
        print("{} {} {}".format(len(station),len(dates),len(levels)))
        return None

    for i in range(len(station)):
        if not len(dates[i])==len(levels[i]):
            print(station[i].name,"has incorrect dates/levels data")
            print("date_len",len(dates[i]),"levels_len",len(levels[i]))
            to_del = i

    del station[to_del]
    del dates[to_del]
    del levels[to_del]


    for i in range(len(station)):

        # Set figure for station
        plt.figure(i+1)

        # Plot
        plt.plot(dates[i], levels[i],label="Water level")

        # Plot typical ranges
        plt.plot(dates[i],[station[i].typical_range[0] for j in range(len(dates[i]))],label="Typical range: Low")
        plt.plot(dates[i],[station[i].typical_range[1] for j in range(len(dates[i]))],label="Typical range: High")

        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station[i].name)
        plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots water levels for given station list, dates and levels lists
    and also a least squares fit.
    """

    if not len(station)==len(dates)==len(levels):
        print("Invalid entry to plot_water_levels function")
        print("variables of different lengths")
        print("{} {} {}".format(len(station),len(dates),len(levels)))
        return None

    to_del = 0
    for i in range(len(station)):
        print("date_len",len(dates[i]),"levels_len",len(levels[i]))
        if not len(dates[i])==len(levels[i]):
            print(station[i].name,"has incorrect dates/levels data")
            print("date_len",len(dates[i]),"levels_len",len(levels[i]))
            to_del = i

    if to_del:
        del station[to_del]
        del dates[to_del]
        del levels[to_del]

    for i in range(len(station)):

        # Gather polydata
        poly, d0 = polyfit(dates[i],levels[i],p)

        poly_y = [poly(mpl.dates.date2num(dates[i][n])-d0) for n in range(len(dates[i]))]

        # Set figure for station
        plt.figure(i+1)

        # Plot raw data
        plt.plot(dates[i], levels[i],label="Water level")

        # Plot polyfit data
        plt.plot(dates[i], poly_y)


        # Plot typical ranges
        plt.plot(dates[i],[station[i].typical_range[0] for j in range(len(dates[i]))],label="Typical range: Low")
        plt.plot(dates[i],[station[i].typical_range[1] for j in range(len(dates[i]))],label="Typical range: High")

        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station[i].name)
        plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
