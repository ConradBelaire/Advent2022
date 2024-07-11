import re
f = open("d4input.txt", "r")
total = 0

for line in f:
    line = line.strip()
    print(line)
    nums = list(map(int, (re.findall(r"\d+", line))))
    print(nums)
    if (nums[2] <= nums[0] <= nums[3]) or (nums[2] <= nums[1] <= nums[3]):
        print("A")
        total += 1
    elif (nums[0] <= nums[2] <= nums[1]) or (nums[0] <= nums[3] <= nums[1]):
        print("B")
        total += 1

print(total)
