# day one by aquarock

pairs, distances, a, b = [], [], [], []

# split data into part "a" and "b"
with open('data.txt') as f: data = f.readlines()
for d in data:
    s = d.split('   ')
    a.append(s[0])
    b.append(s[1])

# calculate the distances and get sum
for pair in zip(sorted(a), sorted(b)): pairs.append((int(pair[0]), int(pair[1])))
for pair in pairs: distances.append(abs(pair[0] - pair[1]))
print(sum(distances))
