from collections import deque

def climb_hill_in_fewest_steps(is_test=True):
    start_pos, end_pos, elevation_grid = convert_to_grid(is_test)
    rows, cols = len(elevation_grid), len(elevation_grid[0])

    # Part 1
    distance_from_S_to_E = find_shortest_distance(start_pos, end_pos, elevation_grid)

    # Part 2
    min_distance_from_a_to_E = float('inf')
    for r in range(rows):
        for c in range(cols):
            if elevation_grid[r][c] == 0:
                distance_from_a_to_E = find_shortest_distance([r, c], end_pos, elevation_grid)
                if distance_from_a_to_E < min_distance_from_a_to_E:
                    min_distance_from_a_to_E = distance_from_a_to_E

    return (distance_from_S_to_E, min_distance_from_a_to_E)
    
def find_shortest_distance(start_pos, end_pos, grid):
    queue = deque([(0, start_pos)])
    seen = set((start_pos[0], start_pos[1]))
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFS
    while queue:
        num_steps, current_pos = queue.popleft()
        if current_pos == end_pos:
            return num_steps

        curr_r, curr_c = current_pos

        for r_inc, c_inc in directions:
            new_r, new_c = curr_r + r_inc, curr_c + c_inc
            if 0 <= new_r < rows and 0 <= new_c < cols \
                and grid[new_r][new_c] <= grid[curr_r][curr_c] + 1 and (new_r, new_c) not in seen:
                seen.add((new_r, new_c))
                queue.append((num_steps + 1, [new_r, new_c]))

    return float('inf')

def convert_to_grid(is_test):
    input_file = "day12_test.txt" if is_test else "day12.txt"
    grid = [list(line) for line in open(input_file, "r").read().splitlines()]
    start_pos, end_pos = [0, 0], [0, 0]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                grid[r][c] = 0
                start_pos = [r, c]
            elif grid[r][c] == "E":
                grid[r][c] = 25
                end_pos = [r, c]
            else:
                grid[r][c] = ord(grid[r][c]) - ord('a')
    return (start_pos, end_pos, grid)

# Part 1 + 2
print(climb_hill_in_fewest_steps(is_test=False))