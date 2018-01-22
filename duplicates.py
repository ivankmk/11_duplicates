import sys
import collections
import os.path
from collections import Counter


def get_file_locations(directory):
    file_locations = collections.defaultdict(list)
    for rootdir, dirs, file_names, in os.walk(directory):
        for file_name in file_names:
            path_to_current_file = os.path.join(rootdir, file_name)
            file_size = os.path.getsize(path_to_current_file)
            file_locations[(file_name,
                            file_size)].append(path_to_current_file)
    return file_locations


def get_duplications(all_files):
    return [((file_name, size), paths) for (file_name, size),
            paths in all_files.items() if len(paths) > 1]

def check_path(directory):
    if os.path.exists(directory):
        return directory
    else:
        return None

if __name__ == '__main__':
    try:
        path = check_path(sys.argv[1])
        duplicated_files = get_duplications(get_file_locations(path))
        print('\nHello, below files which at least duplicated:')
        print('---------------------------------------------')
        for (file_name, size), paths in duplicated_files:
            print(file_name)
            for path in paths:
                print('   ', path)
    except IndexError:
        sys.exit('Please, enter the path.')
    except NameError:
        sys.exit('Please use correct filepath.')
