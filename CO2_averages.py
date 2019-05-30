import os
import numpy as np
import csv
import datetime
import matplotlib.pyplot as plt
import sys
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--plot",action='store_true',default=False)
    args = parser.parse_args()
    arg_dict = vars(args)
    path = 'C:/Users/emily/documents/Co2_calibration'
    #data = pd.read_csv(path)
    #cell_a1 = data.loc[1, 'a']
    x = []
    y = []
    yerr = []
    for filename in os.listdir(path):
        print(filename)
        with open(path+'/'+filename,'r') as f:
            reader = csv.reader(f)
            i = 0
            CO2 = []
            err = []
            for row in reader:
                i = i+1
                if i == 1:
                    continue
                CO2.append(float(row[1]))
                err.append(float(row[2]))
            CO2_avg = np.mean(np.array(CO2))
            err_avg = np.std(np.array(CO2))
            print(CO2_avg)
            print(err_avg)
            x.append(filename)
            y.append(CO2_avg)
            yerr.append(err_avg)
    #x.extend(range(len(y)))
    if arg_dict['plot']:
        plt.plot(x, y)
        plt.errorbar(x, y, yerr)

        plt.xlabel('test')
        plt.ylabel('ppm')

        plt.title('Co2 Averages')

        plt.show()
