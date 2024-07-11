import re
f = open("d4input.txt", "r")
total = 0

for line in f:
    line = line.strip()
    print(line)
    nums = list(map(int, (re.findall(r"\d+", line))))
    print(nums)
    if (nums[0] <= nums[2] and nums[1] >= nums[3]):
        print("Found!")
        total += 1
    elif (nums[0] >= nums[2] and nums[1] <= nums[3]):
        print("Different found")
        total += 1

print(total)
