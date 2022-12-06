# Part 1
def find_start_of_packet_marker(buffer, marker_length):
    l, r = 0, 0
    seen = set()
    while r < len(buffer):
        if r - l == marker_length - 1 and buffer[r] not in seen:
            return r + 1
        if buffer[r] not in seen:
            seen.add(buffer[r])
            r += 1
        else:
            while buffer[l] != buffer[r]:
                seen.remove(buffer[l])
                l += 1
            seen.remove(buffer[l])
            l += 1

# Part 1 + 2
test_filename = "day6_test.txt"
filename = "day6.txt"
with open(filename) as file:
    for line in file:
        print(find_start_of_packet_marker(line, 4)) # start-of-packer marker length
        print(find_start_of_packet_marker(line, 14)) # start-of-message marker length

