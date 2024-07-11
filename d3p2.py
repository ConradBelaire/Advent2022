
f = open("d3input.txt", "r")

total = 0

while True:
    seen = [set(), set(), set()]
    for i in range(0, 3):
        line = f.readline().strip()
        if not line:
            break

        for c in line:
            seen[i].add(c)
    else:
        final = seen[0] & seen[1] & seen[2]
        c = final.pop()
        if ord(c) > ord('a'):
            subtotal = ord(c) - ord('a') + 1
        else:
            subtotal = ord(c) - ord('A') + 27
        # print(c, subtotal)
        total += subtotal
        continue
    break

print(total)
