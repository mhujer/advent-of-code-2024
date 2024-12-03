import re


def process_multiples(filename: str) -> int:
    memory = load_data(filename)

    items: list[tuple[str, str]] = re.findall(r'mul\((?P<numa>\d+),(?P<numb>\d+)\)', memory)

    sum_of_multiples: int = sum(int(a) * int(b) for a, b in items)

    return sum_of_multiples


def process_conditional_multiples(filename: str) -> int:
    memory = load_data(filename)

    matches = re.finditer(r"(?P<dont>don't)|(?P<do>do)|mul\((?P<numa>\d+),(?P<numb>\d+)\)", memory)
    result: int = 0
    enabled: bool = True
    for match in matches:
        match_groups = match.groupdict()
        if match_groups['dont'] is not None:
            enabled = False

        elif match_groups['do'] is not None:
            enabled = True

        elif enabled:
            result += int(match_groups['numa']) * int(match_groups['numb'])

    return result


def load_data(filename: str) -> str:
    with open(filename) as file:
        memory = ''.join(line for line in file)

    return memory


result = process_multiples('data-demo.txt')
print(f"Sum of multiples: {result}")
assert result == 161

result_cond = process_conditional_multiples('data-demo-part-2.txt')
print(f"Sum of conditional multiples: {result_cond}")
assert result_cond == 48

result_real = process_multiples('data-real.txt')
print(f"Sum of multiples: {result_real}")
assert result_real == 182619815

result_cond_real = process_conditional_multiples('data-real.txt')
print(f"Sum of conditional multiples: {result_cond_real}")
assert result_cond_real == 80747545
