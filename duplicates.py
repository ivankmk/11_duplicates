import sys
import collections
import os.path


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


def print_duplications(duplicated_files):
    print('\nHello, below files which at least duplicated:')
    print('---------------------------------------------')
    for (file_name, size), paths in duplicated_files:
        print(file_name)
        for path in paths:
            print('   ', path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Please, enter the path.')
    path = sys.argv[1]
    if not os.path.exists(path):
        sys.exit('Please, enter the correct path.')
    duplicated_files = get_duplications(get_file_locations(sys.argv[1]))
    print_duplications(duplicated_files)
