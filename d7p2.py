f = open("d7input.txt", "r")
lines = f.readlines()

dirs = {}  # Dict of dirs and their sizes
curr = []  # List of folders we are currently exploring

result = 0

for i in range(0, len(lines)):
    line = lines[i].strip().split(' ')
    if line[0] == "$" and line[1] == "cd":
        if line[2] != "..":
            if len(curr) == 0:
                path = ""
            else:
                path = curr[-1] + "/"
            curr.append(path + line[2])
            dirs[path + line[2]] = 0
        else:
            d = curr.pop()
    elif line[0].isnumeric():
        for d in curr:
            dirs[d] += int(line[0])


print(dirs)

target = 30000000 - 70000000 + dirs["/"]
best = dirs["/"]
for d in dirs:
    if target < dirs[d] < best:
        best = dirs[d]

print(target)
print(best)