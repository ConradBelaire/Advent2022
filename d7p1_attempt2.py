f = open("d7inpute.txt", "r")
lines = f.readlines()

dirs = {}  # Dict of dirs and their sizes
curr = []  # List of folders we are currently exploring

result = 0

for i in range(0, len(lines)):
    line = lines[i].strip().split(' ')
    if line[0] == "$" and line[1] == "cd":
        if line[2] != "..":
            curr.append(line[2])
            dirs[line[2]] = 0
        else:
            d = curr.pop()
            if dirs[d] <= 100000:
                result += dirs[d]
                print(d, dirs[d])
    elif line[0].isnumeric():
        for d in curr:
            dirs[d] += int(line[0])


print(dirs)
print(curr)

for d in curr:
    if dirs[d] <= 100000:
        result += dirs[d]
        print(d, dirs[d])


print(result)
