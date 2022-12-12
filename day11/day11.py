from collections import deque, defaultdict

def conduct_monkey_inspection_rounds(num_rounds, worry_level_factor, is_test=True):
    monkey_items, monkey_operations = get_monkey_items_and_operations_map(is_test)
    monkey_item_inspection_frequency = defaultdict(int)

    # Keep an upper bound because multiplication will eventually become incredibly expensive as worries get larger.
    # If a worry level exceeds this limit, we'll wrap it back around (using mod) to keep the divisibility rules applicable.
    # Note: finding the LCM would also work, this is just a crude strategy.
    worry_limit = 1
    for monkey in range(len(monkey_items)):
        worry_limit *= monkey_operations[monkey][1]
    
    for i in range(num_rounds):
        for monkey in range(len(monkey_items)):
            curr_items_being_inspected = monkey_items[monkey]
            for _ in range(len(curr_items_being_inspected)):
                old = curr_items_being_inspected.popleft()
                transformation_rule, divisible_by = monkey_operations[monkey][0], monkey_operations[monkey][1]
                old = eval(transformation_rule) // worry_level_factor
                if old % divisible_by == 0:
                    monkey_to_send = monkey_operations[monkey][2]
                    monkey_items[monkey_to_send].append(old)
                else:
                    monkey_to_send = monkey_operations[monkey][3]
                    monkey_items[monkey_to_send].append(old % worry_limit)
                monkey_item_inspection_frequency[monkey] += 1
    
    most_common_1, most_common_2 = sorted(monkey_item_inspection_frequency.values(), key=lambda x: -x)[:2]
    return most_common_1 * most_common_2

def get_monkey_items_and_operations_map(is_test):
    monkey_notes = get_monkey_notes(is_test)
    curr_monkey = 0
    monkey_items = defaultdict(deque)
    monkey_operations = defaultdict(list) # map to a list of [operation, divisible_by_num, true case monkey, false case monkey]

    for line in monkey_notes:
        first_word = line.split()[0]
        match first_word:
            case "Monkey":
                curr_monkey = int(line.split()[1][:-1])
            case "Starting":
                item_worry_levels = line.split(": ")[1].split(", ")
                for item_worry in item_worry_levels:
                    monkey_items[curr_monkey].append(int(item_worry))
            case "Operation:":
                operation = line.split(" = ")[1]
                monkey_operations[curr_monkey].append(operation)
            case "Test:":
                divisible_by = int(line.split(" by ")[1])
                monkey_operations[curr_monkey].append(divisible_by)
            case "If":
                # will append true case first, then false case
                monkey_to_throw_to = int(line.split(" monkey ")[1])
                monkey_operations[curr_monkey].append(monkey_to_throw_to)

    return (monkey_items, monkey_operations)

def get_monkey_notes(is_test):
    input_file = "day11_test.txt" if is_test else "day11.txt"
    lines = [line.strip() for line in open(input_file, "r").read().splitlines() if line]
    return lines

# Part 1
print(conduct_monkey_inspection_rounds(20, 3, is_test=False))

# Part 2
print(conduct_monkey_inspection_rounds(10000, 1, is_test=False))