# day 2 #1

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def count_safe_reports(data, count = 0):

    def check_report(report) -> bool:
        if (not all(i < j for i, j in zip(report, report[1:])) and
            not all(i > j for i, j in zip(report, report[1:]))): return False
        return all(abs(i - j) >= 1 and abs(i - j) <= 3 for i, j in zip(report, report[1:]))

    for line in [line.strip().split(' ') for line in data]:
        if check_report([int(n) for n in line]): count += 1
    return count

with open('data.txt') as f: print(f"Count: {count_safe_reports(f.readlines())}")
