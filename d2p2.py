f = open("d2input.txt", "r")

# A = Rock
# B = Paper
# C = Scissors

result = 0
for line in f:
    if line[0] == 'A': # Rock
        if line[2] == 'X': # Scissors
            result += 0 + 3
        elif line[2] == 'Y': # Rock
            result += 3 + 1
        else: # Paper
            result += 6 + 2

    elif line[0] == 'B': # Paper
        if line[2] == 'X': # Rock
            result += 0 + 1
        elif line[2] == 'Y': # Paper
            result += 3 + 2
        else: # Scissors
            result += 6 + 3

    else:  # Scissors
        if line[2] == 'X':  # Paper
            result += 0 + 2
        elif line[2] == 'Y':  # Scissors
            result += 3 + 3
        else:  # Rock
            result += 6 + 1

print(result)
