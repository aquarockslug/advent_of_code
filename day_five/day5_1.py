# day 5 #1 by Aquarock


def main():
    rules, data = read_file("data.txt")
    valid_updates: list[list[int]] = []

    for update in data:
        if follows_rules(update, rules):
            valid_updates.append(update)

    middles = [update[int(len(update) / 2)] for update in valid_updates]
    print(f"valid count: {len(valid_updates)}\nsum of middle values: {sum(middles)}")


def read_file(filename: str):
    with open(filename) as f:
        data = f.readlines()
        split_point = data.index("\n")
        return (
            [[int(c) for c in r.strip().split("|")] for r in data[0:split_point]],
            [[int(c) for c in d.strip().split(",")] for d in data[split_point + 1 :]],
        )


def follows_rules(update: list[int], rules: list[list[int]]):
    for r in rules:
        if r[0] in update:
            if r[1] in update[: update.index(r[0])]:
                return False
    return True


if __name__ == "__main__":
    main()
