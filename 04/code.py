def find_xmas(filename: str) -> int:
    text = load_data(filename)
    count = 0

    for x in range(len(text)):
        # rows
        for item in zip(text[x], text[x][1:], text[x][2:], text[x][3:]):
            if item == ("X", "M", "A", "S") or item == ("S", "A", "M", "X"):
                count += 1

    for x in range(len(text) - 3):
        # cols
        for item in zip(text[x], text[x + 1], text[x + 2], text[x + 3]):
            if item == ("X", "M", "A", "S") or item == ("S", "A", "M", "X"):
                count += 1

        # diagonals left-to-right
        for item in zip(text[x], text[x + 1][1:], text[x + 2][2:], text[x + 3][3:]):
            if item == ("X", "M", "A", "S") or item == ("S", "A", "M", "X"):
                count += 1

        # diagonals right-to-left
        for item in zip(text[x][3:], text[x + 1][2:], text[x + 2][1:], text[x + 3]):
            if item == ("X", "M", "A", "S") or item == ("S", "A", "M", "X"):
                count += 1

    return count


def find_xmas_x(filename: str) -> int:
    text = load_data(filename)
    count = 0

    for x in range(len(text) - 2):
        for item in zip(
                text[x], text[x][2:],
                text[x + 1][1:],
                text[x + 2], text[x + 2][2:],
        ):
            if (
                    item == ("M", "S", "A", "M", "S") or
                    item == ("S", "M", "A", "S", "M") or
                    item == ("M", "M", "A", "S", "S") or
                    item == ("S", "S", "A", "M", "M")
            ):
                count += 1
    return count


def load_data(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


result = find_xmas('data-demo.txt')
print(f"XMAS count demo: {result}")
assert result == 18
result_x = find_xmas_x('data-demo.txt')
print(f"XMAS-X count demo: {result_x}")
assert result_x == 9

result_real = find_xmas('data-real.txt')
print(f"XMAS count real: {result_real}")
assert result_real == 2644
result_x_real = find_xmas_x('data-real.txt')
print(f"XMAS-X count real: {result_x_real}")
assert result_x_real == 1952
