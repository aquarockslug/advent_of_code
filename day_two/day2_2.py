# day 2 #1

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def count_safe_reports(data, count = 0):

    def check_report(report) -> bool:

        print(report)

        for i in range(1, len(report)):
            diff = abs(report[i] - report[i - 1])
            if (not diff >= 1 and not diff <= 3):
                del report[i]
                if not check_report(report): return False

        if (not all(i < j for i, j in zip(report, report[1:])) and
             not all(i > j for i, j in zip(report, report[1:]))): return False

        return True

    for line in [line.strip().split(' ') for line in data]:
        if check_report([int(n) for n in line]): count += 1

    return count

with open('data.txt') as f: print(f"Count: {count_safe_reports(f.readlines())}")
