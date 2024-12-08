# Day 6 by Aquarock

startPos = []
with open("data.txt") as f:
    data = f.readlines()
    obstacles = [list(map(lambda c: c == "#", list(line.strip()))) for line in data]
    for i, line in enumerate(data):
        if line.__contains__("^"):
            startPos = [i, line.index("^")]

print(f"guard starting position: {startPos}")
