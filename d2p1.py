f = open("d2input.txt", "r")

# A and X = Rock
# B and Y = Paper
# C and Z = Scissors

result = 0
for line in f:
    if line[2] == 'X':
        result += 1
        if line[0] == 'A':
            result += 3
        elif line[0] == 'B':
            result += 0
        else:  # line[0] == 'C'
            result += 6

    elif line[2] == 'Y':
        result += 2
        if line[0] == 'A':
            result += 6
        elif line[0] == 'B':
            result += 3
        else:  # line[0] == 'C'
            result += 0

    else:
        result += 3
        if line[0] == 'A':
            result += 0
        elif line[0] == 'B':
            result += 6
        else:  # line[0] == 'C'
            result += 3

print(result)
