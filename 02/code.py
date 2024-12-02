def process(filename: str) -> tuple[int, int]:
    reports: list[list[int]] = []
    with open(filename) as file:
        for line in file:
            reports.append([int(value) for value in line.strip().split(' ')])

    safe_reports: int = 0
    safe_reports_after_adjustment: int = 0
    for report in reports:
        if is_valid(report):
            safe_reports += 1
            safe_reports_after_adjustment += 1
            continue

        for index, el in enumerate(report):
            # list without one item
            adjusted_item = report[:index] + report[index + 1:]

            if is_valid(adjusted_item):
                safe_reports_after_adjustment += 1
                break

    return (safe_reports, safe_reports_after_adjustment)


def is_valid(report: list[int]) -> bool:
    MAX_DIFF = 3

    for prev, curr in zip(report, report[1:]):
        diff = curr - prev
        if curr == prev or abs(diff) > MAX_DIFF:
            return False

        if diff > 0 and report[0] > report[1]:
            return False

        if diff < 0 and report[0] < report[1]:
            return False

    return True


safe_reports_demo = process('data-demo.txt')
print(f"Safe reports demo: {safe_reports_demo[0]}")
assert safe_reports_demo[0] == 2
print(f"Safe reports demo after adjustment: {safe_reports_demo[1]}")
assert safe_reports_demo[1] == 4

safe_reports_real = process('data-real.txt')
print(f"Safe reports real: {safe_reports_real[0]}")
assert safe_reports_real[0] == 402
print(f"Safe reports real after adjustment: {safe_reports_real[1]}")
assert safe_reports_real[1] == 455
