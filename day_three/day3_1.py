import re

# Day 3 #1 by Aquarock


# return a tuple containing the parameters in the command
def parse_parameters(cmds):
    for c in cmds:
        yield re.compile(r"\d+").findall(str(c))


# find valid commands with a regular expression
def parse_commands(data: str):
    return re.compile(r"mul\(\d+,\d+\)").findall(data)


with open("data.txt") as f:
    products, data = [], "".join(f.readlines())
    for p in parse_parameters(parse_commands(data)):
        products.append(int(p[0]) * int(p[1]))

    print(sum(products))
