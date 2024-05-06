import os
import json
import csv
import pickle
from CreaThreeFiles import create_file_dict

directory = '/path/to/directory'

def create_file_dict(directory):
    file_dict = {}

    with open('files.json', 'w') as json_file:
        json.dump(file_dict, json_file, indent=4)

    with open('files.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Path', 'Type', 'Size'])
        for path, data in file_dict.items():
            writer.writerow([path, data['type'], data['size']])

    with open('files.pickle', 'wb') as pickle_file:
        pickle.dump(file_dict, pickle_file)


if __name__ == '__main__':
    create_file_dict(directory)
        