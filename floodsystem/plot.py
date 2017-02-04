import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """Plots water levels for given station, dates and levels lists
    """

    if not len(station)==len(dates)==len(levels):
        print("Invalid entry to plot_water_levels function")
        print("variables of different lengths")
        print("{} {} {}".format(len(station),len(dates),len(levels)))
        return None

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

    return None
