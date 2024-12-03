# day one by aquarock

a, b = [], []

# split data into part "a" and "b"
with open('data.txt') as f: data = f.readlines()
for d in data:
    s = d.split('   ')
    a.append(int(s[0]))
    b.append(int(s[1]))

product = 0
for d1 in a:
    count = 0
    for d2 in b:
        if (d1 == d2): count += 1
    if (count > 0): product += d1 * count

print(product)
