import re
f = open("d5input.txt", "r")
result = ""

lines = f.readlines()
linebreak = lines.index("\n")
numStacks = int(lines[linebreak - 1][-3])
stacks = [[] for x in range(numStacks)]

for i in range(linebreak-2, -1, -1):
    for j in range(numStacks):
        if lines[i][1+j*4] == " ":
            continue
        #print(i, j, lines[i][1+j*4])
        stacks[j].append(lines[i][1+j*4])

print(stacks)

for line in lines[linebreak+1:]:
    command = list(map(int, re.findall(r"\d+", line)))
    print(command)
    stacks[command[2] - 1] += stacks[command[1]-1][-command[0]:]
    for i in range(0, command[0]):
        stacks[command[1]-1].pop()
    print(stacks)

for stack in stacks:
    result += stack.pop()
print(result)
