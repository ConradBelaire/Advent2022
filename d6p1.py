f = open("d6input.txt", "r")
line = f.readline().strip()

result = 0
recent = []
for c in line:
    result += 1
    recent.append(c)
    if len(recent) < 4:
        continue

    if len(set(recent)) == len(recent):
        print(recent, result)
        break

    recent.pop(0)

