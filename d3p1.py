
f = open("d3input.txt", "r")

total = 0

for line in f:
    line = line.strip()
    p1 = line[:len(line)//2]
    p2 = line[len(line)//2:]

    seen = set()
    for c in p1:
        seen.add(c)
    for c in p2:
        if c in seen:  # Found our matching character
            if ord(c) > ord('a'):
                subtotal = ord(c) - ord('a') + 1
            else:
                subtotal = ord(c) - ord('A') + 27
            #print(c, subtotal)
            total += subtotal
            break

print(total)
