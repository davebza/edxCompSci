s = 'azcbobobegghakl'

needle = "bob"
pointer = 0
count = 0

for c in s:
    target = s[pointer: pointer + 3]
    print(target)
    if target == needle:
        count += 1
    pointer += 1

print("Number of times bob occurs is: " + str(count))