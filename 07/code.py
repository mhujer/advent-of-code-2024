import itertools


def calculate(filename: str) -> int:
    result = 0

    input = load_data(filename)

    for line in input:
        expected_result, operands = line

        operators_for_row = itertools.product('*+', repeat=len(operands) - 1)
        for operator_tuple in operators_for_row:
            operands_iter = iter(operands)
            res = next(operands_iter)
            for operator in operator_tuple:
                if operator == '+':
                    res += next(operands_iter)
                elif operator == '*':
                    res *= next(operands_iter)
                else:
                    raise ValueError('!')

            if res == expected_result:
                result += expected_result
                break

    return result


def calculate_part2(filename: str) -> int:
    result = 0

    input = load_data(filename)

    for line in input:
        expected_result, operands = line

        operators_for_row: iter[tuple[str,...]] = itertools.product('*+|', repeat=len(operands) - 1)
        for operator_tuple in operators_for_row:
            operands_iter = iter(operands)
            res = next(operands_iter)
            for operator in operator_tuple:
                if operator == '+':
                    res += next(operands_iter)
                elif operator == '*':
                    res *= next(operands_iter)
                elif operator == '|':
                    res = int(f"{res}{next(operands_iter)}")

            if res == expected_result:
                result += expected_result
                break

    return result


def load_data(filename: str) -> list[tuple[int, tuple[int, ...]]]:
    with open(filename) as file:
        return [
            (
                int(expected_result),
                tuple(map(int, operands.strip().split(' ')))
            )
            for expected_result, operands in (
                line.strip().split(':') for line in file.readlines()
            )
        ]

# part 1
result_demo = calculate('data-demo.txt')
print(f"demo result part 1: {result_demo}")
assert result_demo == 3749

result_real = calculate('data-real.txt')
print(f"real result part 1: {result_real}")
assert result_real == 1985268524462

# part 2
result_demo = calculate_part2('data-demo.txt')
print(f"demo result part 2: {result_demo}")
assert result_demo == 11387

result_real = calculate_part2('data-real.txt')
print(f"real result part 2: {result_real}")
assert result_real == 150077710195188
