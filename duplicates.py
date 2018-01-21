import os
import sys
import collections
import os.path
from collections import Counter


def get_locations(directory):
    file_locations = collections.defaultdict(list)
    for rootdir, dirs, file_names, in os.walk(directory):
        for file_name in file_names:
            path_to_current_file = os.path.join(rootdir, file_name)
            file_size = os.path.getsize(path_to_current_file)
            file_locations[(file_name, file_size)].append(path_to_current_file)
    return file_locations


def get_duplications(all_files):
    duplications = []
    for (file_name, size), paths in all_files.items():
        if len(paths) > 1:
            duplications.append((file_name, size, paths))

    return duplications


if __name__ == '__main__':
    try:
        if os.path.exists(sys.argv[1]):
            folder_path = sys.argv[1]
            all_files = get_locations(folder_path)
            duplicated_files = get_duplications(all_files)
            print('---------------------------------------------')
            print('Hello, below files which at least duplicated:')
            print('---------------------------------------------')
            for file_name, size, paths in duplicated_files:
                print(file_name)
                for path in paths:
                    print('    ', path)
        else:
            print('Folder path not exist.')
    except IndexError:
        sys.exit('Please, enter correct path.')
