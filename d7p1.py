f = open("d7input.txt", "r")
lines = f.readlines()

dirs = {}

for i in range(0, len(lines)):
    line = lines[i].strip().split(' ')
    if line[1] == "cd":
        if line[2] != "..":
            depth = 1
            dirs[line[2]] = 0
            j = 2
            while depth > 0:
                crawl = lines[i+j].strip().split(' ')
                print(crawl)
                if crawl[0].isnumeric():
                    dirs[line[2]] += int(crawl[0])
                    print(line[2], crawl[1], crawl[0], dirs[line[2]])
                elif crawl[1] == "cd":
                    if crawl[2] == "..":
                        depth -= 1
                    else:
                        depth += 1
                j += 1
                if i + j > len(lines)-1:
                    break
print(dirs)

result = 0
for d in dirs:
    if dirs[d] <= 100000:
        result += dirs[d]
        print(d, dirs[d])

print(result)
