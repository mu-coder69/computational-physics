import csv
from os.path import dirname, join

def write(datax, datay, path, name='data'):
    header = ['x', 'y']
    data = [datax, datay]

    with open(join(dirname(path), f'{name}.csv'), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        
        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
