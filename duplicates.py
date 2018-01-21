import sys
import collections
import os.path
from collections import Counter


def get_locations(directory):
    if os.path.exists(directory):
        file_locations = collections.defaultdict(list)
        for rootdir, dirs, file_names, in os.walk(directory):
            for file_name in file_names:
                path_to_current_file = os.path.join(rootdir, file_name)
                file_size = os.path.getsize(path_to_current_file)
                file_locations[(file_name,
                                file_size)].append(path_to_current_file)
        return file_locations
    else:
        return None


def get_duplications(all_files):
    return [((file_name, size), paths) for (file_name, size),
            paths in all_files.items() if len(paths) > 1]


if __name__ == '__main__':
    try:
        duplicated_files = get_duplications(get_locations(sys.argv[1]))
        print('\nHello, below files which at least duplicated:')
        print('---------------------------------------------')
        for (file_name, size), paths in duplicated_files:
            print(file_name, paths)
    except IndexError:
        sys.exit('Please, enter the path.')
    except AttributeError:
        sys.exit('Filepath is not correct.')
