"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'pictures',
    'png': 'pictures',
}

def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = f'{directory}/{DICTIONARY[extension]}'
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.mkdir(new_directory)
        os.rename(f'{directory}/{f}',
                  f'{new_directory}/{f}')


if __name__ == '__main__':
    sort_files('Filectory')