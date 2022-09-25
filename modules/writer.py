import csv
import inspect
from numpy import concatenate
from os.path import splitext

def write(data: list, 
          header: list=None, 
          split=False, 
          keep=0, 
          path="default") -> None:

    if path == "default":
        previous_frame = inspect.currentframe().f_back
        path = inspect.getframeinfo(previous_frame)[0]

    if not split:     
        print("Writing file...")
        with open(splitext(path)[0] + '.csv', 
                mode='w', 
                encoding='UTF8',
                newline='') as f:
            writer = csv.writer(f, delimiter=" ")
            #write header
            if header is not None:
                writer.writerow(header)
            # write selected data
            writer.writerows(data)
    else:
        n_columns = data.shape[1]
        #get the column to keep
        column_to_keep = data[:, keep].reshape((-1, 1))
        print("Writing file...")
        for i in range(n_columns):
            if i != keep:
                with open(splitext(path)[0] + f'{i}.csv', 
                        mode='w', 
                        encoding='UTF8',
                        newline='') as f:

                    print(f'printing column {i}')
                    writer = csv.writer(f, delimiter=" ")
                    #write header
                    if header is not None:
                        writer.writerow([header[keep], header[i]])
                    #split data
                    new_data = data[:, i].reshape((-1, 1))
                    temp_data = concatenate((column_to_keep, new_data), axis=1)
                    # write selected data
                    writer.writerows(temp_data)

    print("File created succesfully!")

def optimize(data: list, keep_each=2) -> list:
    return data[0::keep_each]