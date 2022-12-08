# Part 1
def find_number_of_visible_trees(input_file="day8_test.txt"):
    lines = open(input_file, 'r').read().splitlines()
    tree_grid = make_tree_grid(lines)
    rows, cols = len(tree_grid), len(tree_grid[0])
    num_visible_trees = 0

    for r in range(rows):
        for c in range(cols):
            if is_visible(tree_grid, r, c):
                num_visible_trees += 1

    return num_visible_trees

# Part 2
def find_maximum_scenic_score(input_file="day8_test.txt"):
    lines = open(input_file, 'r').read().splitlines()
    tree_grid = make_tree_grid(lines)
    rows, cols = len(tree_grid), len(tree_grid[0])
    max_scenic_score = float('-inf')

    for r in range(rows):
        for c in range(cols):
            curr_scenic_score = determine_scenic_score(tree_grid, r, c)
            if curr_scenic_score > max_scenic_score:
                max_scenic_score = curr_scenic_score

    return max_scenic_score

def determine_scenic_score(grid, r, c):
    left_dist, right_dist, top_dist, bottom_dist = 0, 0, 0, 0
    # Check left
    for col in range(c - 1, -1, -1):
        left_dist += 1
        if grid[r][col] >= grid[r][c]:
            break
    # Check right
    for col in range(c + 1, len(grid[0])):
        right_dist += 1
        if grid[r][col] >= grid[r][c]:
            break
    # Check top
    for row in range(r - 1, -1, -1):
        top_dist += 1
        if grid[row][c] >= grid[r][c]:
            break
    # Check bottom
    for row in range(r + 1, len(grid)):
        bottom_dist += 1
        if grid[row][c] >= grid[r][c]:
            break

    return (left_dist * right_dist * top_dist * bottom_dist)

def is_visible(grid, r, c):
    # trees on edge of grid
    if r == len(grid) - 1 or r == 0 or c == len(grid[0]) - 1 or c == 0:
        return True
    # check trees in all 4 directions
    return is_visible_horizontally(grid, r, c) or is_visible_vertically(grid, r, c)

def is_visible_horizontally(grid, r, c):   
    def visible_left():
        for col in range(0, c):
            if grid[r][col] >= grid[r][c]:
                return False
        return True

    def visible_right():
        for col in range(c + 1, len(grid[0])):
            if grid[r][col] >= grid[r][c]:
                return False
        return True
    
    return visible_left() or visible_right()

def is_visible_vertically(grid, r, c):
    def visible_top():
        for row in range(0, r):
            if grid[row][c] >= grid[r][c]:
                return False
        return True

    def visible_bottom():
        for row in range(r + 1, len(grid)):
            if grid[row][c] >= grid[r][c]:
                return False
        return True
    
    return visible_top() or visible_bottom()

def make_tree_grid(lines):
    grid = []
    for line in lines:
        grid.append([int(i) for i in list(line)])
    return grid

# Test input
print(find_number_of_visible_trees())
print(find_maximum_scenic_score())

# Main input
print(find_number_of_visible_trees("day8.txt"))
print(find_maximum_scenic_score("day8.txt"))