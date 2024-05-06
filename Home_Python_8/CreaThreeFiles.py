import os

directory = '/path/to/directory'

def create_file_dict(directory):
    file_dict = {}

    for root, dirs, files in os.walk(directory):
        dir_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        for file in files:
            file_path = os.path.join(root, file)
            file_dict[file_path] = {
                'type': 'file',
                'size': os.path.getsize(file_path)
            }
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = 0
            for dir_root, _, dir_files in os.walk(dir_path):
                dir_size += sum(os.path.getsize(os.path.join(dir_root, name)) for name in dir_files)
            file_dict[dir_path] = {
                'type': 'directory',
                'size': dir_size
            }
      
       
if __name__ == '__main__':
    create_file_dict(directory)
