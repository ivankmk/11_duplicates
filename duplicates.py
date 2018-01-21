import os
import sys
import collections
from collections import Counter


def get_files(directory):
    file_locations = collections.defaultdict(list)
    for rootdir, dirs, file_names, in os.walk(directory):
        for file_name in file_names:
            path_to_current_file = os.path.join(rootdir, file_name)
            file_size = os.path.getsize(path_to_current_file)
            file_locations[(file_name, file_size)].append(path_to_current_file)
    return file_locations


def get_duplications(all_files):
    duplications = []
    for file_name_and_size, paths in all_files.items():
        if len(paths) > 1:
            duplications.append(file_name_and_size)
    return duplications


if __name__ == '__main__':
    try:
        all_files = get_files(sys.argv[1])
        duplicated_files = get_duplications(all_files)
        print('---------------------------------------------')
        print('Hello, below files which at least duplicated:')
        print('---------------------------------------------')
        for file_name in duplicated_files:
            print(file_name[0])
            for path in all_files[file_name]:
                print('  ..', path)
    except IndexError:
        sys.exit('Please, enter correct path.')
