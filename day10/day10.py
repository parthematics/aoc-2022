def find_signal_strengths_and_render_crt(is_test=True):
    program_instructions = get_program_instructions(is_test)
    instruction_to_cycles = {"noop": 1, "addx": 2}
    X, num_cycles = 1, 0

    # Part 1
    signal_strength_sum = 0
    cycles_of_interest = {40 * i - 20 for i in range(1, 7)}

    # Part 2
    crt_pixels = ["." for _ in range(240)]

    for instruction, delta_x in program_instructions:
        # increment cycle number
        for _ in range(instruction_to_cycles[instruction]):
            num_cycles += 1
            # Part 1
            if num_cycles in cycles_of_interest:
                signal_strength_sum += num_cycles * X
            # Part 2
            crt_pixels[num_cycles - 1] = draw_pixel(X % 40, (num_cycles - 1) % 40)

        X += delta_x
    
    # Part 2
    for pixel_idx in range(0, len(crt_pixels), 40):
        print(''.join(crt_pixels[pixel_idx : pixel_idx + 40]))

    return signal_strength_sum

def draw_pixel(sprite_pos, pixel_being_drawn):
    return "#" if sprite_pos - 1 <= pixel_being_drawn <= sprite_pos + 1 else "."

def get_program_instructions(is_test=True):
    input_file = "day10_test.txt" if is_test else "day10.txt"
    lines = open(input_file, 'r').read().splitlines()
    instructions = []
    for line in lines:
        parsed = line.split()
        if len(parsed) == 2:
            instructions.append((parsed[0], int(parsed[1])))
        else:
            instructions.append((parsed[0], 0))
    return instructions

# Part 1 + 2
print(find_signal_strengths_and_render_crt(is_test=False))