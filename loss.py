# import numpy as np
import pylab as pl

f = open('Bi227', 'r')

data = []
dataX = []
dataY = []

for line in f.readlines():
    if len(line) > 1:
        row = line.split()
        if row[0][0].isnumeric() or row[0][0]=='-' or row[0][0]=='+':
            dataRow = [float(row[0].replace(',','.')), float(row[1].replace(',','.'))]
            data.append(dataRow)
            print(dataRow[0], dataRow[1])

for item in data:
    dataX.append(item[0])
    dataY.append(item[1])

pl.plot(dataX, dataY)

pl.xlabel('Wavelength (nm)')
pl.ylabel('Loss (dB/m)')
pl.title('Loss spectrum of the Bi227 fiber')

pl.xlim(1200, 1700)
pl.ylim(0, 4)

pl.show()