import sys
import collections
import os.path
from collections import Counter

# #        if os.path.exists(sys.argv[1]):
#         else:
#             print('Folder path not exist.')
def get_locations(directory):
    if os.path.exists(directory):
        file_locations = collections.defaultdict(list)
        for rootdir, dirs, file_names, in os.walk(directory):
            for file_name in file_names:
                path_to_current_file = os.path.join(rootdir, file_name)
                file_size = os.path.getsize(path_to_current_file)
                file_locations[(file_name, file_size)].append(path_to_current_file)
        return file_locations
    else:
        return None

def get_duplications(all_files):
    return [((file_name, size), paths) for (file_name, size),
            paths in all_files.items() if len(paths) > 1]

# #        if os.path.exists(sys.argv[1]):
#         else:
#             print('Folder path not exist.')
if __name__ == '__main__':
    try:
        if get_locations(sys.argv[1]) is None:
            print('Path not exist.')
        else:
            all_files = get_locations(sys.argv[1])
            duplicated_files = get_duplications(all_files)
            print('\nHello, below files which at least duplicated:')
            print('---------------------------------------------')
            for (file_name, size), paths in duplicated_files:
                print(file_name)
                for path in paths:
                   print('    ', path)
    except IndexError:
        sys.exit('Please, enter the path.')
