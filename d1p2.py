f = open("d1input.txt", "r")
max = [0,0,0]
current = 0


for line in f:
    line = line.strip()
    if line == "":
        if current > max[0]:
            max[2] = max[1]
            max[1] = max[0]
            max[0] = current
        elif current > max[1]:
            max[2] = max[1]
            max[1] = current
        elif current > max[2]:
            max[2] = current
        current = 0
    else:
        current += int(line)

# Algorithm wasn't running for last elf
if current > max[0]:
    max[2] = max[1]
    max[1] = max[0]
    max[0] = current
elif current > max[1]:
    max[2] = max[1]
    max[1] = current
elif current > max[2]:
    max[2] = current

print(max)
print(sum(max))