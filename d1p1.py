f = open("d1input.txt", "r")
max = 0
current = 0
# Wrote this elves list stuff before reading the rest of the challenge lol
elves = []
elf = []
for line in f:
    line = line.strip()
    if line == "":
        elves.append(elf)
        elf = []
        if current > max:
            max = current
        current = 0
    else:
        elf.append(line)
        current += int(line)


#print(elves)
print(max)