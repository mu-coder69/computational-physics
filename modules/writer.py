import csv
from os.path import splitext
from numpy import concatenate

def write(datax, datay, path=__file__):
    header = ['x', 'y']
    data = concatenate([datax, datay], axis=1)
    with open(splitext(path)[0] + '.csv', 
              mode='w', 
              encoding='UTF8',
              newline='') as f:
        print("Writing file...")
        writer = csv.writer(f, delimiter=" ")
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(data)

        print("File created succesfully!")
