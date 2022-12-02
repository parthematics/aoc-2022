# Part 1
def find_elf_with_most_calories(filename="day1.txt"):
    max_sum = float('-inf')
    with open(filename) as file:
        curr_sum = 0
        for line in file:
            if not line.rstrip():
                max_sum = max(curr_sum, max_sum)
                curr_sum = 0
                continue
            else:
                curr_sum += int(line.rstrip())

    # Include the final calorie sum in the max calculation
    max_sum = max(max_sum, curr_sum)
    return max_sum

# Part 2
import heapq
def find_top_3_elves_with_most_calories(filename="day1.txt"):
    heap = []
    with open(filename) as file:
        curr_sum = 0
        for line in file:
            if not line.rstrip():
                if len(heap) == 3:
                    heapq.heappushpop(heap, curr_sum)
                else:
                    heapq.heappush(heap, curr_sum)
                curr_sum = 0
                continue
            else:
                curr_sum += int(line.rstrip())

    # Include the final calorie sum in the heap
    heapq.heappushpop(heap, curr_sum)
    return sum(heap)
    
print(find_elf_with_most_calories())
print(find_top_3_elves_with_most_calories())