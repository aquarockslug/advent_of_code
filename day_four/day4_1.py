import re

# Day four #1 by Aquarocks

data = []
with open("data.txt") as f:
    data = f.readlines()

count = 0
for d in data:
    if re.search("XMAS", d): # forward
        count += 1
    if re.search("XMAS", d[::-1]): # backwards
        count += 1

print(count)
