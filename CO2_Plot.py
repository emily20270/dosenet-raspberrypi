import csv
import datetime
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print('Please provide input file :)')
    exit

filename = str(sys.argv[1])


with open(filename) as csvfile:
    file = csv.reader(csvfile, delimiter=',')

    x = []
    y = []
    yerr = []

    for row in file:

        print(row)
        try:
            x.append(float(row[0]))
            y.append(float(row[1]))
            yerr.append(float(row[2]))
        except Exception as e:
            print(e)
            pass
    plt.plot(x, y)
    plt.errorbar(x, y, yerr)

    plt.xlabel('time')
    plt.ylabel('ppm')
    
    plt.title(filename)

    plt.show()
