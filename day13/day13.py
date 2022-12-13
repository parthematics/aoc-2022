from functools import cmp_to_key

# Part 1
def find_num_of_well_ordered_packets(is_test):
    input_file = "day13_test.txt" if is_test else "day13.txt"
    all_packets = [eval(line) for line in open(input_file, "r").read().splitlines() if line]
    pair_index, in_right_order = 1, []

    for i in range(0, len(all_packets), 2):
        left, right = all_packets[i], all_packets[i + 1]
        if well_ordered(left, right) == 1:
            in_right_order.append(pair_index)
        pair_index += 1
    
    return sum(in_right_order)

# Part 2
def determine_decoder_key(is_test):
    input_file = "day13_test.txt" if is_test else "day13.txt"
    all_packets = [eval(line) for line in open(input_file, "r").read().splitlines() if line]
    all_packets.extend([[[2]], [[6]]])

    # sort packets in place
    all_packets.sort(key=cmp_to_key(well_ordered), reverse=True)
    first_divider_idx, second_divider_idx = all_packets.index([[2]]) + 1, all_packets.index([[6]]) + 1

    return first_divider_idx * second_divider_idx

def well_ordered(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif right < left:
            return -1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return well_ordered([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return well_ordered(left, [right])
    elif not left and right:
        return 1
    elif left and not right:
        return -1
    elif not left and not right:
        return 0
    else:
        first_comparison = well_ordered(left[0], right[0])
        if not first_comparison:
            return well_ordered(left[1:], right[1:])
        else:
            return first_comparison

print(find_num_of_well_ordered_packets(is_test=False))
print(determine_decoder_key(is_test=False))