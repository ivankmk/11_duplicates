import os
import sys
from collections import Counter


def get_list_of_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):

        if '/.' not in root:
            for file_data in files:
                path = os.path.join(root, file_data)
                if '/.' not in path:
                    size = os.stat(path).st_size
                    all_files.append((path.split('/')[-1], size))
    return all_files


def get_duplications(files):
    duplicated_files = []
    files_with_counter = Counter(files)
    for name_size, count in files_with_counter.items():
        if count > 1:
            duplicated_files.append((name_size[0], name_size[1], count))
    return duplicated_files

if __name__ == '__main__':
    try:
        files_in_path = get_list_of_files(sys.argv[1])
    except IndexError:
        sys.exit('Please, enter correct path.')
    duplicated_result = get_duplications(files_in_path)
    print('Hello, below files which at least duplicated:')
    print('-'*40)
    for filename, _, count in duplicated_result:
        print(filename, ': ', count)
    print('-'*40)
