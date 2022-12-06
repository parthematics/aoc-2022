from re import match
from collections import deque

def decode_move(move):
    num_crates = int(move.split(" from ")[0].split()[1])
    src_and_dst = move.split(" from ")[1].split(" to ")
    from_, to_ = int(src_and_dst[0]), int(src_and_dst[1])
    return (num_crates, (from_, to_))

def create_stacks(stack_layers, num_stacks):
    stack = {i : deque([]) for i in range(1, num_stacks + 1)}
    for layer in stack_layers:
        for crate_num, label in layer:
            stack[crate_num].appendleft(label)
    return stack

# Part 1
def execute_move_single(stacks, move):
    num_to_pop = move[0]
    from_, to_ = move[1]
    for i in range(num_to_pop):
        curr = stacks[from_].pop()
        stacks[to_].append(curr)

# Part 2
def execute_move_multiple(stacks, move):
    num_to_pop = move[0]
    from_, to_ = move[1]
    in_order = []
    for i in range(num_to_pop):
        curr = stacks[from_].pop()
        in_order.append(curr)
    for i in range(len(in_order) - 1, -1, -1):
        stacks[to_].append(in_order[i])

def find_top_crate_arrangement(filename="day5.txt"):
    stack_layers, moves = [], []
    part_1_res, part_2_res = [], []
    with open(filename) as file:
        for line in file:
            index_matches = []
            if line.rstrip() and line[1] == "1":
                num_stacks = (len(line) + 1) // 4
                continue
            if line.rstrip() and line[0] == "m":
                moves.append(decode_move(line))
                continue
            for i in range(len(line)):
                if match(r"[A-Z]", line[i]):
                    index_matches.append(((i + 3) // 4, line[i]))
            if index_matches:
                stack_layers.append(index_matches)

        part_1_stacks = create_stacks(stack_layers, num_stacks)
        part_2_stacks = create_stacks(stack_layers, num_stacks)

        for move in moves:
            execute_move_single(part_1_stacks, move)
            execute_move_multiple(part_2_stacks, move)

        for stack in part_1_stacks.values():
            part_1_res.append(stack[-1])
        
        for stack in part_2_stacks.values():
            part_2_res.append(stack[-1])
        
        return (''.join(part_1_res), ''.join(part_2_res))

print(find_top_crate_arrangement())