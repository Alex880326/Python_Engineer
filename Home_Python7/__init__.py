import os

from Creator import generate_files
from Extentioner import generate_with_dictionary
from Sorter import sort_files
from Renamer import rename_files

directory = "D:\GB\Python Enginer\Filectory"
d = {
        'doc': 5,
        'jpg': 10,
        'png': 23,
        'txt': 15,
    }

if __name__ == '__main__':
    generate_files('rnd', 'Filectory')
    generate_with_dictionary(d)
    sort_files('Filectory')
    rename_files(directory)

