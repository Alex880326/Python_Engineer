import os

directory = "D:\GB\Python Enginer\Filectory"

def rename_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # counter = 0
    # for root, dirs, files in os.walk(directory):
    #     for i, file_name in enumerate(files):
    #         new_file_name = f"{file_name}"

    #         file_path = os.path.join(root, file_name)
    #         new_file_path = os.path.join(root, new_file_name)
            
    #         os.rename(file_path, new_file_path)
    #         counter += 1
    #         print(f"Переименовываю {file_path} to {new_file_path}")

    # print(f'Переименовано файлов: {counter}')


    counter = 0 
    for root, dirs, files in os.walk(directory):
        for i, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{i+1}{file_name}"

            file_name = os.path.join(root, file_name)
            new_file_name = os.path.join(root, new_file_name)
                            
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
            counter += 1

            print(f"Переименовываю {file_name} в {new_file_name}")
            print(f'Переименовано файлов: {counter}')
        
        
if __name__ == '__main__':
    rename_files(directory)
