import os
import numpy as np
import modules.writer as w

path = r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data\0'
path2 = r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data\3'

i = 1
files = ['pendulumODE(0.2)2.csv',
         'pendulumODE(0.201)2.csv']
for dataset in os.listdir(path):
    if dataset in files:
        print(f'file {i}/{len(os.listdir(path))}')
        data = np.genfromtxt(open(os.path.join(path, dataset), 'rb'), 
                        delimiter=" ", 
                        names=True,
                        dtype=np.float64)

        headers = data.dtype.names
        data = np.array([data[headers[0]], data[headers[1]]]).T

        dump = 0 # %
        rows_to_dump = int(data.shape[0]*dump / 100)
        data = w.dump(data, rows_to_dump)

        remaining_data = 30 # %
        data_to_keep = int((data.shape[0] - 1)*remaining_data / 100)
        data = w.optimize(data, int((data.shape[0] - 1) / data_to_keep))

        name = os.path.splitext(dataset)[0]
        w.write(data, header=headers, name=name, path=path2)

    i += 1