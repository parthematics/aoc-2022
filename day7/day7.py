class Directory:
    def __init__(self, name, parent_directory=None):
        self.name = name
        self.child_directories = {} # mapping from child dir name to child dir
        self.files = [] # list of tuples (filename, file_size)
        self.parent_directory = parent_directory # for root directory, this will be none

    def __str__(self):
        return f"{self.name}+{self.parent_directory}"

# Part 1
def find_all_directories_under_size(size_threshold):
    root_dir = create_directory_structure()
    directory_to_size_map = {}
    total_size_sum = 0

    # recursively determine sizes of all directories contained within root
    find_sizes_of_directories(root_dir, directory_to_size_map)

    for size in directory_to_size_map.values():
        if size <= size_threshold:
            total_size_sum += size
    
    return total_size_sum

# Part 2
def find_smallest_directory_to_delete(unused_space_required, total_disk_space):
    root_dir = create_directory_structure()
    directory_to_size_map = {}
    # recursively determine sizes of all directories contained within root
    find_sizes_of_directories(root_dir, directory_to_size_map)

    sorted_sizes = sorted(directory_to_size_map.values())
    total_space_used = sorted_sizes[-1]
    current_unused_space = total_disk_space - total_space_used

    for size in sorted_sizes:
        if size >= unused_space_required - current_unused_space:
            return size

def create_directory_structure():
    lines = open("day7.txt", 'r').readlines()
    root_dir = Directory("/")
    curr_dir = root_dir

    for line in lines:
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                changed_dir = tokens[2]
                if changed_dir == "/":
                    curr_dir = root_dir
                elif changed_dir == "..":
                    curr_dir = curr_dir.parent_directory
                else:
                    curr_dir = curr_dir.child_directories[changed_dir]
            # ls command, doesn't really do much
            else:
                continue
        # log this as an existing directory within curr directory
        elif tokens[0] == "dir":
            child_directory = tokens[1]
            # store child directory in parent directory if we haven't already added it
            if child_directory not in curr_dir.child_directories:
                curr_dir.child_directories[child_directory] = Directory(child_directory, curr_dir)
        # otherwise, we're seeing a file in the current directory, log it within the files arr
        else:
            file_name, file_size = tokens[1], int(tokens[0])
            curr_dir.files.append((file_name, file_size))

    return root_dir

def find_sizes_of_directories(curr_directory, directory_to_size_map):
    curr_size = 0

    for _, size in curr_directory.files:
        curr_size += size

    for child_dir in curr_directory.child_directories:
        child_directory = curr_directory.child_directories[child_dir]
        curr_size += find_sizes_of_directories(child_directory, directory_to_size_map)

    directory_to_size_map[str(curr_directory)] = curr_size
    return curr_size

print(find_all_directories_under_size(100000))
print(find_smallest_directory_to_delete(30000000, 70000000))