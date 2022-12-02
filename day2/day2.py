# Part 1
# map[opp][you] maps to a tuple of (outcome score, shape score)
rps_map = {
    "A" : { # opponent rock
        "X" : (3, 1), # you play rock, draw
        "Y" : (6, 2), # you play paper, win
        "Z" : (0, 3) # you play scissors, loss
    },
    "B" : { # opponent paper
        "X" : (0, 1), # you play rock, loss
        "Y" : (3, 2), # you play paper, draw
        "Z" : (6, 3) # you play scissors, win
    },
    "C" : { # opponent scissors
        "X" : (6, 1), # you play rock, win
        "Y" : (0, 2), # you play paper, loss
        "Z" : (3, 3) # you play scissors, draw
    }
}

def find_total_incorrect_score(filename="day2.txt"):
    total_score = 0
    with open(filename) as file:
        for line in file:
            opp_move, your_move = line.rstrip().split()
            total_score += sum(rps_map[opp_move][your_move])
    return total_score

# Part 2
# map[opp][you] maps to a tuple of (outcome score, shape score)
correct_rps_map = {
    "A" : { # opponent rock
        "X" : (0, 3), # to lose, you play scissors
        "Y" : (3, 1), # to draw, you play rock
        "Z" : (6, 2) # to win, you play paper
    },
    "B" : { # opponent paper
        "X" : (0, 1), # to lose, you play rock
        "Y" : (3, 2), # to draw, you play paper
        "Z" : (6, 3) # to win, you play scissors
    },
    "C" : { # opponent scissors
        "X" : (0, 2), # to lose, you play paper
        "Y" : (3, 3), # to draw, you play scissors
        "Z" : (6, 1) # to win, you play rock
    }
}

def find_total_correct_score(filename="day2.txt"):
    total_score = 0
    with open(filename) as file:
        for line in file:
            opp_move, your_move = line.rstrip().split()
            total_score += sum(correct_rps_map[opp_move][your_move])
    return total_score

print(find_total_incorrect_score())
print(find_total_correct_score())