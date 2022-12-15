# defining constants for visual appeal
EMPTY, ROCK, SAND = "·", "◙", "☼"

# Part 1
def simulate_sand_dropping_no_floor(is_test):
    min_x, cave_grid = build_cave_grid(is_test=is_test)
    sand_particles_at_rest = 0
    while True:
        init_sand_pos = normalize_position((500, 0), min_x)
        # drop sand particle and check if's fallen to the abyss
        if not drop_sand_particle(init_sand_pos, cave_grid):
            break
        sand_particles_at_rest += 1
    
    # for curiosity of what the cave looks like
    print_cave_state(cave_grid)
    return sand_particles_at_rest

# Part 2
def simulate_sand_dropping_with_floor(is_test):
    min_x, cave_grid = build_cave_grid(is_test=is_test, is_floor=True, tolerance=150)
    sand_particles_at_rest = 0
    while True:
        init_sand_pos = normalize_position((500, 0), min_x)
        sand_particles_at_rest += 1
        # drop sand particle and check if's fallen to the abyss
        if not drop_sand_particle(init_sand_pos, cave_grid, is_floor=True):
            break
    
    # for curiosity of what the cave looks like
    print_cave_state(cave_grid)
    return sand_particles_at_rest

def drop_sand_particle(particle_pos, cave_grid, is_floor=False):
    rows, cols = len(cave_grid), len(cave_grid[0])
    init_sand_pos = particle_pos
    sand_at_rest = False
    while not sand_at_rest:
        r, c = particle_pos
        # if our particle is about to fall into the abyss with no floor
        if not is_floor and (c == 0 or c == cols - 1 or r == rows - 1):
            return False
        # check if it can fall directly one step down
        elif cave_grid[r + 1][c] == EMPTY:
            particle_pos = (r + 1, c)
        # check if it can fall diagonally left
        elif cave_grid[r + 1][c - 1] == EMPTY:
            particle_pos = (r + 1, c - 1)
        # check if it can fall diagonally right
        elif cave_grid[r + 1][c + 1] == EMPTY:
            particle_pos = (r + 1, c + 1)
        else:
            cave_grid[r][c] = SAND
            sand_at_rest = True
            # if sand has stacked up all the way to the opening
            if is_floor and init_sand_pos == (r, c):
                return False
    return True

def build_cave_grid(is_test, is_floor=False, tolerance=0):
    rock_wall_positions, min_x, max_x, max_y = get_rock_positions(is_test)

    # Part 2, infinite floor underneath
    if is_floor:
        min_x, max_x, max_y = min_x - tolerance, max_x + tolerance, max_y + 2

    cave_grid = [[EMPTY for _ in range(max_x - min_x + 3)] for _ in range(max_y + 1)]

    for wall in rock_wall_positions:
        for i in range(len(wall) - 1):
            src, dst = wall[i], wall[i + 1]
            draw_wall(src, dst, min_x, cave_grid)

    # Part 2, draw infinite floor underneath
    if is_floor:
        draw_wall((min_x, max_y), (max_x, max_y), min_x, cave_grid)

    return min_x, cave_grid

def print_cave_state(cave_grid):
    for line in cave_grid:
        print("".join(line))

def draw_wall(src, dst, min_x, cave_grid):
    r1, c1 = normalize_position(src, min_x)
    r2, c2 = normalize_position(dst, min_x)
    if r1 == r2:
        for c in range(min(c1, c2), max(c1, c2) + 1):
            cave_grid[r1][c] = ROCK
    elif c1 == c2:
        for r in range(min(r1, r2), max(r1, r2) + 1):
            cave_grid[r][c1] = ROCK

def normalize_position(pos, min_x):
    return (pos[1], pos[0] - min_x + 1)

def get_rock_positions(is_test):
    input_file = "day14_test.txt" if is_test else "day14.txt"
    rock_wall_positions = [line.split(" -> ") for line in open(input_file, "r").read().splitlines()]
    min_x, max_x = float('inf'), float('-inf')
    max_y = float('-inf')

    for wall in rock_wall_positions:
        for i in range(len(wall)):
            x, y = wall[i].split(",")
            wall[i] = (int(x), int(y))
            min_x, max_x = min(min_x, int(x)), max(max_x, int(x))
            max_y = max(max_y, int(y))

    return (rock_wall_positions, min_x, max_x, max_y)

# Part 1
print(simulate_sand_dropping_no_floor(is_test=False))

# Part 2
print(simulate_sand_dropping_with_floor(is_test=False))